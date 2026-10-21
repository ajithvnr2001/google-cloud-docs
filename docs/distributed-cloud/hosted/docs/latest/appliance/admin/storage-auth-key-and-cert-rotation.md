---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/storage-auth-key-and-cert-rotation/
title: Rotate storage authentication keys and certificates \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:44.545719+00:00
---

# Rotate storage authentication keys and certificates  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/storage-auth-key-and-cert-rotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Rotate storage authentication keys and certificates Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped appliance adopts ONTAP Select (OTS) as the software-defined storage vendor. OTS has its own authentication system where each identity (core service or client) has associated name and a key.

This document describes the steps to rotate the authentication keys and certificates that must be performed for:

  * regularly scheduled key rotation to ensure that the device is compliant and secure.
  * key exposure. You should rotate the exposed key as soon as possible.



## Before you begin

Make sure you have the following access:

  * Admin console access to the ONTAP cluster
  * Kubeconfig for the Management API server



## Rotate IPsec credentials (PSK)

ONTAP supports certificate-based authentication for IPsec as of 9.10.1. This release of GDC is on 9.14.1 and uses pre-shared keys.

For Appliance, IPsec is implemented for two types of OTS traffic:

  * External traffic between baremetal hosts and SVMs.
  * Internal traffic between worker nodes.



We will go through them separately.

### Prerequisites

  * Admin console access to the ONTAP cluster
  * A new pre-shared key
  * Kubeconfig for the Management API server
  * Access to hosts to update StrongSwan configuration



### Impact

While IPsec policies are being rotated, hosts will experience a loss of IP connectivity to the storage system. Connections will stall or possibly fail depending on application behavior. You can pause user workloads during the rotation if possible, but it is not required. Connections should recover shortly after the secrets are reset.

### Key Rotation for OTS External Traffic

To validate rotation, use the following command and compare your output:
    
    
    export KUBECONFIG= #path to root-admin kubeconfig
    
    
    
    kubectl get StorageEncryptionConnections -n gpc-system
    

Output:
    
    
    NAME          INVENTORYMACHINE   STORAGEVIRTUALMACHINE   STORAGECIDR   PRESHAREDKEY                 READY   AGE
    bm-1ba9796c   bm-1ba9796c        root-admin              10.4.4.0/24   bm-1ba9796c-pre-shared-key   True    6h16m
    bm-96a5f32a   bm-96a5f32a        root-admin              10.4.4.0/24   bm-96a5f32a-pre-shared-key   True    16h
    bm-e07f4a4f   bm-e07f4a4f        root-admin              10.4.4.0/24   bm-e07f4a4f-pre-shared-key   True    21h
    

Verify that the `READY` field is true for the specific host that you executed the script earlier.

Manually rotate PSK if you find any error during validation.

  1. Execute the following command:
         
         export KUBECONFIG= #path to root-admin kubeconfig
         
         
         mgmt_ip="$(kubectl get storagecluster -A -o jsonpath='{.items[0].spec.network.clusterManagement.ip}')"
         
         username="$(kubectl get secret storage-root-level1 -n gpc-system -o jsonpath='{.data.username}' | base64 -d)"
         
         password="$(kubectl get secret storage-root-level1 -n gpc-system -o jsonpath='{.data.password}' | base64 -d)"
         

  2. View the password and copy it to clipboard:
         
         echo $password
         

  3. Log in to the ONTAP console:
         
         ssh $username@$mgmt_ip
         

When prompted for password, paste in the copied password from the previous step.

  4. Use the following script for credential rotation:
         
         export KUBECONFIG= #path to root-admin kubeconfig
         
         
         kubectl get StorageEncryptionConnections -n gpc-system
         

Output:
         
         NAME          INVENTORYMACHINE   STORAGEVIRTUALMACHINE   STORAGECIDR   PRESHAREDKEY                 READY   AGE
         bm-1ba9796c   bm-1ba9796c        root-admin              10.4.4.0/24   bm-1ba9796c-pre-shared-key   True    6h16m
         bm-96a5f32a   bm-96a5f32a        root-admin              10.4.4.0/24   bm-96a5f32a-pre-shared-key   True    16h
         bm-e07f4a4f   bm-e07f4a4f        root-admin              10.4.4.0/24   bm-e07f4a4f-pre-shared-key   True    21h
         

For every host you want to rotate, you can execute the following:
         
         export bm_host= //name of bm-host from above
         export secret="${bm_host}-pre-shared-key"
         export job_name="os-policy-config-host-ipsec-${bm_host}"
         export ns="gpc-system"
         export svm="$(kubectl get storageencryptionconnections "${bm_host}" -n "${ns}" -o jsonpath='{.spec.storageVirtualMachineRef.name}')"
         

Now confirm that you see all the components of the storage encryption connection. For admin cluster connections, either root-admin or organization-admin, you must use root-admin cluster.
         
         kubectl get secrets -n "${ns}" "${secret}"
         kubectl get jobs -n "${ns}" "${job_name}"
         

If both of these items are present, you can proceed on to the next step. If not, halt and don't proceed with modifying ipsec. Contact technical support.
         
         kubectl delete secrets -n "${ns}" "${secret}"
         kubectl delete jobs "${job_name}" -n "${ns}"
         

Now use the Management API server to delete the storageencryptionconnection
         
         export KUBECONFIG= #path to root-admin kubeconfig
         
         
         kubectl delete storageencryptionconnections "${bm_host}"
         
         annotation_key="reconcile_annotation_key"
         annotation_value="reconcile_annotation_value"
         
         kubectl patch storagevirtualmachines "${svm}" -n "${ns}" --type=merge -p "{\"metadata\":{\"annotations\":{\"$annotation_key\":\"$annotation_value\"}}}"
         kubectl patch storagevirtualmachines "${svm}" -n "${ns}" --type=json -p="[{\"op\": \"remove\", \"path\": \"/metadata/annotations/$annotation_key\"}]"
         

### Key Rotation for OTS Internal Traffic




Similarly, to validate rotation, use the following command and compare your output:
    
    
    export KUBECONFIG= #path to root-admin kubeconfig
    
    
    
    kubectl get secret ots-internal-pre-shared-key -n gpc-system
    

Output:
    
    
    NAME                          TYPE     DATA   AGE
    ots-internal-pre-shared-key   Opaque   1      18m
    
    
    
    kubectl get jobs -n gpc-system | grep os-policy-config-host-ipsec
    

Output:
    
    
    os-policy-config-host-ipsec-bm-3d33bb857t5bh                Complete   1/1           17s        10m
    os-policy-config-host-ipsec-bm-774fa8e6frgr7                Complete   1/1           30s        11m
    os-policy-config-host-ipsec-bm-8e452fb29q5wd                Complete   1/1           23s        11m
    

Verify that all the jobs are in `Complete` status.
    
    
    kubectl get StorageEncryptionConnections -n gpc-system
    

Output:
    
    
    NAME          INVENTORYMACHINE   STORAGEVIRTUALMACHINE   STORAGECIDR   PRESHAREDKEY                 READY   AGE
    bm-3d33bb85   bm-3d33bb85        root-admin              10.4.4.0/24   bm-3d33bb85-pre-shared-key   True    6h16m
    bm-774fa8e6   bm-774fa8e6        root-admin              10.4.4.0/24   bm-774fa8e6-pre-shared-key   True    16h
    bm-8e452fb2   bm-8e452fb2        root-admin              10.4.4.0/24   bm-8e452fb2-pre-shared-key   True    21h
    

Verify that the `READY` field is true for all the hosts.

  1. Delete all the CRs in step 2 with the listed order

     * Delete the secret for the internal traffic `sh kubectl delete secret ots-internal-pre-shared-key -n gpc-system`

     * Delete all three os policy jobs `sh kubectl delete jobs os-policy-config-host-ipsec-bm-3d33bb857t5bh -n gpc-system kubectl delete jobs os-policy-config-host-ipsec-bm-774fa8e6frgr7 -n gpc-system kubectl delete jobs os-policy-config-host-ipsec-bm-8e452fb29q5wd -n gpc-system`

     * Delete all three storageencryptionconnection `sh kubectl delete StorageEncryptionConnections bm-3d33bb85-root-admin -n gpc-system kubectl delete StorageEncryptionConnections bm-774fa8e6-root-admin -n gpc-system kubectl delete StorageEncryptionConnections bm-8e452fb2-root-admin -n gpc-system`

  2. Wait for a few minutes (~3-5 mins). Repeat step 2 until every CR is in READY or Complete status.




## Rotate volume keys

This section describes the manual steps to rotate OTS volume credentials.

### Before you begin

Complete the following steps:

  1. Verify that you meet the [laptop prerequisites](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/laptop). 
  2. Ensure that you can login to the console of the OTS cluster through BM01 or BM02. 



### Initiate volume key rotation

In the OTS console, trigger the one-off key rotation:
    
    
    volume encryption rekey start -vserver SVM_name -volume volume_name
    

The following command changes the encryption key for `vol1` on `SVMvs1`:
    
    
    cluster1::> volume encryption rekey start -vserver vs1 -volume vol1
    

To see the names of the vservers and the volumes, you can use the `show` command:
    
    
    vserver show
    volume show
    

### Verify volume key rotation

After the key rotation is initiated, check the rekey status:
    
    
    volume encryption rekey show
    

Display the status of the rekey operation:
    
    
    cluster1::> volume encryption rekey show
    
    Vserver   Volume   Start Time           Status
    -------   ------   ------------------   ---------------------------
    vs1       vol1     9/18/2017 17:51:41   Phase 2 of 2 is in progress.
    

When the rekey operation is complete, verify that the volume is enabled for encryption:
    
    
    volume show -is-encrypted true
    

Display the encrypted volumes on `cluster1`:
    
    
    cluster1::> volume show -is-encrypted true
    
    Vserver  Volume  Aggregate  State  Type  Size  Available  Used
    -------  ------  ---------  -----  ----  -----  --------- ----
    vs1      vol1    aggr2     online    RW  200GB    160.0GB  20%
    

## Rotate external HSM certificates

This section describes how to rotate and update the external HSM certificates for ONTAP.

### Prerequisites

  * Admin access to the ONTAP cluster or relevant SVMs
  * Current password
  * kubectl access to the appropriate cluster(s)



### Instructions

  1. Back up the old HSM certificates:
         
         kubectl get secret aa-aa-external-hsm-creds -n gpc-system -o yaml > external-hsm-creds-old.yaml
         

  2. Update the HSM certificates secret in Kubernetes:

     1. Copy the old secret yaml file: `sh cp external-hsm-creds-old.yaml external-hsm-creds-new.yaml`

     2. Update the new `external-hsm-creds-new.yaml` file with the new HSM credentials including the server CA certficiate, the public client certificate, and the private key for the client.

     3. Apply the change and update the HSM secret object.
            
            kubectl apply -f external-hsm-creds-new.yaml
            

  3. Update the HSM certificates in ONTAP:

     1. Log into the ONTAP CLI.

     2. Install the new server CA certificate:
            
            cluster::> security certificate install -type server-ca -vserver <>
            

     3. Install the new client certificate:
            
            cluster::> security certificate install -type client -vserver <>
            

     4. Update the key manager configuration to use the newly installed certificates:
            
            cluster::> security key-manager external modify -vserver <> -client-cert <> -server-ca-certs <
            




### Validation

  1. Verify the change with key manager status:
         
         cluster::> security key-manager external show-status
         

Check if the key servers are still in `Available` status.




## Rotate storage admin credential

This section describes how to rotate and set the storage admin user and password.

### Prerequisites

  * Admin access to the ONTAP cluster or relevant SVMs
  * Current password
  * kubectl access to the appropriate cluster(s)



### Instructions

  1. Start with the following command and then follow the resulting prompts:
         
         cluster::> security login password
         

  2. Update the secret to match:

     * **Option 1 (Interactive)** :
           
           kubectl edit secret -n <netapp_namespace> netapp_credential
           

Use the editor to change the password to the new base64-encoded value.

     * **Option 2 (Patch with jq dependency)** :
           
           k get secret -n <netapp_namespace> netapp_credential -o json | jq '.data["password"]="<new-base64-encoded-password>"' | kubectl apply -f -
           




## Rotate ONTAP emergency access credentials

During file and block storage setup, four emergency access user accounts are created that can be used to access ONTAP directly. These credentials can be obtained as secrets in the Management API server. Once those credentials have been used, they need to be rotated.

Two types of secrets are created during setup, level 1 and level 2. Level 1 is `storage-root-level1 and storage-root-level1-backup`. Level 2 is `storage-root-level2 and storage-root-level2-backup`. Level 2 secrets need to be stored in the safe and each level has two secrets, normal and backup. While the software handles deletion of both normal and backup secrets simultaneously, we recommend only rotating one of these partner secrets at once as an added layer of security.

While level 1 secrets are rotated automatically after a period of 90 days, level 2 secrets are not. Either type of secret must be rotated manually using the following process if it is used.

### Prerequisites

  * Access required: Management API server



### Validation

  1. Secret rotation can be validated by checking if the secret is still marked for deletion. If it is not, the secret has been rotated. Follow step one in the following instructions to check.
  2. If the secret is a level 2 secret, copy it on physical media and store it in the safe. Then the secret should be marked persisted using annotation `"disk.gdc.goog/persisted"`.
         
         kubectl annotate secrets
          <secret_name> -n gpc-system disk.gdc.goog/persisted=''
         




Use the following instructions to manually rotate secret if you find any error during validation.

### Instructions

  1. Check if a secret is marked for deletion:

     1. Run the following command:
            
            kubectl get secret <secret_name> -n gpc-system -o yaml
            

     2. If the `deletionTimestamp` field is present in the response as per this example, the secret is marked for deletion. Otherwise, it is not.
            
            apiVersion: v1
            data:
              password: KFZbQTJdYjIwSUtVVV1aNytJJVM=
              username: cm9vdC1sdmwy
            immutable: true
            kind: Secret
            metadata:
              annotations:
                cluster-name: aa-aa-stge01
              creationTimestamp: "2022-12-21T05:03:02Z"
              deletionGracePeriodSeconds: 0
              deletionTimestamp: "2022-12-21T14:42:13Z"
              finalizers:
              - ontap.storage.private.gdc.goog/breakglass-finalizer
              labels:
                breakglass-secret: "true"
              name: storage-root-level2
              namespace: gpc-system
              resourceVersion: "591897"
              uid: 6f331f8a-bf48-4d59-9725-6c99c5e766f7
            type: Opaque
            
            

  2. Rotate the secret after using it to access ONTAP:

     1. Check if the partner credential exists and is not marked for deletion. Don't proceed and come back to these steps in the future if it is marked for deletion.
     2. If level 2 secret is being rotated, the partner secret must be marked persisted by adding `disk.gdc.goog/persisted` annotation:
            
            kubectl annotate secrets
            <secret_name> -n gpc-system disk.gdc.goog/persisted=''
            

     3. Delete the secret from the cluster using the following:
            
            kubectl delete
            secret <secret_name> -n gpc-system
            

     4. At this point, the deletion process will start (and can be confirmed by checking if the secret is marked for deletion). It can take close to an hour for the secret to be deleted and regenerated.




## Rotate storage admin and SVM certificates

These certificates are the _server_ certificates installed into the ONTAP system by GDC.

There is one certificate for the _storage admin_ , also known as the _cluster admin_ account. Its name is prefixed with the ONTAP system's hostname, and has a trailing unique hash. It is installed in the cluster admin vserver. GDC uses this certificate internally for administrative tasks.

There are also several server-side certificates that are defined for ONTAP SVMs. These establish authenticity for clients talking to the SVMs.

All certificates can be rotated using the same process. Due to a root-ca certificate mismatch in the root-admin cluster, for cluster and SVM certificates, which are listed in the following tables, rotation requires rotating all certificates within the respective list. This means that if any cluster certificate needs to be rotated, all other cluster certificates must also be rotated. The same applies to SVM certificates. This limitation will be addressed once automated certificate management is implemented.

### Prerequisites

  * Admin access to the ONTAP cluster or relevant SVMs
  * kubectl access to the appropriate Kubernetes cluster(s)
  * reinstall client-ca certificates outlined in client-ca certificates installation steps.



### Mapping between certificates and Kubernetes secrets

For each certificate installed in ONTAP, there is a corresponding Kubernetes secret in the Management API server that contains the certificate details. GDC generates the certificates, and the process for replacing a certificate is simple: delete the secret that corresponds to a given certificate, and the certificate will be regenerated immediately. That new certificate can then be installed into ONTAP manually, replacing the old one.

Use `kubectl get secrets -n <namespace> -s <secret> -o yaml` to inspect the certificate in Kubernetes and verify that it matches the details in ONTAP seen from `security certificate show -vserver <svm_name>`. The namespace will always be "gpc-system" and you can refer to the proceeding table for the secret name.

You can also see the mapping of Certificate to Secret by checking:
    
    
    kubectl get certificates -n <namespace>
    

### Relevant Cluster Certificates

**ONTAP Common Name** | **Vserver** | **K8S Certificate Name** | **Kubernetes Secret Name** | **Description**  
---|---|---|---|---  
N/A  | <hostname> | <hostname>-admin-cert  | <hostname>-admin-cert-secret  | Cluster admin cert   
N/A  | <hostname> | <hostname>-server-cert  | <hostname>-server-cert-secret  | Server cert signed by the GDC issuer used as the ONTAP server cert   
N/A  | <hostname> | <hostname>-read-only-cert  | <hostname>-read-only-cert-secret  | Read-only monitoring access   
  
### Relevant SVM Certificates

**Vserver** | **K8S Certificate Name** | **Kubernetes Secret Name** | **Description**  
---|---|---|---  
root-admin  | root-admin-server-cert  | root-admin-server-cert-secret  | Server cert signed by the GDC issuer used as the SVM server cert   
root-admin  | root-admin-s3-server-cert  | root-admin-s3-server-cert-secret  | Server cert signed by the GDC issuer used as the ONTAP S3 server cert   
root-admin  | root-admin-client-cert  | root-admin-client-cert-secret  | SVM administrator access   
root-admin  | root-admin-s3-identity-client-cert  | root-admin-s3-identity-client-cert-secret  | S3 identity access   
  
### Validation

#### Vserver certificate

After all certificates are rotated, verify that the trident backend is still connected successfully for every cluster associated with the server cert rotated.

  1. Execute the following:
         
         export KUBECONFIG= #path to root-admin kubeconfig
         
         
         kubectl get tridentbackendconfigs -n netapp-trident
         

Output should look like:
         
         NAME                                   BACKEND NAME   BACKEND UUID                           PHASE   STATUS
         netapp-trident-backend-tbc-ontap-san   iscsi-san      a46ce1c7-26da-42c9-b475-e5e37a0911f8   Bound   Success
         

  2. Verify that the `PHASE` is **Bound** and the `Status` is **Success**.




#### Root admin certificate

To test the admin certificate, we can create a new test StorageVirtualMachine and see that GDC is able to reconcile it appropriately. The steps for this are as follows:

  1. List the existing StorageVirtualMachines and pick one to clone as a test.
  2. Extract the Kubernetes spec for it.
  3. Edit the definition to change the name and delete unnecessary fields.
  4. Apply the test definition.
  5. Wait for the StorageVirtualMachine status to become `Ready`.
  6. Delete the test StorageVirtualMachine.
  7. Delete the actual SVM from ONTAP.



#### Example

This example uses a GDC NetApp namespace `gpc-system` and clones the `organization-root-user` temporarily to a new SVM called `test-svm`.

  1. List SVMs:
         
         kubectl get storagevirtualmachines -n ngpc-system
         

Output:
         
         NAME                      AGE
         organization-root-admin   13d
         

  2. Extract the spec:
         
         kubectl get storagevirtualmachines -n gpc-system -o yaml > svm.yaml
         

  3. Edit the spec to look similar to the following:
         
         apiVersion: system.gpc.gke.io/v1alpha1
         kind: StorageVirtualMachine
         metadata:
           labels:
             ontap.storage.gpc.gke.io/role: user
           name: test-svm
           namespace: netapp-alatl12-gpcstge02
         spec:
           aggregates:
           - alatl12-gpcstge02-c1-aggr1
           - alatl12-gpcstge02-c2-aggr1
           clusterName: alatl12-gpcstge02
           iscsiTarget:
             port: a0a-4
             subnetName: root-svm-data
           nasServer:
             port: a0a-4
             subnetName: root-svm-data
           svmNetwork:
             port: e0M
             subnetName: Default
         

  4. Apply it to the cluster:
         
         kubectl create -f svm.yaml
         

  5. Wait for the new SVM to become ready. Periodically observe the output of:
         
         kubectl get storagevirtualmachines -n gpc-system test-svm
         

Success is indicated by:
         
         Conditions:
             Last Transition Time:  2022-03-30T21:30:27Z
             Message:
             Observed Generation:   1
             Reason:                SVMCreated
             Status:                True
             Type:                  Ready
         

or `AnsibleJobSucceed`.

  6. Delete the SVM resource:
         
         kubectl delete storagevirtualmachines -n gpc-system test-svm
         

  7. Fully delete it from ONTAP. Deleting the resource does not remove it from ONTAP.

Log in to the NetApp console and delete the SVM:
         
         alatl12-gpcstge02::> vserver delete test-svm
         

Output:
         
         Warning: When Vserver "test-svm" is deleted,
                 the following objects are automatically removed as well:
                 LIFs: 7
                 Routes: 2
                 Admin-created login accounts: 2
                 Do you want to continue? {y|n}: y
         [Job 3633] Success
         




Use the following instructions to manually rotate ONTAP certificate if you find any error during validation.

### Instructions

If the preceding ONTAP certificate name is not applicable, nothing needs to be rotated in ONTAP. Inspect the certificate and secret in Kubernetes and delete the secret.

  1. Generate a new certificate, referencing the preceding table for the secret name:
         
         kubectl get certificates -n <namespace>
         
         
         $ kubectl patch Certificates <cert_name> -n gpc-system \
          --type=merge -p "{\"spec\":{\"privateKey\": {\"rotationPolicy\": \"Always\"}}}"
         $ kubectl delete secret -n <namespace> <secret_name>
         

  2. View the installed certificates for a given vserver, for certificates installed in ONTAP (not marked as not applicable):
         
         cluster::> security certificate show -vserver <svm_name> -type server
         

  3. Inspect the matching secret in Kubernetes (reference the previous table):
         
         kubectl get certificates -n <namespace>
         

  4. When satisfied with the match, generate a new certificate by deleting the secret:
         
         kubectl delete secret -n <namespace> <secret_name>
         

  5. Re-inspect the secret to see that a new certificate has been regenerated. Once that is confirmed, create a new server certificate in ONTAP. **Only** do the following steps for the preceding certificates with "server-cert" suffix.

  6. Extract the new TLS certificate body using `kubectl` and other tools directly, and install it into ONTAP:
         
         $ gdch_cert_details -n <namespace> -s <secret_name>
         
         cluster::> security certificate install -vserver <svm_name> -type server
         

First prompt will be:

`Please enter Certificate: Press <Enter> when done`

To which you should enter `tls.crt`. In case there are multiple cert blocks in `tls.crt`, enter the first block, and keep remaining cert blocks as intermediates cert for reference in the next step.

  7. The system will prompt: `Please enter Private Key: Press <Enter> when done`. Paste the contents of your `tls.key` file and press Enter.

Next, it will prompt: `Do you want to continue entering root and/or intermediate certificates {y|n}:` If your `tls.crt` file contains only a single certificate, type `N` and press Enter. Otherwise, type `Y` and press Enter.

**If you typed`Y`:** You will be prompted to enter intermediate certificates. Paste them one at a time from your `tls.crt` file, pressing Enter after each. Finally, paste the root certificate from your `ca.crt` file and press Enter.

**If you typed`N`:** (No further action needed regarding certificates at this prompt)

ONTAP will then return a serial number. Record this number, as it represents the serial number of the new certificate and CA. This serial number will be referred to as `<new\_server\_serial>` and `<new\_ca>` in subsequent steps. Do **not** follow these certificate steps if you are configuring an S3 server certificate.

  8. View the current state of ssl configs for the vserver and cluster. Keep handy the _Server Certificate Issuing CA_ , the _Server Certificate Common Name_ , and the _Server Certificate Serial Number_ , as these will be referred to as `<old\_server\_common\_name>`, `<old\_ca>`, and `<old\_server\_serial>` respectively:
         
         cluster::> security ssl show -vserver <vserver>
         

This returns the ssl info, with the old server cert info. You can reference this later to make sure it has been updated, after you modify the ssl config.

  9. Modify the ssl config:
         
         cluster::> security ssl modify -server-enabled -client-enabled true -vserver <svm_name> -serial <new_server_serial> -ca <new_ca>
         

  10. View the new state of ssl configs for the vserver and cluster. This should have the updated serial number for the server cert now installed:
         
         cluster::> security ssl show -vserver <vserver>
         

  11. Delete the old server certificate after verifying the previous step:
         
         cluster::> security certificate delete -vserver <svm_name> -common-name <old_server_common_name> -ca <old_ca> -type server -serial <old_server_serial>
         




## Client-CA certificates

  1. Fetch all CA certificates from the `trust-store-internal-only` ConfigMap in the `gpc-system` namespace using the following command:
         
         kubectl get cm -n gpc-system trust-store-internal-only -o jsonpath='{.data.ca\.crt}'
         

  2. For each CA certificate retrieved in the previous step, execute the following command on your ONTAP cluster:
         
         cluster::> security certificate install -vserver <svm_name> -type client-ca
         

You will be prompted: `Please enter Certificate: Press <Enter> when done.` Paste each certificate block retrieved in step 1 and press Enter. Repeat this installation command for each CA certificate.




## Rotate Harvest certificates

Harvest certificate generation depends on `<hostname>-read-only-cert-secret`. Ensure `<hostname>-read-only-cert-secret` is rotated before proceeding.

  1. View the installed certificates for the Harvest pod:
         
         export KUBECONFIG= #path to root-admin kubeconfig
         
         
         cluster_name="$(kubectl get storagecluster -A -o jsonpath='{.items[0].metadata.name}')"
         secret_name="$cluster_name"-read-only-cert-secret
         
         
         export TLS_CRT="$(kubectl get secret -n gpc-system $secret_name -o jsonpath='{.data.tls\.crt}')"
         
         
         export TLS_KEY="$(kubectl get secret -n gpc-system $secret_name -o jsonpath='{.data.tls\.key}')"
         
         
         export CA_CRT="$(kubectl get secret -n gpc-system $secret_name -o jsonpath='{.data.ca\.crt}')"
         

  2. Patch the Harvest credentials secret to supply the updated certificates:
         
         $ kubectl patch secret \
         -n gpc-system netapp-harvest-configuration-credential \
         -p "{\"data\":{\"tls.crt\":\"${TLS_CRT:?}\",\"tls.key\":\"${TLS_KEY:?}\",\"ca.crt\":\"${CA_CRT:?}\"}}"
         

  3. Restart the Harvest service to load the updated configuration:
         
         kubectl delete pod -n gpc-system -l 'app=harvest.netapp.io'
         




## Rotate file-system certificates

Run the following command to regenerate `file-storage-webhooks-serving-cert` and `file-observability-backend-target-cert` cert
    
    
    kubectl delete secret file-storage-webhooks-serving-cert -n file-system
    kubectl delete secret file-observability-backend-target-cert -n file-system
    

Restart pods to load the updated configuration:
    
    
    kubectl delete pod -n file-system -l 'app=file-observability-backend-controller'
    kubectl delete pod file-storage-backend-controller -n file-system
    

## Rotate Trident and ONTAP certificates

Trident must communicate with ONTAP. This is configured with the Trident backend which uses the client cert `<svm\_name>-client-cert-secret>` defined earlier. The client cert rotation is not part of Trident, but Trident relies on pieces of this cert, which need to be updated.

### Instructions

**For CA cert update:**

  1. Export `KUBECONFIG` to point to the kubeconfig for the cluster specific to the Trident components in question. Each cluster will have Trident configured on it.

  2. Grab the ca cert, base64 encoded from the client-cert secret and store it as a variable:
         
         ca_cert=$(kubectl get secrets -n "${ns}" "${secret}" -o jsonpath='{.data.ca\.crt}')
         

  3. Patch the tridentBackendConfig object:
         
         kubectl patch tridentBackendConfigs netapp-trident-backend-tbc-ontap-san -n netapp-trident --type=merge -p "{\"spec\":{\"trustedCACertificate\":\"$ca_cert\"}}"
         




**For the actual client cert and key:**

  1. Grab the tls cert, base64 encoded from the client-cert secret and store it as a variable:
         
         tls_cert=$(kubectl get secrets -n "${ns}" "${secret}" -o jsonpath='{.data.tls\.crt}')
         

  2. Grab the tls key, base64 double encoded from the client-cert secret and store it as a variable:
         
         tls_key=$(kubectl get secrets -n "${ns}" "${secret}" -o jsonpath='{.data.tls\.key}' | base64 -w 0)
         

  3. Update the backend secret with the private key:
         
         kubectl patch secrets netapp-trident-backend-tbc-ontap -n netapp-trident --type=merge -p "{\"data\":{\"clientPrivateKey\": \"$tls_key\"}}"
         

  4. Patch the backend config with the tls certificate:
         
         kubectl patch tridentBackendConfigs netapp-trident-backend-tbc-ontap-san -n netapp-trident --type=merge -p "{\"spec\":{\"clientCertificate\":\"$tls_cert\"}}"
         




## Rotate Trident controller certificates

The Trident containers must communicate with the Trident Operator. This communication is done over HTTPs, and server and client certs need to be managed as a part of this.

### Validation

Confirm that both the daemonset and deployment (where applicable) comes up in a healthy state.

Use the following instructions to manually rotate server and client certs if you find any error during validation.

### Instructions

Both the server and client certs have no corresponding cert on the ONTAP side. These are strictly contained in the clusters.

  1. Delete the secret corresponding to the cert that is expiring.
         
         kubectl delete secret -n netapp-trident <secret_name>
         

  2. Restart the netapp-trident-csi daemonset:
         
         kubectl rollout restart daemonset netapp-trident-csi -n netapp-trident
         

  3. For server certificate rotations, you will also need to restart the netapp-trident-csi deployment:
         
         kubectl rollout restart deployments netapp-trident-csi -n netapp-trident
         




## Trident CA certificate

The CA cert is used to provide the certificate authority for signing the Trident server and client certs.

**Certificate Name** | **Namespace** | **Secret** | **Description**  
---|---|---|---  
netapp-trident-csi-cert  | netapp-trident  | netapp-trident-csi-cert  | Trident CA Cert   
  
#### Validation

You see that the secret is regenerated. In order for the client and server certs to take effect, you can also follow rotating the Trident controller certificates in the preceding instructions after rotating this cert.

Use the following instructions to manually rotate the CA certificate if you find any error during validation.

#### Instructions

To rotate this key, you only need to delete the secret from Kubernetes:
    
    
    kubectl delete secret -n netapp-trident <secret_name>
    

## Trident CSI nodes and SVMs (data)

This is a svm-wide set of iSCSI CHAP credentials to enable access to the data plane for block access. This does not apply to file protocols.

**Management API server**

**Namespace** | **Secret** | **Description**  
---|---|---  
gpc-system  | <organization>-<type>-svm-credential  | SVM configuration needed for Trident setup   
  
**Org admin and Management API server**

**Namespace** | **Secret** | **Description**  
---|---|---  
gpc-system  | <organization>-<type>-svm-credential  | SVM configuration needed for Trident setup   
netapp-trident  | netapp-trident-backend-tbc-ontap  | Secret needed to manage Trident backend   
  
#### Validation

  1. Verify that backend is still configured successfully:
         
         #export kubeconfig of org cluster
         export KUBECONFIG= #path to root-admin kubeconfig
         
         kubectl get tridentBackendConfigs -n netapp-trident
         

  2. Verify that backend status is `Success`.




Use the following instructions to manually rotate the secrets if you find any error during validation.

#### Instructions

Generate a new random string of 16 length with no special characters for both the initiator secret and the target initiator secret:
    
    
    #export kubeconfig of Management API server
    export KUBECONFIG= #path to root-admin kubeconfig
    
    initiator_secret=$(head /dev/random | tr -dc A-Za-z0-9 | head -c16 | base64)
    
    target_secret=$(head /dev/random | tr -dc A-Za-z0-9 | head -c16 | base64)
    
    kubectl patch secrets -n gpc-system "$org-$type-svm-credential" --type=merge -p "{\"data\":{\"initiatorSecret\": \"$initiator_secret\", \"targetSecret\": \"$target_secret\"}}"
    
    #export kubeconfig of org cluster
    export KUBECONFIG= #path to root-admin kubeconfig
    
    kubectl patch secrets -n netapp-trident netapp-trident-backend-tbc-ontap --type=merge -p "{\"data\":{\"chapInitiatorSecret\": \"$initiator_secret\", \"chapTargetInitiatorSecret\": \"$target_secret\"}}"
    
    

## Trident AES key

The AES key is used internally by Trident to encrypt iSCSI CHAP credentials for internal use of Trident. It is a random sequence of characters that must be 32 bytes in length.

**Cluster running Trident (could be root/org-admin/user/system) clusters**

**Namespace** | **Secret** | **Description**  
---|---|---  
netapp-trident  | netapp-trident-aes-key  | AES key needed by Trident to encrypt iSCSI CHAP credentials   
  
### Validation

  1. Verify that the backend is still configured successfully:
         
         #export kubeconfig of org cluster
         export KUBECONFIG= #path to root-admin kubeconfig
         
         kubectl get tridentBackendConfigs -n netapp-trident
         

  2. Verify that backend status is `Success`.

  3. Attempt to create a test volume:

     1. Create a YAML file with the pvc info in it:
            
            echo "
            kind: PersistentVolumeClaim
            apiVersion: v1
            metadata:
              name: block-pvc
            spec:
              accessModes:
                - ReadWriteOnce
              resources:
                requests:
                  storage: 5Gi
              storageClassName: standard-rwo" > pvc.yaml
            

     2. Apply it to the Kubernetes cluster:
            
            kubectl apply -f pvc.yaml
            

  4. Verify that there are no errors in CSI logs due to iSCSI encryption:
         
         kubectl logs deploy/netapp-trident-csi -n netapp-trident -c trident-main | grep "Error encrypting"
         

You see no logs returned if there were no errors.

  5. Clean up file and pvc:
         
         kubectl delete -f pvc.yaml
         rm -f pvc.yaml
         




Use the following instructions to manually rotate the key if you find any error during validation.

#### Instructions

Before rotating this key, ensure that there are no pending pods with PVs in the cluster. If there are, wait for them to fully provision before rotating the key.

Generate a new random string of 32 length with no special characters for the aesKey:
    
    
    #export kubeconfig of org cluster
    export KUBECONFIG= #path to root-admin kubeconfig
    
    aes_key=$(head /dev/random | tr -dc A-Za-z0-9 | head -c32 | base64)
    
    #save old key just in case of errors
    old_key=$(kubectl get secrets -n netapp-trident "netapp-trident-aes-key" -o jsonpath='{.data.aesKey}')
    
    kubectl patch secrets -n netapp-trident "netapp-trident-aes-key" --type=merge -p "{\"data\":{\"aesKey\": \"$aes_key\"}}"
    
    kubectl rollout restart deployment netapp-trident-csi -n netapp-trident
    

#### Rollback

  1. Roll back to the last used creds if there are errors:
         
         kubectl patch secrets -n netapp-trident "netapp-trident-aes-key" --type=merge -p "{\"data\":{\"aesKey\": \"$old_key\"}}"
         
         kubectl rollout restart deployment netapp-trident-csi -n netapp-trident
         

  2. Redo the verification steps.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

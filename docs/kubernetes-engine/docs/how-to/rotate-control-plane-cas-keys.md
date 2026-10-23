---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rotate-control-plane-cas-keys/
title: Rotate customer-managed control plane CAs and keys \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:11.260505+00:00
---

# Rotate customer-managed control plane CAs and keys  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rotate-control-plane-cas-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Rotate customer-managed control plane CAs and keys Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Note:** This document uses a [general availability](https://cloud.google.com/products#product-launch-stages) feature named _GKE control plane authority_ that's only available for eligible Google Cloud customers. To request access to this feature, contact your Google Cloud account team.

This page shows cluster administrators and Security engineers how to rotate the certificate authorities (CAs) and service account signing keys that you configured for GKE control plane authority.

You should be familiar with the following concepts:

  * [Key and credential management](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-control-plane-authority#key-credential-management).
  * [Rotation of customer-managed credentials](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-control-plane-authority#rotation-customer-managed-credentials).
  * [Considerations for asymmetric keys](https://docs.cloud.google.com/kms/docs/key-rotation#asymmetric).



## Plan credential rotations

This document shows you how to rotate the following credential components in your control plane:

  * The cluster root CA, the aggregation root CA, the etcd API root CA, and the etcd peer root CA.
  * The Kubernetes ServiceAccount signing and verification keys.



You can also rotate the customer-managed encryption keys that you used to encrypt your control plane boot disks, etcd disks, and the etcd internal backup that Google Cloud uses for disaster recovery. For more information, see [Rotate etcd and control plane boot disk encryption keys](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rotate-etcd-kcp-encryption-keys).

**Best practice** : 

Validate your key and credential rotation procedures _before_ an actual incident occurs.

Rotate your credentials to avoid CA expiry, to mitigate key version compromises, and as part of your organization's security practices. To plan how often you rotate specific GKE control plane authority resources, consider the following:

  * By default, GKE certificates signed by the root CAs in Certificate Authority Service (CA Service) expire one year after the creation date.
  * Keys in Cloud Key Management Service (Cloud KMS) don't expire. Perform a manual key rotation only if your organization has requirements for key rotation. To minimize disruptions to running workloads, don't configure automatic key rotation for these keys.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Have an existing cluster that uses [self-managed CAs and service account keys](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/run-your-own-cas-keys) and runs GKE version 1.35.2-gke.1842000 or later.

  * Identify the project IDs of the following Google Cloud projects:

    * **Key project** : the project that contains your Cloud KMS and CA Service resources.
    * **Cluster project** : the project that contains your GKE cluster.
  * To do the validation tasks in this document, verify that the following Data Access audit logs are enabled:

    * Cloud Key Management Service (KMS) API: `DATA_READ`
    * Certificate Authority Service: `ADMIN_READ`

To enable these log types, see [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).




### Required roles and permissions

To get the permissions that you need to rotate your customer-managed CAs and keys, ask your administrator to grant you the following IAM roles: 

  * Manage keys or key versions: [Cloud KMS Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.admin) (`roles/cloudkms.admin`) on your key project 
  * Manage root CAs: [CA Service Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/privateca#privateca.admin) (`roles/privateca.admin`) on your key project 
  * Configure clusters to use new credentials: [Kubernetes Engine Cluster Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterAdmin) (`roles/container.clusterAdmin`) on your cluster project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Limitations

The asymmetric Cloud KMS keys that you use for service account signing and verification don't support automatic key rotation.

## Rotate the service account signing and verification keys

When you setup GKE control plane authority, you add a service account signing key and service account verification keys to your cluster. GKE uses these keys to sign and validate bearer tokens for Kubernetes ServiceAccounts. During a rotation, you add your new key to the list of service account verification keys, wait for changes to propagate, and then replace the service account signing key with the new key.

To rotate the service account keys, follow these steps:

  1. Get the full resource name of the original key version of the service account signing key:
         
         gcloud container clusters describe CLUSTER_NAME \
             --project=CLUSTER_PROJECT_ID \
             --location=CONTROL_PLANE_LOCATION \
             --format="value(userManagedKeysConfig.serviceAccountSigningKeys)"
         

Replace the following:

     * `CLUSTER_NAME`: the name of your cluster.
     * `CONTROL_PLANE_LOCATION`: the location of the cluster.
     * `CLUSTER_PROJECT_ID`: the project ID of the cluster project.

The output is similar to the following:
    
    projects/KEY_PROJECT_ID/locations/CONTROL_PLANE_LOCATION/keyRings/KEYRING_NAME/cryptoKeys/SIGNING_KEY_NAME/cryptoKeyVersions/ORIGINAL_SIGNING_KEY_VERSION
    

In this output, `SIGNING_KEY_NAME` is the name of the key and `ORIGINAL_SIGNING_KEY_VERSION` is the number of the original signing key version.

  2. Create a new key version for the service account signing key:
         
         gcloud kms keys versions create \
             --key=SIGNING_KEY_NAME \
             --keyring=KEYRING_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID
         

Replace the following:

     * `SIGNING_KEY_NAME`: the name of the service account signing key.
     * `KEYRING_NAME`: the name of the key ring that holds the key.
     * `CONTROL_PLANE_LOCATION`: the Google Cloud location of the key ring.
     * `KEY_PROJECT_ID`: the project ID of your _key project_.
  3. Get the full resource name of the new key version:
         
         gcloud kms keys versions list \
             --key=SIGNING_KEY_NAME \
             --keyring=KEYRING_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID \
             --filter="STATE=ENABLED" --sort-by=~ \
             --format="value(name)" | sed 1q
         

The output is similar to the following:
         
         projects/KEY_PROJECT_ID/locations/CONTROL_PLANE_LOCATION/keyRings/KEYRING_NAME/cryptoKeys/SIGNING_KEY_NAME/cryptoKeyVersions/NEW_SIGNING_KEY_VERSION
         

In this output, `SIGNING_KEY_NAME` is the name of the key and `NEW_SIGNING_KEY_VERSION` is the number of the new signing key version.

  4. Add the new key version to the set of service account verification keys for the cluster:
         
         gcloud container clusters update CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=CLUSTER_PROJECT_ID \
             --service-account-verification-keys=ORIGINAL_KEY_VERSION_PATH,NEW_KEY_VERSION_PATH
         

Replace the following:

     * `ORIGINAL_KEY_VERSION_PATH`: the full resource name of the original signing key version from the output of the first step in this section. For example, `projects/example-key-project/locations/us-central1/keyRings/example-keyring/cryptokeys/example-signing-key/cryptoKeyVersions/1`.
     * `NEW_KEY_VERSION_PATH`: the full resource name of the new signing key version from the output of the previous step. For example, `projects/example-key-project/locations/us-central1/keyRings/example-keyring/cryptokeys/example-signing-key/cryptoKeyVersions/2`.

After the cluster update operation completes, it might take up to 10 minutes for the new key version path to propagate to the Kubernetes API server and every GKE API endpoint.

  5. To confirm that the new key version path is fully propagated, do the following:

     1. Get the public component of the cluster signing keys from the GKE API as a JSON Web Key Set (JWKS):
            
            curl https://container.googleapis.com/v1/projects/CLUSTER_PROJECT_ID/locations/CONTROL_PLANE_LOCATION/clusters/CLUSTER_NAME/jwks
            

The output is similar to the following:
            
            {
              "keys": [
                {
                  "kty": "RSA",
                  "alg": "RS256",
                  "use": "sig",
                  "kid": "KEY1_ID",
                  "n": "KEY1_MODULUS",
                  "e": "KEY1_EXPONENT"
                },
                {
                  "kty": "RSA",
                  "alg": "RS256",
                  "use": "sig",
                  "kid": "KEY2_ID",
                  "n": "KEY2_MODULUS",
                  "e": "KEY2_EXPONENT"
                }
              ]
            }
            

This output must have two key entries, which indicates that both of the key versions are available in the GKE API. If you only see one key entry, wait for 10 minutes and retry the command.

     2. Connect to the cluster so that you can run `kubectl` commands:
            
            gcloud container clusters get-credentials CLUSTER_NAME \
                --location=CONTROL_PLANE_LOCATION
            

     3. Get the public component of the cluster signing keys from the Kubernetes API server as a JWKS:
            
            kubectl get --raw /openid/v1/jwks | jq
            

The output is similar to the following:
            
            {
              "keys": [
                {
                  "kty": "RSA",
                  "alg": "RS256",
                  "use": "sig",
                  "kid": "KEY1_ID",
                  "n": "KEY1_MODULUS",
                  "e": "KEY1_EXPONENT"
                },
                {
                  "kty": "RSA",
                  "alg": "RS256",
                  "use": "sig",
                  "kid": "KEY2_ID",
                  "n": "KEY2_MODULUS",
                  "e": "KEY2_EXPONENT"
                }
              ]
            }
            

This output must have two key entries, which indicates that both of the key versions are available in the Kubernetes API server. If you only see one key entry, wait for 10 minutes and retry the command.

  6. Update the cluster to use the new key version as the service account signing key:
         
         gcloud container clusters update CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=CLUSTER_PROJECT_ID \
             --service-account-signing-keys=NEW_KEY_VERSION_PATH
         

  7. Verify that new service account tokens use the new key version:

     1. Create a ServiceAccount:
            
            kubectl create serviceaccount test-sa-1
            

     2. Create a token for the ServiceAccount:
            
            kubectl create token test-sa-1
            

     3. Extract a recently signed digest from Logging:
            
            export SIGNED_DIGEST=$(gcloud logging read \
                'resource.type="gke_cluster"
                AND resource.labels.cluster_name="CLUSTER_NAME"
                AND protoPayload.methodName="google.cloud.gkeauth.v1.Auth.SignServiceAccountJWT"
                AND protoPayload.metadata.subject="system:serviceaccount:default:test-sa-1"' \
                --freshness=1h \
                --bucket=_Required \
                --location=global \
                --view=_AllLogs \
                --order=DESC \
                --limit=1 \
                --format="value(protoPayload.metadata.toBeSignedDigest)")
            

     4. Validate that the new signing key version is in use:
            
            gcloud logging read \
                'resource.type="cloudkms_cryptokeyversion" 
                AND protoPayload.methodName="AsymmetricSign"
                AND protoPayload.request.digest.sha256="'${SIGNED_DIGEST}'"' \
                --freshness=1h \
                --bucket=_Default \
                --location=global \
                --view=_AllLogs \
                --order=DESC \
                --limit=1 \
                --format="value(protoPayload.resourceName)"
            

The output is the resource path of the new signing key version.

  8. Wait for every token in the cluster that uses the original service account signing key version to expire. By default, the token lifetime is one hour, with a configurable maximum of 24 hours. To check the configured token lifetime in your cluster, run the following command:
         
         kubectl get pods -A -o json | jq -r '.items[]?.spec?.volumes[]?.projected?.sources[]?.serviceAccountToken?.expirationSeconds | select(. != null)' | sort -nr | head -n 1
         

**Note:** if you store ServiceAccount tokens in Secrets, recreate the Secrets so that Kubernetes generates new tokens that are signed by the new key version.
  9. Wait for the configured token lifetime from the output of the previous step to pass. After this period of time passes, all of the bound tokens in your cluster use the new service account signing key version.

  10. Remove the original key version from the list of verification keys for the cluster:
         
         gcloud container clusters update CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=CLUSTER_PROJECT_ID \
             --service-account-verification-keys=NEW_KEY_VERSION_PATH
         

  11. Optional: Disable the original key version. After you verify that the original key version isn't being used and that the cluster is healthy, destroy the key version.

Unless you're rotating the keys in response to a critical event, we recommend that you wait for a few days before you destroy the original key version. For more information, see [Destroy and restore key versions](https://docs.cloud.google.com/kms/docs/destroy-restore).




After you complete these steps, every new and existing service account token in your cluster is signed by the new key version. The API server rejects any requests that use a bearer token with the original key version, because the original key version doesn't exist in the cluster configuration.

## Rotate the GKE control plane authority CAs

The following sections show you how to rotate the root CAs that the cluster uses for GKE control plane authority.

### Create new key versions for the CAs

  1. Create a new key version for the cluster root CA key:
         
         gcloud kms keys versions create \
             --key=CLUSTER_CA_KEY_NAME \
             --keyring=KEYRING_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID
         

Replace the following:

     * `CLUSTER_CA_KEY_NAME`: the name of the cluster root CA key for the cluster.
     * `KEYRING_NAME`: the name of the key ring that holds the key.
     * `CONTROL_PLANE_LOCATION`: the Google Cloud location of the key ring. This is the same as your cluster location.
     * `KEY_PROJECT_ID`: the project ID of your _key project_.
  2. Create a new key version for the aggregation root CA key:
         
         gcloud kms keys versions create \
             --key=AGGREGATION_CA_KEY_NAME \
             --keyring=KEYRING_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID
         

Replace `AGGREGATION_CA_KEY_NAME` with the name of the aggregation root CA key for the cluster.

  3. Create a new key version for the etcd API root CA key:
         
         gcloud kms keys versions create \
             --key=ETCD_API_CA_KEY_NAME \
             --keyring=KEYRING_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID
         

Replace `ETCD_API_CA_KEY_NAME` with the name of the etcd API root CA key for the cluster.

  4. Create a new key version for the etcd peer root CA key:
         
         gcloud kms keys versions create \
             --key=ETCD_PEER_CA_KEY_NAME \
             --keyring=KEYRING_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID
         

Replace `ETCD_PEER_CA_KEY_NAME` with the name of the etcd peer root CA key for the cluster.




### Create new root CAs

  1. Get the full resource name of the new cluster root CA key version:
         
         gcloud kms keys versions list \
             --key=CLUSTER_CA_KEY_NAME \
             --keyring=KEYRING_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID \
             --filter="STATE=ENABLED" --sort-by=~ \
             --format="value(name)" | sed 1q
         

The output is similar to the following:
         
         projects/KEY_PROJECT_ID/locations/CONTROL_PLANE_LOCATION/keyRings/KEYRING_NAME/cryptoKeys/CLUSTER_CA_KEY_NAME/cryptoKeyVersions/VERSION
         

In this output, `VERSION` is the number of the new key version.

  2. Create a new cluster root CA in the cluster CA pool:
         
         gcloud privateca roots create CLUSTER_ROOT_CA_NAME \
             --pool=CLUSTER_CA_POOL_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --kms-key-version=CLUSTER_CA_KEY_PATH \
             --subject="CN=cluster-ca, O=ORGANIZATION" \
             --project=KEY_PROJECT_ID
         

Replace the following:

     * `CLUSTER_ROOT_CA_NAME`: a name for your new root CA.
     * `CLUSTER_CA_POOL_NAME`: the name of the cluster CA pool.
     * `CLUSTER_CA_KEY_PATH`: the full resource name of the new key version from the output of the preceding step.
     * `ORGANIZATION`: your organization name.
  3. Get the full resource name of the new aggregation root CA key version:
         
         gcloud kms keys versions list \
             --key=AGGREGATION_CA_KEY_NAME \
             --keyring=KEYRING_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID \
             --filter="STATE=ENABLED" --sort-by=~ \
             --format="value(name)" | sed 1q
         

The output is similar to the following:
         
         projects/KEY_PROJECT_ID/locations/CONTROL_PLANE_LOCATION/keyRings/KEYRING_NAME/cryptoKeys/AGGREGATION_CA_KEY_NAME/cryptoKeyVersions/VERSION
         

  4. Create a new aggregation root CA in the aggregation CA pool:
         
         gcloud privateca roots create AGGREGATION_ROOT_CA_NAME \
             --pool=AGGREGATION_CA_POOL_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --kms-key-version=AGGREGATION_CA_KEY_PATH \
             --subject="CN=aggregation-ca, O=ORGANIZATION" \
             --project=KEY_PROJECT_ID
         

Replace the following:

     * `AGGREGATION_ROOT_CA_NAME`: a name for your new aggregation root CA.
     * `AGGREGATION_CA_POOL_NAME`: the name of the aggregation CA pool.
     * `AGGREGATION_CA_KEY_PATH`: the full resource name of the new key version from the output of the preceding step.
  5. Get the full resource name of the new etcd API root CA key version:
         
         gcloud kms keys versions list \
             --key=ETCD_API_CA_KEY_NAME \
             --keyring=KEYRING_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID \
             --filter="STATE=ENABLED" --sort-by=~ \
             --format="value(name)" | sed 1q
         

The output is similar to the following:
         
         projects/KEY_PROJECT_ID/locations/CONTROL_PLANE_LOCATION/keyRings/KEYRING_NAME/cryptoKeys/ETCD_API_CA_KEY_NAME/cryptoKeyVersions/VERSION
         

  6. Create a new etcd API root CA in the etcd API CA pool:
         
         gcloud privateca roots create ETCD_API_ROOT_CA_NAME \
             --pool=ETCD_API_CA_POOL_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --kms-key-version=ETCD_API_CA_KEY_PATH \
             --subject="CN=etcd-api-ca, O=ORGANIZATION" \
             --project=KEY_PROJECT_ID
         

Replace the following:

     * `ETCD_API_ROOT_CA_NAME`: a name for your new etcd API root CA.
     * `ETCD_API_CA_POOL_NAME`: the name of the etcd API CA pool.
     * `ETCD_API_CA_KEY_PATH`: the full resource name of the new key version from the output of the preceding step.
  7. Get the full resource name of the new etcd peer root CA key version:
         
         gcloud kms keys versions list \
             --key=ETCD_PEER_CA_KEY_NAME \
             --keyring=KEYRING_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID \
             --filter="STATE=ENABLED" --sort-by=~ \
             --format="value(name)" | sed 1q
         

The output is similar to the following:
         
         projects/KEY_PROJECT_ID/locations/CONTROL_PLANE_LOCATION/keyRings/KEYRING_NAME/cryptoKeys/ETCD_PEER_CA_KEY_NAME/cryptoKeyVersions/VERSION
         

  8. Create a new etcd peer root CA in the etcd peer CA pool:
         
         gcloud privateca roots create ETCD_PEER_ROOT_CA_NAME \
             --pool=ETCD_PEER_CA_POOL_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --kms-key-version=ETCD_PEER_CA_KEY_PATH \
             --subject="CN=etcd-peer-ca, O=ORGANIZATION" \
             --project=KEY_PROJECT_ID
         

Replace the following:

     * `ETCD_PEER_ROOT_CA_NAME`: a name for your new etcd peer root CA.
     * `ETCD_PEER_CA_POOL_NAME`: the name of the etcd peer CA pool.
     * `ETCD_PEER_CA_KEY_PATH`: the full resource name of the new key version from the output of the preceding step.
  9. Before you continue, propagate the root CA changes to the cluster trust bundle by following the instructions in the Restart the control plane and nodes section.




### Replace the original root CAs with the new root CAs

After you restart the control plane and nodes, follow these steps:

  1. Enable the new cluster root CA:
         
         gcloud privateca roots enable CLUSTER_ROOT_CA_NAME \
             --pool=CLUSTER_CA_POOL_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID
         

  2. Enable the new aggregation root CA:
         
         gcloud privateca roots enable AGGREGATION_ROOT_CA_NAME \
             --pool=AGGREGATION_CA_POOL_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID
         

  3. Enable the new etcd API root CA:
         
         gcloud privateca roots enable ETCD_API_ROOT_CA_NAME \
             --pool=ETCD_API_CA_POOL_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID
         

  4. Enable the new etcd peer root CA:
         
         gcloud privateca roots enable ETCD_PEER_ROOT_CA_NAME \
             --pool=ETCD_PEER_CA_POOL_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID
         

  5. Disable the original cluster root CA:
         
         gcloud privateca roots disable ORIGINAL_CLUSTER_ROOT_CA \
             --pool=CLUSTER_CA_POOL_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID
         

Replace `ORIGINAL_CLUSTER_ROOT_CA` with the name of the original cluster root CA that you're rotating.

  6. Disable the original aggregation root CA:
         
         gcloud privateca roots disable ORIGINAL_AGGREGATION_ROOT_CA \
             --pool=AGGREGATION_CA_POOL_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID
         

Replace `ORIGINAL_AGGREGATION_ROOT_CA` with the name of the original aggregation root CA that you're rotating.

  7. Disable the original etcd API root CA:
         
         gcloud privateca roots disable ORIGINAL_ETCD_API_ROOT_CA \
             --pool=ETCD_API_CA_POOL_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID
         

Replace `ORIGINAL_ETCD_API_ROOT_CA` with the name of the original etcd API root CA that you're rotating.

  8. Disable the original etcd peer root CA:
         
         gcloud privateca roots disable ORIGINAL_ETCD_PEER_ROOT_CA \
             --pool=ETCD_PEER_CA_POOL_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID
         

Replace `ORIGINAL_ETCD_PEER_ROOT_CA` with the name of the original etcd peer root CA that you're rotating.

  9. At this point, the new root CAs issue all new certificates in the cluster. To issue new certificates for the `kubelet` on each node, Restart the control plane and nodes. This step is required because `kubelet` certificates have long lifetimes.




After multiple days where the cluster remains in a healthy state, you can delete the original root CAs, as described in the next section.

### Delete the original root CAs

This section shows you how to delete your original root CAs. Before you follow these steps, verify the following:

  * The cluster remained in a healthy state for multiple days after you replaced the original root CAs with the new root CAs.
  * You replaced all of the certificates issued by the original root CAs with new certificates.



To delete the original root CAs, use the [`gcloud privateca roots delete`](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/roots/delete) command, as described in the following steps. In these commands, the `--ignore-active-certificates` flag deletes the CA after a grace period, even if the CA has un-revoked or un-expired certificates.

  1. Delete the original cluster root CA:
         
         gcloud privateca roots delete ORIGINAL_CLUSTER_ROOT_CA \
             --pool=CLUSTER_CA_POOL_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID \
               --ignore-active-certificates
         

Replace `ORIGINAL_CLUSTER_ROOT_CA` with the name of the original cluster root CA that you're rotating.

  2. Delete the original aggregation root CA:
         
         gcloud privateca roots delete ORIGINAL_AGGREGATION_ROOT_CA \
             --pool=AGGREGATION_CA_POOL_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID \
               --ignore-active-certificates
         

Replace `ORIGINAL_AGGREGATION_ROOT_CA` with the name of the original aggregation root CA that you're rotating.

  3. Delete the original etcd API root CA:
         
         gcloud privateca roots delete ORIGINAL_ETCD_API_ROOT_CA \
             --pool=ETCD_API_CA_POOL_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID \
               --ignore-active-certificates
         

Replace `ORIGINAL_ETCD_API_ROOT_CA` with the name of the original etcd API root CA that you're rotating.

  4. Delete the original etcd peer root CA:
         
         gcloud privateca roots delete ORIGINAL_ETCD_PEER_ROOT_CA \
             --pool=ETCD_PEER_CA_POOL_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --project=KEY_PROJECT_ID \
               --ignore-active-certificates
         

Replace `ORIGINAL_ETCD_PEER_ROOT_CA` with the name of the original etcd peer root CA that you're rotating.

  5. Optional: Propagate the changes to root CAs to the cluster trust bundle. For instructions, see the Restart the control plane and nodes section. If you skip this step, the original root CAs are removed during the next control plane and node version upgrade.


**Success:** You rotated all of the root CAs in your control plane. All of the CA certificates in your cluster are issued by your new root CAs. The original root CAs no longer exist in the cluster trust bundle.

### Restart the control plane and nodes

When you make changes to the root CA configuration of your cluster, such as enabling root CAs, disabling root CAs, or revoking certificates, you must propagate those changes to the cluster's trust bundle. To propagate changes to trust bundle for the cluster, you restart the control plane and (in some scenarios) the nodes.

  1. Upgrade the cluster control plane to the same version that it already uses.

**Caution:** In zonal clusters, the control plane becomes unavailable until the upgrade operation completes. In Autopilot clusters and regional Standard clusters, the control plane remains available.
     1. Find the GKE version that control plane already uses:
            
            gcloud container clusters describe CLUSTER_NAME \
                --location=CONTROL_PLANE_LOCATION \
                --project=CLUSTER_PROJECT_ID \
                --format="value(currentMasterVersion)"
            

Replace the following:

        * `CLUSTER_NAME`: the name of your GKE cluster.
        * `CLUSTER_VERSION`: the GKE version that the cluster already runs.
        * `CLUSTER_PROJECT_ID`: the project ID of your _cluster project_.
     2. Upgrade the control plane:
            
            gcloud container clusters upgrade CLUSTER_NAME \
                --master \
                --location=CONTROL_PLANE_LOCATION \
                --cluster-version=CLUSTER_VERSION \
                --project=CLUSTER_PROJECT_ID
            

  2. For cluster root CA rotation only, trigger node recreation by upgrading each of your node pools to the same version that they already use.

**Caution:** GKE immediately begins recreating the nodes for this change using the node upgrade strategy, regardless of active maintenance policies. GKE depends on [resource availability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota) for the change. Disabling node auto-upgrades [doesn't prevent this change](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable-only-versions). Prepare the workloads that run on your nodes for disruption before you initiate this change.
     1. Find the GKE version that the node pool uses:
            
            gcloud container node-pools describe NODE_POOL_NAME \
                --cluster=CLUSTER_NAME \
                --location=CONTROL_PLANE_LOCATION \
                --project=CLUSTER_PROJECT_ID \
                --format="value(version)"
            

Replace `NODE_POOL_NAME` with the name of the node pool to upgrade.

     2. Upgrade the node pool:
            
            gcloud container clusters upgrade CLUSTER_NAME \
                --node-pool=NODE_POOL_NAME \
                --location=CONTROL_PLANE_LOCATION \
                --cluster-version=CLUSTER_VERSION \
                --project=CLUSTER_PROJECT_ID
            

  3. After your control plane and nodes finish upgrading, update any Kubernetes API clients like the kubectl CLI to use the updated trust bundle. If you manually generate certificates by using Kubernetes CertificateSigningRequests, re-issue all of those certificates and provide the new certificates to API clients.




If you performed the steps in this section during a CA rotation, proceed to the next phase of the rotation, which is one of the following sections in this document:

  * Replace the original root CAs with the new root CAs.
  * Delete the original root CAs.



## What's next

  * [Rotate etcd and control plane boot disk encryption keys](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rotate-etcd-kcp-encryption-keys)
  * [Verify identity issuance and usage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/verify-identity-issuance-usage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

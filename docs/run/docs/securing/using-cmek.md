---
url: https://docs.cloud.google.com/run/docs/securing/using-cmek/
title: Using customer managed encryption keys \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:13.180018+00:00
---

# Using customer managed encryption keys  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/securing/using-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Using customer managed encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

By default, Cloud Run encrypts customer content at rest. Cloud Run handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Cloud Run. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Cloud Run resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

To learn about protecting your data with CMEK on functions created using [`gcloud functions`](https://docs.cloud.google.com/sdk/gcloud/reference/functions) commands or the [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/reference/rest), see [Protect your data with CMEK](https://docs.cloud.google.com/functions/docs/securing/cmek).

You should be aware of the following:

  * File metadata, such as the path, is not encrypted.
  * Metadata of the Cloud Run service or worker pool, such as name or environment variables, is not encrypted using the provided key but with a Google-owned and Google-managed encryption key.
  * At runtime, the memory and file content are not encrypted.
  * If a CMEK is disabled, new instances of existing Cloud Run revisions using the key won't start.
  * If a CMEK is disabled, deploying a new Cloud Run revision will fail unless a new valid key is used.



## CMEK with Cloud KMS Autokey

You can either create CMEKs manually to protect your Cloud Run resources or use Cloud KMS Autokey. With Autokey, key rings and keys are generated on demand to support resource creation in Cloud Run. Service agents that use the keys for encrypt and decrypt operations are created if they don't already exist and are granted the required Identity and Access Management (IAM) roles. For more information, see [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

To set up CMEK manually, follow the instructions to configure CMEK for a service or a worker pool.

To set up CMEK using Autokey, follow the instructions to configure Autokeys for a service or a worker pool.

Autokey is not available for functions created using [`gcloud functions`](https://docs.cloud.google.com/sdk/gcloud/reference/functions) commands or the [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/reference/rest).

**Note:** This feature protects container images after they're deployed to Cloud Run. The contents of the container images prior to deployment are protected separately, such as with Artifact Registry. If you use a container image within a [CMEK protected Artifact Registry repository](https://docs.cloud.google.com/artifact-registry/docs/cmek), you don't need to use the same key for Cloud Run deployment.

## Cloud KMS quotas and Cloud Run

You can set your CMEK to one of the available protection levels to indicate how cryptographic operations are performed. When you use CMEK in Cloud Run, your projects can consume Cloud KMS cryptographic requests quotas. For example, CMEK-encrypted repositories can consume these quotas for each upload or download.

Encryption and decryption operations using CMEK keys affect Cloud KMS quotas in these ways:

  * For software CMEK keys generated in Cloud KMS, no Cloud KMS quota is consumed.
  * For hardware CMEK keys—sometimes called Cloud HSM keys—encryption and decryption operations count against [Cloud HSM quotas](https://docs.cloud.google.com/kms/quotas#hsm) in the project that contains the key.
  * For external CMEK keys—sometimes called Cloud EKM keys—encryption and decryption operations count against [Cloud EKM quotas](https://docs.cloud.google.com/kms/quotas#ekm) in the project that contains the key.



For more information, see [Cloud KMS quotas](https://docs.cloud.google.com/kms/quotas).

## Autoscaling behavior affected by CMEK

The [expected autoscaling](https://docs.cloud.google.com/run/docs/about-instance-autoscaling) for your Cloud Run service can be impacted when you use customer managed encryption keys. For example, latency for starting new instances can increase due to delays in contacting external key management systems during key operations.

The following table shows the possible changes in behavior due to use of CMEK:

CMEK-related operation | Autoscaling behavior  
---|---  
Key disabled/destroyed/revoked | New instances won't start.  
External key manager cannot be contacted | If the key request can be retried, no instances are shutdown during the retries and no new instances will start. Scale-out can appear slower than expected.  
If the key request cannot be retried, no new instances are started, and running instances are shut down after a waiting period.  
KMS quota exceeded | If this quota is exceeded, `RESOURCE_EXHAUSTED` errors are logged, and new instances won't start. You can [request additional quota](https://console.cloud.google.com/iam-admin/quotas?service=cloudkms.googleapis.com) to fix this.  
  
## Before you begin

  * [Enable the Cloud Run Admin API](https://console.cloud.google.com/apis/library/run.googleapis.com)



## Allow Cloud Run to access a key

**Important:** The key must be a symmetric key created for the same region where you will deploy the Cloud Run service or worker pool, for example, `europe-west1`. Don't choose a multi-region key.

To use CMEK for Cloud Run, perform the following steps:

  1. Configure Artifact Registry [to use CMEK](https://docs.cloud.google.com/artifact-registry/docs/cmek).

  2. Using the Artifact Registry [Docker Quickstart](https://docs.cloud.google.com/artifact-registry/docs/docker/store-docker-container-images) as a reference create a Docker repository push an image to it.

  3. Use an existing Cloud KMS _symmetric_ key or [create a new symmetric key](https://docs.cloud.google.com/kms/docs/creating-keys#create_a_key).

  4. To allow Cloud Run access to the key, grant the Cloud Run service agent the _Cloud KMS CryptoKey Encrypter/Decrypter_ role:

### Console

     1. Go to the [Cryptographic keys page](https://console.cloud.google.com/security/kms/keyrings)

     2. Click the key ring for your key to open its key list page.

     3. Select the key and in the right-side Permissions tab, click **Add principal**.

     4. In the **New principals** field, copy the Cloud Run [service agent](https://docs.cloud.google.com/iam/docs/service-agents) email. It has the following suffix:

**service- PROJECT_NUMBER@serverless-robot-prod.iam.gserviceaccount.com**.

     5. In the **Select a role** field, select _Cloud KMS CryptoKey Encrypter/Decrypter_.

     6. Click **Save**.

###  gcloud 

Use the following [`gcloud kms`](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/add-iam-policy-binding) command:
    
    gcloud kms keys add-iam-policy-binding KEY_NAME \
    --keyring=KEYRING \
    --location=LOCATION \
    --member serviceAccount:service-PROJECT_NUMBER@serverless-robot-prod.iam.gserviceaccount.com \
    --role='roles/cloudkms.cryptoKeyEncrypterDecrypter'

Replace the following:

     * KEY_NAME: the name of your key.
     * KEYRING: the name of your key ring.
     * LOCATION: the name of your region.
     * PROJECT_NUMBER: the project number where you intend to deploy the Cloud Run service or worker pool.

You need permission to administer Cloud KMS resources in the Google Cloud project to grant the IAM role `roles/cloudkms.cryptoKeyEncrypterDecrypter`. Only IAM members with Owner (`roles/owner`) or Cloud KMS Admin (`roles/cloudkms.admin`) roles can grant or revoke access to Cloud KMS resources.




## Configure CMEK for a service

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Services** from the Cloud Run navigation menu:

     1. If you are configuring a new service, click **Deploy container** and fill out the initial service settings page. Then click **Containers, Networking, Security** to expand the service configuration page.

     2. If you are configuring an existing service, click the service.

  3. Click the **Security** tab.

  4. Under **Encryption** , select **Cloud KMS key**.

  5. For **Key management type** , select **Cloud KMS**.

  6. From the **Select a Cloud KMS key** menu, choose one of the following options:

     * Select **Switch projects** if you need to use a key from a different project. You can reference a key from another project if your project's service account can access the key for encryption and decryption operations.

     * Select **Enter key manually** to enter the secret from a project, using the following format: `projects/PROJECT_NAME/locations/LOCATION/keyRings/KEYRING_NAME/cryptoKeys/KEY_NAME`.

  7. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




To copy and paste the resource name from another project that you have access to:

  1. In the Google Cloud console, go to the **Cryptographic keys** page:

[Go to Cryptographic keys](https://console.cloud.google.com/security/kms/keyrings)

  2. Click the key ring.

  3. Select the chosen key ring name and click **Actions**.

  4. Select **Copy resource name** from the menu and paste it in the **Key resource name** field from the previous step.

  5. From the **Key revocation action** menu, choose one of the following options:

     * **Prevent new container instance** : no new instances start after CMEK key revocation.

     * **Shutdown as soon as possible** : no new instances start and existing instances shut down after CMEK key revocation.

     * **Custom shutdown delay** : specify the number of hours before the service shuts down.

  6. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

To set a key on a service, use either of the following commands:
    
    
    gcloud run deploy SERVICE \
    --image IMAGE_URL \
    --key KEY \
    --post-key-revocation-action-type KEY_REVOCATION_ACTION
    --encryption-key-shutdown-hours SHUTDOWN_HOURS
    
    
    gcloud run services update SERVICE --key KEY
    --post-key-revocation-action-type KEY_REVOCATION_ACTION
    --encryption-key-shutdown-hours SHUTDOWN_HOURS

Replace the following:

  * SERVICE: the name of your service.
  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
  * KEY: the fully qualified key name in the following format: `projects/PROJECT_NAME/locations/LOCATION/keyRings/KEYRING_NAME/cryptoKeys/KEY_NAME`.
  * KEY_REVOCATION_ACTION: `shut-down` or `prevent-new`, depending on your [key revocation preferences](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--post-key-revocation-action-type).
  * SHUTDOWN_HOURS: the number of hours to delay before the service shuts down after revocation.



### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update the following CMEK annotations to the values that you want:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/encryption-key: projects/PROJECT_NAME/locations/LOCATION/keyRings/KEYRING_NAME/cryptoKeys/KEY_NAME
                 run.googleapis.com/post-key-revocation-action-type: KEY_REVOCATION_ACTION
                 run.googleapis.com/encryption-key-shutdown-hours: SHUTDOWN_HOURS
               name: REVISION

Replace the following:

     * SERVICE: the name of your Cloud Run service.
     * PROJECT_NAME: the name of the project the key was created in.
     * LOCATION: the location the key was created in. Must match the Cloud Run service location.
     * KEYRING_NAME: the name of the key ring.
     * KEY_NAME: the name of the key.
     * KEY_REVOCATION_ACTION: `shut-down` or `prevent-new`, depending on your [key revocation preferences](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--post-key-revocation-action-type).
     * SHUTDOWN_HOURS: the number of hours to delay before the service shuts down after revocation.
     * `REVISION`: a new revision name or delete it (if present). If you supply a new revision name, it **must** meet the following criteria:
       * Starts with `SERVICE-`
       * Contains only lowercase letters, numbers and `-`
       * Does not end with a `-`
       * Does not exceed 63 characters
  3. Replace the service with its new configuration using the following command:
         
         gcloud run services replace service.yaml




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration.
    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "SERVICE"
      location = "europe-west1"
    
      template {
        containers {
          image = "us-docker.pkg.dev/cloudrun/container/hello"
        }
        encryption_key = "projects/PROJECT_NAME/locations/LOCATION/keyRings/KEYRING_NAME/cryptoKeys/KEY_NAME"
      }
    }
    

Replace the following:

  * SERVICE: the name of your Cloud Run service.
  * PROJECT_NAME: the name of the project the key was created in.
  * LOCATION: the location the key was created in. Must match the Cloud Run service location.
  * KEYRING_NAME: the name of the key ring.
  * KEY_NAME: the name of the key.



### Use Autokey for services

If you haven't already done so, [Enable Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/enable-autokey).

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Services** from the Cloud Run navigation menu:

     1. If you are configuring a new service, click **Deploy container** and fill out the initial service settings page. Then click **Containers, Networking, Security** to expand the service configuration page.

     2. If you are configuring an existing service, click the service.

  3. Click the **Security** tab.

  4. Under **Encryption** , select **Cloud KMS with Autokey**.

  5. Click **Request a key**. The key's details are shown after resource creation.

  6. From the **Key revocation action** menu, choose one of the following options:

     * **Prevent new container instance** : no new instances start after CMEK revocation.

     * **Shutdown as soon as possible** : no new instances start and existing instances shut down after CMEK revocation.

     * **Custom shutdown delay** : specify the number of hours before the service shuts down.

  7. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




### View security settings for services

To view the security settings for your Cloud Run service:

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click your service to open the **Service details** page.

  3. Click the **Security** tab to view the security settings.




###  gcloud 

  1. Run the following command to view the security settings:
         
         gcloud run services describe SERVICE

  2. Locate the security setting in the returned configuration.




### Additional configuration for source-based deployments

[Cloud Run source deployments](https://docs.cloud.google.com/run/docs/deploying-source-code) and [functions](https://docs.cloud.google.com/run/docs/deploy-functions) involve an additional build step. To ensure the CMEK compliance of this step, you must do the following:

  1. Create your own CMEK-encrypted Cloud Storage bucket. For details, refer to [the CMEK documentation](https://docs.cloud.google.com/artifact-registry/docs/cmek) for Cloud Storage.

  2. Upload your source code to the CMEK-encrypted storage bucket as a zipped archive file.

  3. Create your own CMEK-encrypted Artifact Registry repository. For details, refer to [the CMEK documentation](https://docs.cloud.google.com/artifact-registry/docs/cmek) for Artifact Registry. This repository stores artifacts produced by the build process.

  4. Deploy the function, passing the build resources by using the `--source` and `--image` flags.



    
    
        gcloud run deploy FUNCTION \
            --key KEY \
            --source CUSTOM_BUCKET_WITH_SOURCE_CODE \
            --image CUSTOM_AR_REPOSITORY \
            --function FUNCTION_ENTRYPOINT \
            --base-image BASE_IMAGE \
            --region REGION
    

Replace the following:

  * FUNCTION: the name of the function you are deploying. You can omit this parameter entirely, but you will be prompted for the name if you omit it.

  * KEY: the fully qualified key name in the following format: `projects/PROJECT_NAME/locations/LOCATION/keyRings/KEYRING_NAME/cryptoKeys/KEY_NAME`.

  * CUSTOM_BUCKET_WITH_SOURCE_CODE: the URI of a Cloud Storage location where the source code is stored. Use the following format: `gs://BUCKET_NAME/PATH_TO_SOURCE`.

  * CUSTOM_AR_REPOSITORY: the URI of an Artifact Registry repository in the format `REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME`.

  * FUNCTION_ENTRYPOINT: the entry point to your function in your source code. This is the code Cloud Run executes when your function runs. The value of this flag must be a function name or fully-qualified class name that exists in your source code.

  * BASE_IMAGE: the base image environment for your function. For more details about base images and the packages included in each image, see [Runtimes base images](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images).

  * REGION: the Google Cloud [region](https://docs.cloud.google.com/run/docs/locations) where you want to deploy your function. For example, `europe-west1`.




Additionally, if you use [Eventarc](https://docs.cloud.google.com/eventarc/docs/reference/audit-logs) for triggering your functions, familiarize yourself with the [CMEK configuration for Eventarc](https://docs.cloud.google.com/eventarc/docs/use-cmek). In particular, full compliance in such cases requires encrypting channels corresponding to the event types being used.

### Test CMEK revocation for services

To verify that CMEK protection is working, you can disable the key you used to enable CMEK for a service, then try to invoke your service:

  1. Run the following command to confirm the service is accessible: 
         
         curl SERVICE_URL

Replace SERVICE_URL with the service URL. You can find this in the console UI after deployment: the container URL is displayed next to the text **URL:**.

  2. [Disable the key version](https://docs.cloud.google.com/kms/docs/enable-disable#disable).

  3. Wait the number of SHUTDOWN_HOURS you specified. If you did not specify the number of shutdown hours, [re-enable your key](https://docs.cloud.google.com/kms/docs/enable-disable#enable) and edit or redeploy your service with the value set to the minimum of one hour. If you deployed source code, attempt to view the source code. The attempt should fail.

  4. After waiting the SHUTDOWN_HOURS duration you set re-run the following command and confirm the service is no longer accessible:
         
         curl SERVICE_URL
          

  5. After you have verified that the key version is disabled, [enable the key](https://docs.cloud.google.com/kms/docs/enable-disable#enable).




## Configure CMEK for a worker pool

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Worker pools** from the Cloud Run navigation menu:

     1. If you are configuring an existing worker pool, click the worker pool, then click **Edit and deploy new revision**.

     2. If you are configuring a new worker pool, click **Deploy container** and then fill out the initial worker pool page. Then click **Containers, Networking, Security** to expand the worker pools configuration page.

  3. Click the **Security** tab.

  4. Under **Encryption** , select **Cloud KMS key**.

  5. For **Key type** , select **Cloud KMS**.

  6. From the **Select a Cloud KMS key** menu, choose one of the following options:

     * Select **Switch project** if you need to use a key from a different project. You can reference a key from another project if your project's service account can access the key for encryption and decryption operations.

     * Select **Enter key manually** to enter the secret from a project, using the following format: `projects/PROJECT_NAME/locations/LOCATION/keyRings/KEYRING_NAME/cryptoKeys/KEY_NAME`.




To copy and paste the resource name from another project that you have access to:

  1. Go to the [Cryptographic keys page](https://console.cloud.google.com/security/kms/keyrings).
  2. Click the key ring.
  3. Select the chosen key ring name and click **Actions**.
  4. Select **Copy resource name** from the menu and paste it in the **Key resource name** field from the previous step.

  5. From the **Key revocation action** menu, choose one of the following options:

     * **Prevent new container instance** : no new instances start after CMEK key revocation.

     * **Shutdown as soon as possible** : no new instances start and existing instances shut down after CMEK key revocation.

     * **Custom shutdown delay** : specify the number of hours before the service shuts down.

  6. Click **Create** or **Deploy**.




###  gcloud 

To set a key on a worker pool, use either of the following commands:
    
    
    gcloud run worker-pools deploy WORKER_POOL \
    --image IMAGE_URL \
    --key KEY \
    --post-key-revocation-action-type KEY_REVOCATION_ACTION
    --encryption-key-shutdown-hours SHUTDOWN_HOURS
    
    
    gcloud run worker-pools update WORKER_POOL --key KEY
    --post-key-revocation-action-type KEY_REVOCATION_ACTION
    --encryption-key-shutdown-hours SHUTDOWN_HOURS

Replace the following:

  * WORKER_POOL: the name of your worker pool.
  * IMAGE_URL: the URL of the container image.
  * KEY: the fully qualified key name in the following format: `projects/PROJECT_NAME/locations/LOCATION/keyRings/KEYRING_NAME/cryptoKeys/KEY_NAME`.
  * KEY_REVOCATION_ACTION: `shut-down` or `prevent-new`.
  * SHUTDOWN_HOURS: the number of hours to delay before the worker pool shuts down after revocation.



### YAML

  1. If you are creating a new worker pool, skip this step. If you are updating an existing worker pool, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run worker-pools describe WORKER_POOL --format export > worker-pool.yaml

  2. Update the following CMEK annotations in the `WorkerPool` configuration:
         
         apiVersion: run.googleapis.com/v1
         kind: WorkerPool
         metadata:
           name: WORKER_POOL
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/encryption-key: projects/PROJECT_NAME/locations/LOCATION/keyRings/KEYRING_NAME/cryptoKeys/KEY_NAME
                 run.googleapis.com/post-key-revocation-action-type: KEY_REVOCATION_ACTION
                 run.googleapis.com/encryption-key-shutdown-hours: SHUTDOWN_HOURS

Replace the following:

     * WORKER_POOL: the name of your worker pool.
     * PROJECT_NAME: the name of the project the key was created in.
     * LOCATION: the location the key was created in. Must match the Cloud Run worker pool location.
     * KEYRING_NAME: the name of the key ring.
     * KEY_NAME: the name of the key.
     * KEY_REVOCATION_ACTION: `shut-down` or `prevent-new`, depending on your [key revocation preferences](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/deploy#--post-key-revocation-action-type).
     * SHUTDOWN_HOURS: the number of hours to delay before the worker pool shuts down after revocation.
  3. Replace the worker pool with its new configuration using the following command:
         
         gcloud run worker-pools replace worker-pool.yaml




### Use Autokey for worker pools

If you haven't already done so, [Enable Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/enable-autokey).

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Worker pools** from the Cloud Run navigation menu:

     1. If you are configuring an existing worker pool, click the worker pool, then click **Edit and deploy new revision**.

     2. If you are configuring a new worker pool, click **Deploy container** and then fill out the initial worker pool page. Then click **Containers, Networking, Security** to expand the worker pools configuration page.

  3. Click the **Security** tab.

  4. In the **Encryption** section:

  5. From the **Key type** menu, select **Cloud KMS with Autokey**.

  6. Click **Request a key**.

  7. Click **Create**. The key's details are shown after resource creation.

  8. From the **Key revocation action** menu, choose one of the following options:

     * **Prevent new container instance** : no new instances start after CMEK revocation.

     * **Shutdown as soon as possible** : no new instances start and existing instances shut down after CMEK revocation.

     * **Custom shutdown delay** : specify the number of hours before the service shuts down.




### View security settings for worker pools

To view the security settings for your Cloud Run worker pool:

### Console

  1. In the Google Cloud console, go to the Cloud Run worker pools page:

[Go to Cloud Run worker pools](https://console.cloud.google.com/run/workerpools)

  2. Click your worker pool to open the **Worker pools details** page.

  3. Click the **Revisions** tab.

  4. Locate the security setting in the configuration details.




###  gcloud 

  1. Use the following command:
         
         gcloud run worker-pools describe WORKER_POOL

  2. Locate the security setting in the returned configuration.




## Understand audit logs and error messages

If you are responsible for monitoring audit logs, one of your tasks might be to verify CMEK operations in your Cloud Run service or worker pool. In this case, you need to understand the related audit logs.

If you are responsible for addressing and fixing runtime errors for your Cloud Run service or worker pool, you might need to troubleshoot CMEK-related errors logged during the operation of the Cloud Run resource.

The following sections provide information needed for the preceding tasks.

### Audit logs

[KMS audit logs](https://docs.cloud.google.com/kms/docs/audit-logging) provide an audit trail for every operation performed with a key. For CMEK-enabled Cloud Run resources, Cloud Run adds Cloud Run-specific caller context that details why the customer key was accessed by the system. The following table lists the contexts you might see in the audit logs:

Reason for key access | Description  
---|---  
`Decrypting CMEK-encrypted layer during container clone start.` | Logged whenever a new instance is started.  
`Encrypting a newly created data-encryption-key w/ the customer-managed-encryption-key.` | Logged during deployment of a CMEK-enabled service or worker pool, where the data encryption key is wrapped by the CMEK.  
`Decrypting an existing encrypted data-encryption-key, under the same customer-managed-encryption-key, to be used to encrypt container contents.` | Logged when a new instance starts up, which requires decryption of the image.  
`Performing an encrypt operation on dummy data to check the customer-managed-encryption-key status and access.` | Logged whenever there is a validation check on the key, which is done periodically.  
`Performing a decrypt operation on dummy data to check the customer-managed-encryption-key status and access.` | Logged whenever there is a validation check on the key, which is done periodically.  
  
For specifics about audit log format and content, refer to the [KMS audit logging](https://docs.cloud.google.com/kms/docs/audit-logging) page.

### Error messages

Note that error messages provided by an external key manager are directly passed through to the [Cloud Run logs](https://docs.cloud.google.com/run/docs/logging) for your service.

The following table lists the CMEK-related error messages you might see, along with descriptions and possible remedies.

Message | Description  
---|---  
`User's service account does not have CMEK decrypter permission. Service account: %s` | Remedy: [Allow the Cloud Run resource to access the key](https://docs.cloud.google.com/run/docs/securing/using-cmek#allow-encrypt-decrypt)  
`User's KMS operation quota has been exceeded. CMEK key: %s` | The CMEK-enabled resource has exceeded KMS quotas. Remedy: [Request more KMS quota](https://docs.cloud.google.com/kms/quotas)  
`User's CMEK key has been disabled. CMEK key: %s` | The CMEK was revoked. Remedy: Change the resource's CMEK and redeploy it.  
`User's CMEK key has been destroyed. CMEK key: %s` | The CMEK was deleted. Remedy: Change the resource's CMEK and redeploy it.  
`User's CMEK key has been scheduled for deletion. CMEK Key: %s` | The CMEK was scheduled for deletion. Remedy: Change the resource's CMEK and redeploy it.  
  
## What's next

  * Learn [more about CMEK](https://docs.cloud.google.com/kms/docs/cmek).
  * Learn more about [Permissions and roles in Cloud KMS](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles).
  * Learn more about [Google default encryption](https://docs.cloud.google.com/docs/security/encryption/default-encryption).
  * [Create a key](https://docs.cloud.google.com/kms/docs/creating-keys).
  * Learn how to [rotate your keys](https://docs.cloud.google.com/kms/docs/rotating-keys).
  * [Audit logs](https://docs.cloud.google.com/kms/docs/audit-logging)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

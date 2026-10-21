---
url: https://docs.cloud.google.com/kms/docs/quantum-safe-key-import/
title: Quantum-safe key import \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:31.129749+00:00
---

# Quantum-safe key import  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/quantum-safe-key-import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Quantum-safe key import Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide shows you how to import a cryptographic key into Cloud Key Management Service as a new key version using a quantum-safe import method. This approach helps protect the key during transit against "store now, decrypt later" (SNDL) attacks by future quantum computers.

Quantum-safe key import uses standard post-quantum cryptography (PQC) tools including key encapsulation mechanisms (KEMs) and hybrid public key encryption (HPKE) to protect your key while in transit.

Quantum-safe key import is supported for software-backed keys (`SOFTWARE` protection level).

## Before you begin

Before you can import a key, you need to prepare the project, the local system, and the key material itself.

### Prepare the project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the required API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the required API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com&redirect=https%3A//console.cloud.google.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




### Required roles

To get the permissions that you need to import a key, ask your administrator to grant you the following IAM roles on the key ring: 

  * To import into existing keys only: [Cloud KMS Importer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.importer) (`roles/cloudkms.importer`) 
  * To import into new keys: [Cloud KMS Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.admin) (`roles/cloudkms.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Prepare the local system

You need a cryptographic library on your local system that supports post-quantum cryptography (PQC) tools including key encapsulation mechanisms (KEMs) and hybrid public key encryption (HPKE). You can use Tink, OpenSSL, or another cryptographic library that supports the following:

  * Hybrid public key encryption (HPKE)
  * One of the following KEM algorithms: 
    * `ML-KEM-768`
    * `ML-KEM-1024`
    * `X-WING` (a hybrid of `ML-KEM-768` and `X25519`)
  * The `HKDF-SHA256` key derivation function (KDF)
  * Authenticated encryption with associated data (AEAD) using the `AES-256-GCM` algorithm



### Prepare the key

Verify that your key's [algorithm and length](https://docs.cloud.google.com/kms/docs/algorithms) are supported. All versions of a key must have the same protection level (`SOFTWARE`).

## Create the target key and key ring

When you import key material, it becomes a new key version on an existing key. This key is called the target key. The target key ring and target key must exist before you can import key material.

Follow these steps to create an empty software-backed key on a new key ring using the Google Cloud CLI or the Google Cloud console.

### Console

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Click **Create key ring**.

  3. In the **Key ring name** field, enter the name for your key ring.

  4. Under **Location type** , select a location type and location.

  5. Click **Create**. The **Create key** page opens.

  6. In the **Key name** field, enter the name for your key.

  7. For **Protection level** , select **Software**.

  8. For **Key material** , select **Imported key** and then click **Continue**. This prevents an initial key version from being created.

  9. Set the **Purpose** and **Algorithm** for the key and then click **Continue**.

  10. Optional: If you want this key to contain only imported key versions, select **Restrict key versions to import only**. This prevents you from accidentally creating new key versions in Cloud KMS.

  11. Optional: For imported keys, automatic rotation is disabled by default. To enable automatic rotation, select a value from the **Key rotation period** field.

If you enable automatic rotation, new key versions will be generated in Cloud KMS, and the imported key version will no longer be the default key version after a rotation.

  12. Click **Create**.




### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).

  1. Create the target key ring. Choose a location that is compatible with the protection level that you want to use. For more information about supported locations, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).
         
         gcloud kms keyrings create KEY_RING \
           --location LOCATION
         

You can learn more about [creating key rings](https://docs.cloud.google.com/kms/docs/creating-keys#create_a_key_ring).

  2. Create the target key using the `kms keys create` command with the `--skip-initial-version-creation` flag. This creates a key with no initial key version so that your imported key material is version `1`. Use the `--import-only` flag to prevent Cloud KMS from generating key material for new key versions. With this flag set, new key versions for this key must be imported. Keys created as `--import-only` must be rotated manually.
         
         gcloud kms keys create KEY_NAME \
           --location LOCATION \
           --keyring KEY_RING \
           --purpose PURPOSE \
           --protection-level SOFTWARE \
           --skip-initial-version-creation \
           --import-only
         

Replace the following:

     * `KEY_NAME`: the name that you want to use for the key.
     * `LOCATION`: the location of the key ring.
     * `KEY_RING`: the key ring where you want to create the key.
     * `PURPOSE`: the [purpose](https://docs.cloud.google.com/kms/docs/algorithms#key_purposes) that you want to use for the key.




### API

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

  1. Create a new key ring:
         
         curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings?keyRingId=KEY_RING" \
             --request "POST" \
             --header "authorization: Bearer TOKEN" \
             --header "content-type: application/json" \
             --header "x-goog-user-project: PROJECT_ID" \
             --data "{}"
         

See the [`KeyRing.create` API documentation](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/create) for more information.

  2. Create an empty, import-only key:
         
         curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys?cryptoKeyId=KEY_NAME&skipInitialVersionCreation=true" \
             --request "POST" \
             --header "authorization: Bearer TOKEN" \
             --header "content-type: application/json" \
             --header "x-goog-user-project: PROJECT_ID" \
             --data "{"purpose":"PURPOSE", "importOnly": "true", "versionTemplate":{"protectionLevel":"PROTECTION_LEVEL","algorithm":"ALGORITHM"}}"
         

See the [`CryptoKey.create` API documentation](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/create) for more information.




The key ring and key now exist, but the key contains no key material, has no version, and is not active. Next, you create an import job.

## Create the import job

An import job defines the characteristics of the keys it imports, including the protection level and the import method.

Quantum-safe key import is supported only for the `SOFTWARE` protection level. Choose one of the following quantum-safe import methods:

  * `HPKE_KEM_XWING_HKDF_SHA256_AES_256_GCM`
  * `HPKE_KEM_ML_KEM_768_HKDF_SHA256_AES_256_GCM`
  * `HPKE_KEM_ML_KEM_1024_HKDF_SHA256_AES_256_GCM`




###  gcloud 

Run the following command to create an import job with a quantum-safe import method:
    
    
    gcloud kms import-jobs create IMPORT_JOB \
        --location LOCATION \
        --keyring KEY_RING \
        --import-method IMPORT_METHOD \
        --protection-level software
    

Replace the following:

  * `IMPORT_JOB`: a unique name to use for the import job.
  * `LOCATION`: the location of the key ring where you created your target key.
  * `KEY_RING`: the name of the key ring where you created your target key.
  * `IMPORT_METHOD`: the quantum-safe import method that you want to use—for example, `hpke-kem-xwing-hkdf-sha256-aes-256-gcm`.



###  REST 

Call the [`keyRings.importJobs.create`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/create) method:
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/importJobs?import_job_id=IMPORT_JOB" \
        --request "POST" \
        --header "authorization: Bearer TOKEN" \
        --header "content-type: application/json" \
        --data '{"import_method": "IMPORT_METHOD", "protection_level": "SOFTWARE"}'
    

Replace the following:

  * `PROJECT_ID`: the identifier of your Cloud KMS project.
  * `LOCATION`: the location of the key ring where you created your target key.
  * `KEY_RING`: the name of the key ring where you created your target key.
  * `IMPORT_JOB`: a unique name to use for the import job.
  * `TOKEN`: the token to authenticate the request.
  * `IMPORT_METHOD`: the quantum-safe import method that you want to use—for example, `HPKE_KEM_XWING_HKDF_SHA256_AES_256_GCM`.



### Check the state of the import job

The initial state for an import job is `PENDING_GENERATION`. When the state is `ACTIVE`, you can use it to import keys.

An import job expires after three days. If the import job is expired, you must create a new one.

You can check the status of an import job using the Google Cloud CLI, the Google Cloud console, or the Cloud Key Management Service API.

### Console

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Click the name of the key ring that contains your import job.

  3. Click the **Import Jobs** tab at the top of the page.

  4. The state will be visible under **Status** next to your import job's name.




### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).

When an import job is active, you can use it to import keys. This may take a few minutes. Use this command to verify that the import job is active. Use the location and keyring where you created the import job.
    
    
    gcloud kms import-jobs describe IMPORT_JOB \
      --location LOCATION \
      --keyring KEY_RING \
      --format="value(state)"
    

The output is similar to the following:
    
    
    state: ACTIVE

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Cloud KMS Go SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-go).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    )
    
    // checkStateImportJob checks the state of an ImportJob in KMS.
    func checkStateImportJob(w io.Writer, name string) error {
    	// name := "projects/PROJECT_ID/locations/global/keyRings/my-key-ring/importJobs/my-import-job"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Call the API.
    	result, err := client.GetImportJob(ctx, &kmspb.GetImportJobRequest{
    		Name: name,
    	})
    	if err != nil {
    		return fmt.Errorf("failed to get import job: %w", err)
    	}
    	fmt.Fprintf(w, "Current state of import job %q: %s\n", result.Name, result.State)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Cloud KMS Java SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-java).
    
    
    import com.google.cloud.kms.v1.[ImportJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html);
    import com.google.cloud.kms.v1.[ImportJobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJobName.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import java.io.IOException;
    
    public class CheckStateImportJob {
    
      public void checkStateImportJob() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String importJobId = "my-import-job";
        checkStateImportJob(projectId, locationId, keyRingId, importJobId);
      }
    
      // Check the state of an import job in Cloud KMS.
      public void checkStateImportJob(
          String projectId, String locationId, String keyRingId, String importJobId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the parent name from the project, location, and key ring.
          [ImportJobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJobName.html) importJobName = [ImportJobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJobName.html).of(projectId, locationId, keyRingId, importJobId);
    
          // Retrieve the state of an existing import job.
          [ImportJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html) importJob = client.getImportJob(importJobName);
          System.out.printf(
              "Current state of import job %s: %s%n", importJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html#com_google_cloud_kms_v1_ImportJob_getName__)(), importJob.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html#com_google_cloud_kms_v1_ImportJob_getState__)());
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Cloud KMS Node.js SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-nodejs).
    
    
    //
    // TODO(developer): Uncomment these variables before running the sample.
    //
    // const projectId = 'my-project';
    // const locationId = 'us-east1';
    // const keyRingId = 'my-key-ring';
    // const importJobId = 'my-import-job';
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the import job name
    const importJobName = client.importJobPath(
      projectId,
      locationId,
      keyRingId,
      importJobId
    );
    
    async function checkStateImportJob() {
      const [importJob] = await client.getImportJob({
        name: importJobName,
      });
    
      console.log(
        `Current state of import job ${importJob.name}: ${importJob.state}`
      );
      return importJob;
    }
    
    return checkStateImportJob();

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Cloud KMS Python SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python).
    
    
    from google.cloud import kms
    
    
    def check_state_import_job(
        project_id: str, location_id: str, key_ring_id: str, import_job_id: str
    ) -> None:
        """
        Check the state of an import job in Cloud KMS.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            import_job_id (string): ID of the import job (e.g. 'my-import-job').
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Retrieve the fully-qualified import_job string.
        import_job_name = client.[import_job_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_import_job_path)(
            project_id, location_id, key_ring_id, import_job_id
        )
    
        # Retrieve the state from an existing import job.
        import_job = client.[get_import_job](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_get_import_job)(name=import_job_name)
    
        print(f"Current state of import job {import_job.name}: {import_job.state}")
    
    

### API

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

To check the state of an import job, use the [`ImportJobs.get`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/get) method:
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/importJobs/IMPORT_JOB_ID" \
        --request "GET" \
        --header "authorization: Bearer TOKEN"
    

As soon as the import job is active, you can import a key.

## Retrieve the public wrapping key

After the import job is `ACTIVE`, retrieve the public key that's associated with it. You will use this public key on your local system to wrap the key material that you want to import.

###  gcloud 

Run the following command to download the public key:
    
    
    gcloud kms import-jobs describe IMPORT_JOB \
        --location LOCATION \
        --keyring KEY_RING \
        --format="value(publicKey.data)"
    

Replace the following:

  * `IMPORT_JOB`: the name of the import job.
  * `LOCATION`: the location of the key ring where you created the import job.
  * `KEY_RING`: the name of the key ring where you created the import job.



The public key is base64 encoded.

###  REST 

  1. Call the [`keyRings.importJobs.get`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/get) method.
  2. Retrieve the public key from the `publicKey.data` field of the response, and save it locally as `public_key.data`.



## Prepare and wrap your key material

Use a supported external cryptographic library on your local system to wrap the key material using the retrieved public wrapping key.

The wrapping process must perform `HPKE.Seal()` (RFC 9180) to produce a wrapped key. This completes the following steps:

  1. Encapsulate the retrieved public key to produce a shared secret and an encapsulation key.
  2. Derive an ephemeral symmetric key from the shared secret using HKDF-SHA256.
  3. Encrypt your key material with the ephemeral key using AES-256-GCM.
  4. Concatenate the encapsulation key and the key material encrypted as ciphertext. This is the resulting wrapped key that you will use to import the key. Save this as `wrapped_key.bin`.



The following Go code sample demonstrates wrapping key material using the `tink-go` library:
    
    
    package main
    
    import (
        "bytes"
        "encoding/base64"
        "flag"
        "fmt"
        "log"
    
        "google.golang.org/protobuf/proto"
        "github.com/tink-crypto/tink-go/v2/hybrid"
        "github.com/tink-crypto/tink-go/v2/keyset"
    
        hpkepb "github.com/tink-crypto/tink-go/v2/proto/hpke_go_proto"
        tinkpb "github.com/tink-crypto/tink-go/v2/proto/tink_go_proto"
    )
    
    var (
        publicKeyB64Flag = flag.String("public_key", "", "Base64 encoded public key for wrapping.")
        targetKeyB64Flag = flag.String("target_key", "", "Base64 encoded 32-byte target key to be wrapped.")
    )
    
    func main() {
        flag.Parse()
    
        if *publicKeyB64Flag == "" {
            log.Fatal("-public_key is required")
        }
        if *targetKeyB64Flag == "" {
            log.Fatal("-target_key is required")
        }
    
        pkBytes, err := base64.StdEncoding.DecodeString(*publicKeyB64Flag)
        if err != nil {
            log.Fatalf("failed to decode public key: %v", err)
        }
    
        targetKey, err := base64.StdEncoding.DecodeString(*targetKeyB64Flag)
        if err != nil {
            log.Fatalf("failed to decode target key: %v", err)
        }
    
        hpkePubKey := &hpkepb.HpkePublicKey{
            Version: 0,
            Params: &hpkepb.HpkeParams{
                Kem:  hpkepb.HpkeKem_ML_KEM768,
                Kdf:  hpkepb.HpkeKdf_HKDF_SHA256,
                Aead: hpkepb.HpkeAead_AES_256_GCM,
            },
            PublicKey: pkBytes,
        }
        serializedPubKey, err := proto.Marshal(hpkePubKey)
        if err != nil {
            log.Fatalf("failed to marshal HPKE public key: %v", err)
        }
    
        ks := &tinkpb.Keyset{
            PrimaryKeyId: 1,
            Key: []*tinkpb.Keyset_Key{
                {
                    KeyData: &tinkpb.KeyData{
                        TypeUrl:         "type.googleapis.com/google.crypto.tink.HpkePublicKey",
                        Value:           serializedPubKey,
                        KeyMaterialType: tinkpb.KeyData_ASYMMETRIC_PUBLIC,
                    },
                    Status:           tinkpb.KeyStatusType_ENABLED,
                    KeyId:            1,
                    OutputPrefixType: tinkpb.OutputPrefixType_RAW,
                },
            },
        }
        serializedKeyset, err := proto.Marshal(ks)
        if err != nil {
            log.Fatalf("failed to marshal keyset: %v", err)
        }
    
        // Create a KeysetHandle and retrieve the HybridEncrypt primitive.
        reader := keyset.NewBinaryReader(bytes.NewReader(serializedKeyset))
        handle, err := keyset.ReadWithNoSecrets(reader)
        if err != nil {
            log.Fatalf("failed to create keyset handle: %v", err)
        }
    
        enc, err := hybrid.NewHybridEncrypt(handle)
        if err != nil {
            log.Fatalf("failed to create hybrid encrypt primitive: %v", err)
        }
    
        // Perform the wrapping operation. Tink's HPKE implementation handles the
      // 'enc || ciphertext' concatenation automatically.
        wrappedKey, err := enc.Encrypt(targetKey, nil)
        if err != nil {
            log.Fatalf("failed to wrap key: %v", err)
        }
    
        fmt.Printf("Final wrappedKey (base64):\n%s\n", base64.StdEncoding.EncodeToString(wrappedKey))
    }
    

Save the output base64 string or decode it to a binary file: `bash echo "BASE64_WRAPPED_KEY" | base64 --decode > wrapped_key.bin`

**Note:** During preview, only pre-wrapped keys can be imported; automatic key wrapping isn't supported.

## Import the wrapped key

Import the prepared wrapped key as a new key version of your target key.

###  gcloud 

Run the `kms keys versions import` command:
    
    
    gcloud kms keys versions import \
        --location LOCATION \
        --keyring KEY_RING \
        --key KEY_NAME \
        --import-job IMPORT_JOB \
        --algorithm ALGORITHM \
        --wrapped-key-file wrapped_key.bin
    

Replace the following:

  * `LOCATION`: the location of the key ring that contains your target key.
  * `KEY_RING`: the name of the key ring that contains your target key.
  * `KEY_NAME`: the name of your target key.
  * `IMPORT_JOB`: the name of your import job.
  * `ALGORITHM`: the algorithm of the key material to be imported.



###  REST 

Call the [`cryptoKeyVersions.import`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/import) method:
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME/cryptoKeyVersions:import" \
        --request "POST" \
        --header "authorization: Bearer TOKEN" \
        --header "content-type: application/json" \
        --data '{"importJob": "IMPORT_JOB", "algorithm": "ALGORITHM", "wrappedKey": "PATH_TO_WRAPPED_KEY"}'
    

Replace the following:

  * `PROJECT_ID`: the identifier of your Cloud KMS project.
  * `LOCATION`: the location of the key ring that contains your target key.
  * `KEY_RING`: the name of the key ring that contains your target key.
  * `KEY_NAME`: the name of your target key.
  * `TOKEN`: the token to authenticate the request.
  * `IMPORT_JOB`: the identifier of the corresponding import job.
  * `ALGORITHM`: the algorithm of the key material to be imported.
  * `PATH_TO_WRAPPED_KEY`: the path to your manually-wrapped key in base64 format.



### Check the state of the imported key version

The initial state for an imported key version is `PENDING_IMPORT`. When the state is `ENABLED`, the key version has been imported successfully. If the import fails, the status is `IMPORT_FAILED`.

You can check the status of an import request using the Google Cloud CLI, the Google Cloud console, or the Cloud Key Management Service API.

### Console

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Click the name of the key ring that contains your import job.

  3. Click the **Import Jobs** tab at the top of the page.

  4. The state will be visible under **Status** next to your import job's name.




### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).

Use the `versions list` command to check the state. Use the same location, target key ring, and target key that you created earlier in this topic.
    
    
    gcloud kms keys versions list \
      --keyring KEY_RING \
      --location LOCATION \
      --key KEY_NAME
    

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Cloud KMS Go SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-go).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    )
    
    // checkStateImportedKey checks the state of a CryptoKeyVersion in KMS.
    func checkStateImportedKey(w io.Writer, name string) error {
    	// name := "projects/PROJECT_ID/locations/global/keyRings/my-key-ring/cryptoKeys/my-imported-key/cryptoKeyVersions/1"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Call the API.
    	result, err := client.GetCryptoKeyVersion(ctx, &kmspb.GetCryptoKeyVersionRequest{
    		Name: name,
    	})
    	if err != nil {
    		return fmt.Errorf("failed to get crypto key version: %w", err)
    	}
    	fmt.Fprintf(w, "Current state of crypto key version %q: %s\n", result.Name, result.State)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Cloud KMS Java SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-java).
    
    
    import com.google.cloud.kms.v1.[CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html);
    import com.google.cloud.kms.v1.[CryptoKeyVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import java.io.IOException;
    
    public class CheckStateImportedKey {
    
      public void checkStateImportedKey() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String cryptoKeyId = "my-crypto-key";
        String cryptoKeyVersionId = "1";
        checkStateImportedKey(projectId, locationId, keyRingId, cryptoKeyId, cryptoKeyVersionId);
      }
    
      // Check the state of an imported key in Cloud KMS.
      public void checkStateImportedKey(
          String projectId,
          String locationId,
          String keyRingId,
          String cryptoKeyId,
          String cryptoKeyVersionId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the version name from its path components.
          [CryptoKeyVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html) versionName =
              [CryptoKeyVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html).of(
                  projectId, locationId, keyRingId, cryptoKeyId, cryptoKeyVersionId);
    
          // Retrieve the state of an existing version.
          [CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html) version = client.getCryptoKeyVersion(versionName);
          System.out.printf(
              "Current state of crypto key version %s: %s%n", version.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html#com_google_cloud_kms_v1_CryptoKeyVersion_getName__)(), version.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html#com_google_cloud_kms_v1_CryptoKeyVersion_getState__)());
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Cloud KMS Node.js SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-nodejs).
    
    
    //
    // TODO(developer): Uncomment these variables before running the sample.
    //
    // const projectId = 'my-project';
    // const locationId = 'us-east1';
    // const keyRingId = 'my-key-ring';
    // const cryptoKeyId = 'my-imported-key';
    // const cryptoKeyVersionId = '1';
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the key version name
    const keyVersionName = client.cryptoKeyVersionPath(
      projectId,
      locationId,
      keyRingId,
      cryptoKeyId,
      cryptoKeyVersionId
    );
    
    async function checkStateCryptoKeyVersion() {
      const [keyVersion] = await client.getCryptoKeyVersion({
        name: keyVersionName,
      });
    
      console.log(
        `Current state of key version ${keyVersion.name}: ${keyVersion.state}`
      );
      return keyVersion;
    }
    
    return checkStateCryptoKeyVersion();

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Cloud KMS Python SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python).
    
    
    from google.cloud import kms
    
    
    def check_state_imported_key(
        project_id: str, location_id: str, key_ring_id: str, import_job_id: str
    ) -> None:
        """
        Check the state of an import job in Cloud KMS.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            import_job_id (string): ID of the import job (e.g. 'my-import-job').
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Retrieve the fully-qualified import_job string.
        import_job_name = client.[import_job_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_import_job_path)(
            project_id, location_id, key_ring_id, import_job_id
        )
    
        # Retrieve the state from an existing import job.
        import_job = client.[get_import_job](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_get_import_job)(name=import_job_name)
    
        print(f"Current state of import job {import_job.name}: {import_job.state}")
    
    

### API

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

Call the [`ImportJob.get`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/get) method and check the [`state`][api_importjob_fields_state] field. If `state` is `PENDING_GENERATION`, the import job is still being created. Periodically recheck the state until it is `ACTIVE`.

After the initial key version is imported, the key's status changes to `ENABLED`. For symmetric keys, you must [set the imported key version as the primary version](https://docs.cloud.google.com/kms/docs/importing-a-key#symmetric_keys_set_the_primary_version) before you can use the key.

## Re-import a previously destroyed key

If you need to restore a previously imported key version that is in `DESTROYED` or `IMPORT_FAILED` state back to `ENABLED` state, you can re-import the exact same key material.

Re-importing a destroyed key version uses the same procedure as the initial import, using either the original import job or a new import job (with the same `SOFTWARE` protection level).

**Note:** You can't re-import a key using a quantum-safe method if the original key version was imported using an RSA-based key import method.

[ Previous arrow_back  Wrap a key using OpenSSL  ](https://docs.cloud.google.com/kms/docs/wrapping-a-key)

[ Next Set up automatic key wrapping  arrow_forward  ](https://docs.cloud.google.com/kms/docs/crypto)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 

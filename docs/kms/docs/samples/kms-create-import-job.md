---
url: https://docs.cloud.google.com/kms/docs/samples/kms-create-import-job/
title: Create an import job \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:45.646469+00:00
---

# Create an import job  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/samples/kms-create-import-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Samples ](https://docs.cloud.google.com/kms/docs/samples)



#  Create an import job Stay organized with collections  Save and categorize content based on your preferences. 

Create a new import job in Cloud KMS.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Import a key version into Cloud KMS](https://docs.cloud.google.com/kms/docs/importing-a-key)



## Code sample

### Go

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    )
    
    // createImportJob creates a new job for importing keys into KMS.
    func createImportJob(w io.Writer, parent, id string) error {
    	// parent := "projects/PROJECT_ID/locations/global/keyRings/my-key-ring"
    	// id := "my-import-job"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Build the request.
    	req := &kmspb.CreateImportJobRequest{
    		Parent:      parent,
    		ImportJobId: id,
    		ImportJob: &kmspb.ImportJob{
    			// See allowed values and their descriptions at
    			// https://cloud.google.com/kms/docs/algorithms#protection_levels
    			ProtectionLevel: kmspb.[ProtectionLevel_HSM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_ProtectionLevel_PROTECTION_LEVEL_UNSPECIFIED_ProtectionLevel_SOFTWARE_ProtectionLevel_HSM_ProtectionLevel_EXTERNAL_ProtectionLevel_EXTERNAL_VPC_ProtectionLevel_HSM_SINGLE_TENANT),
    			// See allowed values and their descriptions at
    			// https://cloud.google.com/kms/docs/key-wrapping#import_methods
    			ImportMethod: kmspb.[ImportJob_RSA_OAEP_3072_SHA1_AES_256](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_ImportJob_IMPORT_METHOD_UNSPECIFIED_ImportJob_RSA_OAEP_3072_SHA1_AES_256_ImportJob_RSA_OAEP_4096_SHA1_AES_256_ImportJob_RSA_OAEP_3072_SHA256_AES_256_ImportJob_RSA_OAEP_4096_SHA256_AES_256_ImportJob_RSA_OAEP_3072_SHA256_ImportJob_RSA_OAEP_4096_SHA256_ImportJob_HPKE_KEM_ML_KEM_768_HKDF_SHA256_AES_256_GCM_ImportJob_HPKE_KEM_ML_KEM_1024_HKDF_SHA256_AES_256_GCM_ImportJob_HPKE_KEM_XWING_HKDF_SHA256_AES_256_GCM),
    		},
    	}
    
    	// Call the API.
    	result, err := client.CreateImportJob(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to create import job: %w", err)
    	}
    	fmt.Fprintf(w, "Created import job: %s\n", result.Name)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.kms.v1.[ImportJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html);
    import com.google.cloud.kms.v1.[ImportJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html).[ImportMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.ImportMethod.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.cloud.kms.v1.[KeyRingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html);
    import com.google.cloud.kms.v1.[ProtectionLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ProtectionLevel.html);
    import java.io.IOException;
    
    public class CreateImportJob {
    
      public void createImportJob() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String id = "my-import-job";
        createImportJob(projectId, locationId, keyRingId, id);
      }
    
      // Create a new import job.
      public void createImportJob(String projectId, String locationId, String keyRingId, String id)
          throws IOException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the parent name from the project, location, and key ring.
          [KeyRingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) keyRingName = [KeyRingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html).of(projectId, locationId, keyRingId);
    
          // Build the import job to create, with parameters.
          [ImportJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html) importJob =
              [ImportJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html).newBuilder()
                  // See allowed values and their descriptions at
                  // https://cloud.google.com/kms/docs/algorithms#protection_levels
                  .setProtectionLevel([ProtectionLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ProtectionLevel.html).HSM)
                  // See allowed values and their descriptions at
                  // https://cloud.google.com/kms/docs/key-wrapping#import_methods
                  .[setImportMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.Builder.html#com_google_cloud_kms_v1_ImportJob_Builder_setImportMethod_com_google_cloud_kms_v1_ImportJob_ImportMethod_)([ImportMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.ImportMethod.html).RSA_OAEP_3072_SHA1_AES_256)
                  .build();
    
          // Create the import job.
          [ImportJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html) createdImportJob = client.createImportJob(keyRingName, id, importJob);
          System.out.printf("Created import job %s%n", createdImportJob.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ImportJob.html#com_google_cloud_kms_v1_ImportJob_getName__)());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //
    // TODO(developer): Uncomment these variables before running the sample.
    //
    // const projectId = 'my-project';
    // const locationId = 'us-east1';
    // const keyRingId = 'my-key-ring';
    // const id = 'my-import-job';
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the parent key ring name
    const keyRingName = client.keyRingPath(projectId, locationId, keyRingId);
    
    async function createImportJob() {
      const [importJob] = await client.createImportJob({
        parent: keyRingName,
        importJobId: id,
        importJob: {
          protectionLevel: 'HSM',
          importMethod: 'RSA_OAEP_3072_SHA256',
        },
      });
    
      console.log(`Created import job: ${importJob.name}`);
      return importJob;
    }
    
    return createImportJob();

### Python

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import kms
    
    
    def create_import_job(
        project_id: str, location_id: str, key_ring_id: str, import_job_id: str
    ) -> None:
        """
        Create a new import job in Cloud KMS.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            import_job_id (string): ID of the import job (e.g. 'my-import-job').
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Retrieve the fully-qualified key_ring string.
        key_ring_name = client.[key_ring_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_key_ring_path)(project_id, location_id, key_ring_id)
    
        # Set paramaters for the import job, allowed values for ImportMethod and ProtectionLevel found here:
        # https://googleapis.dev/python/cloudkms/latest/_modules/google/cloud/kms_v1/types/resources.html
    
        import_method = kms.[ImportJob](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.ImportJob.html).[ImportMethod](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.ImportJob.ImportMethod.html).RSA_OAEP_3072_SHA1_AES_256
        protection_level = kms.[ProtectionLevel](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.ProtectionLevel.html).HSM
        import_job_params = {
            "import_method": import_method,
            "protection_level": protection_level,
        }
    
        # Call the client to create a new import job.
        import_job = client.[create_import_job](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_create_import_job)(
            {
                "parent": key_ring_name,
                "import_job_id": import_job_id,
                "import_job": import_job_params,
            }
        )
    
        print(f"Created import job: {import_job.name}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudkeymanagementservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

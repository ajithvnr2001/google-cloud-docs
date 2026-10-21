---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/cmek/
title: Enable customer-managed encryption keys for Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:09:44.813221+00:00
---

# Enable customer-managed encryption keys for Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Enable customer-managed encryption keys for Parameter Manager Stay organized with collections  Save and categorize content based on your preferences. 

By default, Parameter Manager [encrypts user data at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption). Parameter Manager handles encryption for you without any additional actions. This option is Google default encryption.

You can enforce granular control over your encryption keys by using Customer-Managed Encryption Keys (CMEKs) within [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs). Services like Parameter Manager integrate seamlessly with CMEKs, letting you manage protection levels, locations, usage, access permissions, and cryptographic boundaries of your keys directly in Cloud KMS. Using Cloud KMS also lets you view audit logs, and control key life cycles. Instead of Google owning and managing the symmetric key encryption keys that protect your data, you control and manage these keys in Cloud KMS.

Accessing your Parameter Manager resources with CMEKs is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/kms/docs/cmek).

You can configure a CMEK on the parameter resource. This key is used to protect the parameter version payload. Parameter version payload data is encrypted using [envelope encryption](https://docs.cloud.google.com/kms/docs/envelope-encryption) upon creation.

**Caution:** If you temporarily disable or permanently destroy the CMEK, the data encrypted with that key can't be decrypted and is therefore inaccessible.

## How CMEK works in Parameter Manager

Before writing a parameter version to persistent storage in a specific location, Parameter Manager encrypts the data with a unique data encryption key (DEK). This DEK is then encrypted with a replica-specific key encryption key (KEK) owned by the Parameter Manager service.

When you use CMEK for Parameter Manager, the KEK is a symmetric key that you manage in Cloud KMS. The CMEK key must be in the same Google Cloud location as the parameter version replica. You can also use an Cloud EKM key as a CMEK for encryption and decryption.

The expected format for a CMEK is `projects/*/locations/*/keyRings/*/cryptoKeys/*`.

For more information about CMEK, including when and why to enable it, see the [ Cloud Key Management Service documentation](https://docs.cloud.google.com/kms/docs/cmek).

**Important:** Parameter Manager uses the `primary` Cloud KMS key version for CMEK encryption. CMEK can only be configured with the primary key version.

## Before you begin

Complete the following prerequisites to set up Parameter Manager and Cloud KMS:

  * Parameter Manager

    * Create or use an existing project to hold your Parameter Manager resources.
    * If necessary, complete the steps on the [Prepare environment for Parameter Manager](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/prepare-environment) page.
  * Cloud KMS

    * Create or use an existing project that holds your Cloud KMS resources.
    * If necessary, [enable the Cloud KMS API](https://docs.cloud.google.com/kms/docs/quickstart#before_you_begin).



Set the following variables to your Parameter Manager and Cloud KMS project IDs.

  * PM_PROJECT_ID: the Parameter Manager project ID. Used in all commands on this page.
  * KMS_PROJECT_ID: the Cloud KMS project ID. Used in all commands on this page.



You can store the key ring within the same project as your resources, or in a different project. Using different projects provides more fine-grained control and supports the [separation of duties](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/\(/kms/docs/separation-of-duties\)).

**Note:** Cloud KMS usage is subject to Cloud HSM and Cloud EKM [additional quota limitations](https://docs.cloud.google.com/kms/docs/quotas#cloud_hsm_quotas) depending on the type of CMEK key used. Parameter Manager calls Cloud KMS every time it performs a cryptographic operation. CMEK key usage is billed to the Cloud KMS project.

## Configure CMEK on a parameter

To set up a CMEK to protect a specific parameter, follow these steps:

  1. Create a new symmetric Cloud KMS key or use an existing one. This example demonstrates creating a new key ring and key.

### gcloud
         
         gcloud kms keyrings create "KEY_RING" \
             --project "KMS_PROJECT_ID" \
             --location "LOCATION"
         
         gcloud kms keys create "KEY_NAME" \
             --project "KMS_PROJECT_ID" \
             --location "LOCATION" \
             --keyring "parameter-manager-cmek" \
             --purpose "encryption"

Replace the following variables:

     * KEY_RING: the name of the key ring that contains the key.
     * KMS_PROJECT_ID: the Cloud KMS project ID.
     * LOCATION: the Cloud KMS location of the key ring. Choose the same location as the parameter resource. Otherwise, the parameter version creation request is rejected.
     * KEY_NAME: the name of the key.
  2. Create a parameter. The resource name of the CMEK is stored as metadata on the parameter.

**Global parameters**

### gcloud

Before using any of the command data below, make the following replacements: 

     * PARAMETER_ID: the name of the parameter
     * PM_PROJECT_ID: the Parameter Manager project ID

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud parametermanager parameters create "PARAMETER_ID" \
             --kms-key "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME" \
             --project "PM_PROJECT_ID"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud parametermanager parameters create "PARAMETER_ID" `
             --kms-key "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME" `
             --project "PM_PROJECT_ID"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud parametermanager parameters create "PARAMETER_ID" ^
             --kms-key "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME" ^
             --project "PM_PROJECT_ID"

### REST

Before using any of the request data, make the following replacements: 

     * PARAMETER_ID: the name of the parameter
     * PM_PROJECT_ID: the Parameter Manager project ID

HTTP method and URL: 
    
    POST https://parametermanager.googleapis.com/v1/projects/PM_PROJECT_ID/parameters?parameter_id=PARAMETER_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://parametermanager.googleapis.com/v1/projects/PM_PROJECT_ID/parameters?parameter_id=PARAMETER_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://parametermanager.googleapis.com/v1/projects/PM_PROJECT_ID/parameters?parameter_id=PARAMETER_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Parameter Manager Go SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-go). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	parametermanager "cloud.google.com/go/parametermanager/apiv1"
    	parametermanagerpb "cloud.google.com/go/parametermanager/apiv1/parametermanagerpb"
    )
    
    // createParamWithKmsKey creates a parameter with kms_key using the Parameter Manager SDK for GCP.
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // parameterID: The ID of the parameter to be created.
    // kmsKey: The ID of the KMS key to be used for encryption.
    // (e.g. "projects/my-project/locations/global/keyRings/my-key-ring/cryptoKeys/my-encryption-key")
    // (For more information, see: https://cloud.google.com/secret-manager/parameter-manager/docs/cmek)
    //
    // The function returns an error if the parameter creation fails.
    func createParamWithKmsKey(w io.Writer, projectID, parameterID, kmsKey string) error {
    	// Create a context and a Parameter Manager client.
    	ctx := context.Background()
    
    	// Create a Parameter Manager client.
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the create parameter.
    	parent := fmt.Sprintf("projects/%s/locations/global", projectID)
    
    	// Create a parameter with unformatted format.
    	req := &parametermanagerpb.CreateParameterRequest{
    		Parent:      parent,
    		ParameterId: parameterID,
    		Parameter: &parametermanagerpb.Parameter{
    			Format: parametermanagerpb.[ParameterFormat_UNFORMATTED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1/parametermanagerpb.html#cloud_google_com_go_parametermanager_apiv1_parametermanagerpb_ParameterFormat_PARAMETER_FORMAT_UNSPECIFIED_ParameterFormat_UNFORMATTED_ParameterFormat_YAML_ParameterFormat_JSON),
    			KmsKey: &kmsKey,
    		},
    	}
    	parameter, err := client.CreateParameter(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to create parameter: %w", err)
    	}
    
    	fmt.Fprintf(w, "Created parameter %s with kms_key %s\n", parameter.Name, *parameter.KmsKey)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    import com.google.cloud.parametermanager.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html);
    import com.google.cloud.parametermanager.v1.[Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import java.io.IOException;
    
    /**
     * Example class to create a new parameter with provided KMS key
     * using the Parameter Manager SDK for GCP.
     */
    public class CreateParamWithKmsKey {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String parameterId = "your-parameter-id";
        String kmsKeyName = "your-kms-key";
    
        // Call the method to create a parameter with the specified kms key.
        createParameterWithKmsKey(projectId, parameterId, kmsKeyName);
      }
    
      // This is an example snippet for creating a new parameter with a specific format.
      public static [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) createParameterWithKmsKey(
          String projectId, String parameterId, String kmsKeyName) throws IOException {
        // Initialize the client that will be used to send requests.
        try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create()) {
          String locationId = "global";
    
          // Build the parent name from the project.
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html) location = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html).of(projectId, locationId);
    
          // Build the parameter to create with the provided format.
          [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) parameter = [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html).newBuilder().[setKmsKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.Builder.html#com_google_cloud_parametermanager_v1_Parameter_Builder_setKmsKey_java_lang_String_)(kmsKeyName).build();
    
          // Create the parameter.
          [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) createdParameter =
              client.createParameter(location.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html#com_google_cloud_parametermanager_v1_LocationName_toString__)(), parameter, parameterId);
          System.out.printf(
              "Created parameter %s with kms key %s\n",
              createdParameter.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html#com_google_cloud_parametermanager_v1_Parameter_getName__)(), createdParameter.[getKmsKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html#com_google_cloud_parametermanager_v1_Parameter_getKmsKey__)());
    
          return createdParameter;
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Parameter Manager Node.js SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-nodejs). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const parameterId = 'YOUR_PARAMETER_ID';
    // const kmsKey = 'YOUR_KMS_KEY'
    
    // Imports the Parameter Manager library
    const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
    
    // Instantiates a client
    const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)();
    
    async function createParamWithKmsKey() {
      const parent = client.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(projectId, 'global');
      const request = {
        parent: parent,
        parameterId: parameterId,
        parameter: {
          kmsKey: kmsKey,
        },
      };
    
      const [parameter] = await client.createParameter(request);
      console.log(
        `Created parameter ${parameter.name} with kms_key ${parameter.kmsKey}`
      );
      return parameter;
    }
    
    return await createParamWithKmsKey();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    // Import necessary classes for creating a parameter.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\CreateParameterRequest;
    use Google\Cloud\ParameterManager\V1\Parameter;
    
    /**
     * Creates a parameter of type "unformatted" with provided KMS key using the Parameter Manager SDK for GCP.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     * @param string $kmsKey The KMS key used to encrypt the parameter (e.g. 'projects/my-project/locations/global/keyRings/test/cryptoKeys/test-key')
     */
    function create_param_with_kms_key(string $projectId, string $parameterId, string $kmsKey): void
    {
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient();
    
        // Build the resource name of the parent object.
        $parent = $client->locationName($projectId, 'global');
    
        // Create a new Parameter object.
        $parameter = (new Parameter())
        ->setKmsKey($kmsKey);
    
        // Prepare the request with the parent, parameter ID, and the parameter object.
        $request = (new CreateParameterRequest())
            ->setParent($parent)
            ->setParameterId($parameterId)
            ->setParameter($parameter);
    
        // Crete the parameter.
        $newParameter = $client->createParameter($request);
    
        // Print the new parameter name
        printf('Created parameter %s with kms key %s' . PHP_EOL, $newParameter->getName(), $newParameter->getKmsKey());
    
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    def create_param_with_kms_key(
        project_id: str, parameter_id: str, kms_key: str
    ) -> parametermanager_v1.Parameter:
        """
        Creates a parameter with default format (Unformatted)
        in the global location of the specified
        project and kms key using the Google Cloud Parameter Manager SDK.
    
        Args:
            project_id (str): The ID of the project where
            the parameter is to be created.
            parameter_id (str): The ID to assign to the new parameter.
            This ID must be unique within the project.
            kms_key (str): The KMS key used to encrypt the parameter.
    
        Returns:
            parametermanager_v1.Parameter: An object representing
            the newly created parameter.
    
        Example:
            create_param_with_kms_key(
                "my-project",
                "my-global-parameter",
                "projects/my-project/locations/global/keyRings/test/cryptoKeys/test-key"
            )
        """
        # Import the necessary library for Google Cloud Parameter Manager.
        from google.cloud import [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest)
    
        # Create the Parameter Manager client.
        client = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterManagerClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html)()
    
        # Build the resource name of the parent project in the global location.
        parent = client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_common_location_path)(project_id, "global")
    
        # Define the parameter creation request.
        request = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[CreateParameterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.CreateParameterRequest.html)(
            parent=parent,
            parameter_id=parameter_id,
            parameter=[parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[Parameter](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.Parameter.html)(kms_key=kms_key),
        )
    
        # Create the parameter.
        response = client.[create_parameter](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_create_parameter)(request=request)
    
        # Print the newly created parameter name.
        print(f"Created parameter {response.name} with kms key {kms_key}")

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    require "google/cloud/parameter_manager"
    
    ##
    # Create a parameter with a KMS key
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    # @param parameter_id [String] The parameter name (e.g. "my-parameter")
    # @param kms_key [String] The KMS key name
    # (e.g. "projects/my-project/locations/global/keyRings/my-keyring/cryptoKeys/my-key")
    #
    def create_param_with_kms_key project_id:, parameter_id:, kms_key:
      # Create a Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html)
    
      # Build the resource name of the parent project.
      parent = client.[location_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: "global"
    
      parameter = {
        kms_key: kms_key
      }
    
      # Create the parameter.
      param = client.create_parameter parent: parent, parameter_id: parameter_id, parameter: parameter
    
      # Print the new parameter name.
      puts "Created parameter #{param.name} with kms_key #{param.[kms_key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-Parameter.html)}"
    end

**Regional parameters**

### gcloud

Before using any of the command data below, make the following replacements: 

     * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter
     * PARAMETER_ID: the name of the parameter
     * PM_PROJECT_ID: the Parameter Manager project ID

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud parametermanager parameters create "PARAMETER_ID" \
             --location "LOCATION" \
             --kms-key "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME" \
             --project "PM_PROJECT_ID"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud parametermanager parameters create "PARAMETER_ID" `
             --location "LOCATION" `
             --kms-key "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME" `
             --project "PM_PROJECT_ID"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud parametermanager parameters create "PARAMETER_ID" ^
             --location "LOCATION" ^
             --kms-key "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME" ^
             --project "PM_PROJECT_ID"

### REST

Before using any of the request data, make the following replacements: 

     * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter
     * PARAMETER_ID: the name of the parameter
     * PM_PROJECT_ID: the Parameter Manager project ID

HTTP method and URL: 
    
    POST https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PM_PROJECT_ID/locations/LOCATION/parameters?parameter_id=PARAMETER_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PM_PROJECT_ID/locations/LOCATION/parameters?parameter_id=PARAMETER_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PM_PROJECT_ID/locations/LOCATION/parameters?parameter_id=PARAMETER_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Parameter Manager Go SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-go). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	parametermanager "cloud.google.com/go/parametermanager/apiv1"
    	parametermanagerpb "cloud.google.com/go/parametermanager/apiv1/parametermanagerpb"
    	"google.golang.org/api/option"
    )
    
    // createRegionalParamWithKmsKey creates a regional parameter with kms_key using the Parameter Manager SDK for GCP.
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // locationID: The ID of the location where the parameter is located.
    // parameterID: The ID of the parameter to be created.
    // kmsKey: The ID of the KMS key to be used for encryption.
    // (e.g. "projects/my-project/locations/us-central1/keyRings/my-key-ring/cryptoKeys/my-encryption-key")
    // (For more information, see: https://cloud.google.com/secret-manager/parameter-manager/docs/cmek)
    //
    // The function returns an error if the parameter creation fails.
    func createRegionalParamWithKmsKey(w io.Writer, projectID, locationID, parameterID, kmsKey string) error {
    	// Create a context and a Parameter Manager client.
    	ctx := context.Background()
    
    	// Create a Parameter Manager client.
    	endpoint := fmt.Sprintf("parametermanager.%s.rep.googleapis.com:443", locationID)
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx, option.WithEndpoint(endpoint))
    	if err != nil {
    		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the create parameter.
    	parent := fmt.Sprintf("projects/%s/locations/%s", projectID, locationID)
    
    	// Create a parameter with unformatted format.
    	req := &parametermanagerpb.CreateParameterRequest{
    		Parent:      parent,
    		ParameterId: parameterID,
    		Parameter: &parametermanagerpb.Parameter{
    			Format: parametermanagerpb.[ParameterFormat_UNFORMATTED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1/parametermanagerpb.html#cloud_google_com_go_parametermanager_apiv1_parametermanagerpb_ParameterFormat_PARAMETER_FORMAT_UNSPECIFIED_ParameterFormat_UNFORMATTED_ParameterFormat_YAML_ParameterFormat_JSON),
    			KmsKey: &kmsKey,
    		},
    	}
    	parameter, err := client.CreateParameter(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to create parameter: %w", err)
    	}
    
    	fmt.Fprintf(w, "Created regional parameter %s with kms_key %s\n", parameter.Name, *parameter.KmsKey)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    import com.google.cloud.parametermanager.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html);
    import com.google.cloud.parametermanager.v1.[Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html);
    import java.io.IOException;
    
    /**
     * Example class to create a new regional parameter with provided KMS 
     * key using the Parameter Manager SDK for GCP.
     */
    public class CreateRegionalParamWithKmsKey {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "your-location-id";
        String parameterId = "your-parameter-id";
        String kmsKeyName = "your-kms-key";
    
        // Call the method to create a regional parameter with the specified kms key.
        createRegionalParameterWithKmsKey(projectId, locationId, parameterId, kmsKeyName);
      }
    
      // This is an example snippet for creating a new parameter with a specific format.
      public static [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) createRegionalParameterWithKmsKey(
          String projectId, String locationId, String parameterId, String kmsKeyName)
          throws IOException {
    
        // Endpoint to call the regional parameter manager server
        String apiEndpoint = String.format("parametermanager.%s.rep.googleapis.com:443", locationId);
        [ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html) parameterManagerSettings =
            [ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html).newBuilder().setEndpoint(apiEndpoint).build();
    
        // Initialize the client that will be used to send requests. This client only needs to be
        // created once, and can be reused for multiple requests.
        try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create(parameterManagerSettings)) {
    
          // Build the parent name from the project.
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html) location = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html).of(projectId, locationId);
    
          // Build the parameter to create with the provided format.
          [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) parameter = [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html).newBuilder().[setKmsKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.Builder.html#com_google_cloud_parametermanager_v1_Parameter_Builder_setKmsKey_java_lang_String_)(kmsKeyName).build();
    
          // Create the parameter.
          [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) createdParameter =
              client.createParameter(location.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html#com_google_cloud_parametermanager_v1_LocationName_toString__)(), parameter, parameterId);
          System.out.printf(
              "Created regional parameter %s with kms key %s\n",
              createdParameter.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html#com_google_cloud_parametermanager_v1_Parameter_getName__)(), createdParameter.[getKmsKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html#com_google_cloud_parametermanager_v1_Parameter_getKmsKey__)());
    
          return createdParameter;
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Parameter Manager Node.js SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-nodejs). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const locationId = 'YOUR_LOCATION_ID';
    // const parameterId = 'YOUR_PARAMETER_ID';
    // const kmsKey = 'YOUR_KMS_KEY'
    
    // Imports the Parameter Manager library
    const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
    
    // Adding the endpoint to call the regional parameter manager server
    const options = {
      apiEndpoint: `parametermanager.${locationId}.rep.googleapis.com`,
    };
    
    // Instantiates a client with regional endpoint
    const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)(options);
    
    async function createRegionalParamWithKmsKey() {
      const parent = client.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(projectId, locationId);
      const request = {
        parent: parent,
        parameterId: parameterId,
        parameter: {
          kmsKey: kmsKey,
        },
      };
    
      const [parameter] = await client.createParameter(request);
      console.log(
        `Created regional parameter ${parameter.name} with kms_key ${parameter.kmsKey}`
      );
      return parameter;
    }
    
    return await createRegionalParamWithKmsKey();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    // Import necessary classes for creating a parameter.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\CreateParameterRequest;
    use Google\Cloud\ParameterManager\V1\Parameter;
    
    /**
     * Creates a regional parameter of type "unformatted" with provided KMS key using the Parameter Manager SDK for GCP.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $locationId The Parameter Location (e.g. 'us-central1')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     * @param string $kmsKey The KMS key used to encrypt the parameter (e.g. 'projects/my-project/locations/us-central1/keyRings/test/cryptoKeys/test-key')
     */
    function create_regional_param_with_kms_key(string $projectId, string $locationId, string $parameterId, string $kmsKey): void
    {
        // Specify regional endpoint.
        $options = ['apiEndpoint' => "parametermanager.$locationId.rep.googleapis.com"];
    
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient($options);
    
        // Build the resource name of the parent object.
        $parent = $client->locationName($projectId, $locationId);
    
        // Create a new Parameter object.
        $parameter = (new Parameter())
        ->setKmsKey($kmsKey);
    
        // Prepare the request with the parent, parameter ID, and the parameter object.
        $request = (new CreateParameterRequest())
            ->setParent($parent)
            ->setParameterId($parameterId)
            ->setParameter($parameter);
    
        // Crete the parameter.
        $newParameter = $client->createParameter($request);
    
        // Print the new parameter name
        printf('Created regional parameter %s with kms key %s' . PHP_EOL, $newParameter->getName(), $newParameter->getKmsKey());
    
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    def create_regional_param_with_kms_key(
        project_id: str, location_id: str, parameter_id: str, kms_key: str
    ) -> parametermanager_v1.Parameter:
        """
        Creates a regional parameter with default format (Unformatted)
        in the specified location, project and with kms key
        using the Google Cloud Parameter Manager SDK.
    
        Args:
            project_id (str): The ID of the project where
            the regional parameter is to be created.
            location_id (str): The region where the parameter is to be created.
            parameter_id (str): The ID to assign to the new parameter.
            This ID must be unique within the project.
            kms_key (str): The KMS key used to encrypt the parameter.
    
        Returns:
            parametermanager_v1.Parameter: An object representing
            the newly created regional parameter.
    
        Example:
            create_regional_param_with_kms_key(
                "my-project",
                "us-central1",
                "my-regional-parameter",
                "projects/my-project/locations/us-central1/keyRings/test/cryptoKeys/test-key"
            )
        """
    
        # Import the Parameter Manager client library.
        from google.cloud import [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest)
    
        api_endpoint = f"parametermanager.{location_id}.rep.googleapis.com"
        # Create the Parameter Manager client for the specified region.
        client = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterManagerClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html)(
            client_options={"api_endpoint": api_endpoint}
        )
    
        # Build the resource name of the parent project for the specified region.
        parent = client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_common_location_path)(project_id, location_id)
    
        # Define the parameter creation request.
        request = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[CreateParameterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.CreateParameterRequest.html)(
            parent=parent,
            parameter_id=parameter_id,
            parameter=[parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[Parameter](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.Parameter.html)(kms_key=kms_key),
        )
    
        # Create the parameter.
        response = client.[create_parameter](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_create_parameter)(request=request)
    
        # Print the newly created parameter name.
        print(f"Created regional parameter {response.name} with kms key {kms_key}")

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    require "google/cloud/parameter_manager"
    
    ##
    # Create a regional parameter with a KMS key
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    # @param location_id [String] The location name (e.g. "us-central1")
    # @param parameter_id [String] The parameter name (e.g. "my-parameter")
    # @param kms_key [String] The KMS key name
    # (e.g. "projects/my-project/locations/us-central1/keyRings/my-keyring/cryptoKeys/my-key")
    #
    def create_regional_param_with_kms_key project_id:, location_id:, parameter_id:, kms_key:
      # Endpoint for the regional parameter manager service.
      api_endpoint = "parametermanager.#{location_id}.rep.googleapis.com"
    
      # Create the Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html) do |config|
        config.endpoint = api_endpoint
      end
    
      # Build the resource name of the parent project.
      parent = client.[location_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: location_id
    
      parameter = {
        kms_key: kms_key
      }
    
      # Create the parameter.
      param = client.create_parameter parent: parent, parameter_id: parameter_id, parameter: parameter
    
      # Print the new parameter name.
      puts "Created regional parameter #{param.name} with kms_key #{param.[kms_key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-Parameter.html)}"
    end

  3. Grant the Parameter Manager service identity, which is specific to your project, the permission to use your encryption key. This lets Parameter Manager encrypt and decrypt data as needed, using your chosen key. To do this, assign the Cloud KMS CryptoKey Encrypter/Decrypter role (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) to the service identity. Note that the service identity is automatically created when you create the first parameter in your project.

### gcloud
         
         gcloud kms keys add-iam-policy-binding "my-cmek-key" \
             --project "KMS_PROJECT_ID" \
             --location "LOCATION" \
             --keyring "parameter-manager-cmek" \
             --member "service-PROJECT_NUMBER@gcp-sa-pm.iam.gserviceaccount.com" \
             --role "roles/cloudkms.cryptoKeyEncrypterDecrypter"

Replace PROJECT_NUMBER with the project number of the Google Cloud project where the parameter is stored.

When the service creates a parameter version, it automatically encrypts the parameter version's payload with the key before writing it to persistent storage, if the service identity can access the customer-managed encryption key (CMEK). If the service identity can't access the key, attempts to create or access parameter versions return an error.

  4. Create a new parameter version. Notice that if you don't specify the Cloud KMS key's resource name, it is read from the parameter's metadata.

### gcloud
         
         gcloud parametermanager parameters versions create PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=LOCATION --payload-data="PARAMETER_PAYLOAD"

Replace the following variables:

     * PARAMETER_VERSION_ID: the ID that you want to assign to the parameter version. Parameter version IDs must be 63 characters or less and consist only of alphanumeric characters (A-Z, a-z, 0-9), dashes (-), and underscores (_). IDs cannot begin with a dash.
     * PARAMETER_PAYLOAD: the data, in plaintext, that you want to store within the parameter.

The parameter version is created, even if the caller doesn't have direct access to use the CMEK key. The service identity for Parameter Manager, rather than the caller, is responsible for encrypting and decrypting parameters when reading or writing them.

Similarly, you don't need direct access to the CMEK key in order to access the parameter. The service identity accesses the key and encrypts or decrypts the parameter on your behalf.

  5. View the parameter version you just created:

### gcloud
         
         gcloud parametermanager parameters versions describe PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=LOCATION




## Update CMEK configuration

To change the encryption key used to protect your data, follow these steps:

  1. Create a new symmetric KMS key in the selected Cloud KMS location.

### gcloud
         
         gcloud kms keys create "my-other-key" \
             --project "KMS_PROJECT_ID" \
             --location "LOCATION" \
             --keyring "parameter-manager-cmek" \
             --purpose "encryption"

  2. Assign the Parameter Manager service identity the necessary permissions to use your encryption key.

### gcloud
         
         gcloud kms keys add-iam-policy-binding "my-other-key" \
             --project "KMS_PROJECT_ID" \
             --location "LOCATION" \
             --keyring "parameter-manager-cmek" \
             --member "service-PROJECT_NUMBER@gcp-sa-pm.iam.gserviceaccount.com" \
             --role "roles/cloudkms.cryptoKeyEncrypterDecrypter"

  3. Modify the CMEK configuration on a parameter by updating the parameter to use the new Cloud KMS key resource names.

**Global parameters**

### gcloud

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
         
         gcloud parametermanager parameters update "PARAMETER_ID" --kms-key "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/parameter-manager-cmek/cryptoKeys/my-other-key"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
         
         gcloud parametermanager parameters update "PARAMETER_ID" --kms-key "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/parameter-manager-cmek/cryptoKeys/my-other-key"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
         
         gcloud parametermanager parameters update "PARAMETER_ID" --kms-key "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/parameter-manager-cmek/cryptoKeys/my-other-key"

### REST

HTTP method and URL: 
         
         PATCH https://parametermanager.googleapis.com/v1/projects/PM_PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID?update_mask=kmsKey

Request JSON body: 
         
         {
           "payload": {
             "kmsKey": "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/parameter-manager-cmek/cryptoKeys/my-other-key"
           }
         }
         
         

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
         
         curl -X PATCH \  
              -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
              -H "Content-Type: application/json; charset=utf-8" \  
              -d @request.json \  
              "https://parametermanager.googleapis.com/v1/projects/PM_PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID?update_mask=kmsKey"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
         
         $cred = gcloud auth print-access-token  
         $headers = @{ "Authorization" = "Bearer $cred" }  
           
         Invoke-WebRequest `  
             -Method PATCH `  
             -Headers $headers `  
             -ContentType: "application/json; charset=utf-8" `  
             -InFile request.json `  
             -Uri "https://parametermanager.googleapis.com/v1/projects/PM_PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID?update_mask=kmsKey" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Parameter Manager Go SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-go). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
         
         import (
         	"context"
         	"fmt"
         	"io"
         
         	parametermanager "cloud.google.com/go/parametermanager/apiv1"
         	parametermanagerpb "cloud.google.com/go/parametermanager/apiv1/parametermanagerpb"
         	"google.golang.org/genproto/protobuf/field_mask"
         )
         
         // updateParamKmsKey updates a parameter kms_key using the Parameter Manager SDK for GCP.
         //
         // w: The io.Writer object used to write the output.
         // projectID: The ID of the project where the parameter is located.
         // parameterID: The ID of the parameter to be updated.
         // kmsKey: The ID of the KMS key to be used for encryption.
         // (e.g. "projects/my-project/locations/global/keyRings/my-key-ring/cryptoKeys/my-encryption-key")
         // (For more information, see: https://cloud.google.com/secret-manager/parameter-manager/docs/cmek)
         //
         // The function returns an error if the parameter creation fails.
         func updateParamKmsKey(w io.Writer, projectID, parameterID, kmsKey string) error {
         	// Create a context and a Parameter Manager client.
         	ctx := context.Background()
         
         	// Create a Parameter Manager client.
         	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx)
         	if err != nil {
         		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
         	}
         	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
         
         	// Construct the name of the create parameter.
         	name := fmt.Sprintf("projects/%s/locations/global/parameters/%s", projectID, parameterID)
         
         	// Create a parameter with unformatted format.
         	req := &parametermanagerpb.UpdateParameterRequest{
         		Parameter: &parametermanagerpb.Parameter{
         			Name:   name,
         			Format: parametermanagerpb.[ParameterFormat_UNFORMATTED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1/parametermanagerpb.html#cloud_google_com_go_parametermanager_apiv1_parametermanagerpb_ParameterFormat_PARAMETER_FORMAT_UNSPECIFIED_ParameterFormat_UNFORMATTED_ParameterFormat_YAML_ParameterFormat_JSON),
         			KmsKey: &kmsKey,
         		},
         		UpdateMask: &field_mask.FieldMask{
         			Paths: []string{"kms_key"},
         		},
         	}
         	parameter, err := client.UpdateParameter(ctx, req)
         	if err != nil {
         		return fmt.Errorf("failed to update parameter: %w", err)
         	}
         
         	fmt.Fprintf(w, "Updated parameter %s with kms_key %s\n", parameter.Name, *parameter.KmsKey)
         	return nil
         }
         

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
         
         import com.google.cloud.parametermanager.v1.[Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html);
         import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
         import com.google.cloud.parametermanager.v1.[ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html);
         import com.google.cloud.parametermanager.v1.[ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html);
         import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
         import com.google.protobuf.util.[FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html);
         import java.io.IOException;
         
         /**
          * This class demonstrates how to change the kms key of a parameter
          * using theParameter Manager SDK for GCP.
          */
         public class UpdateParamKmsKey {
         
           public static void main(String[] args) throws IOException {
             // TODO(developer): Replace these variables before running the sample.
             String projectId = "your-project-id";
             String parameterId = "your-parameter-id";
             String kmsKeyName = "your-kms-key";
         
             // Call the method to update kms key of a parameter.
             updateParamKmsKey(projectId, parameterId, kmsKeyName);
           }
         
           // This is an example snippet for updating the kms key of a parameter.
           public static [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) updateParamKmsKey(
               String projectId, String parameterId, String kmsKeyName) throws IOException {
             // Initialize the client that will be used to send requests. This client only
             // needs to be created once, and can be reused for multiple requests.
             try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create()) {
               String locationId = "global";
         
               // Build the parameter name.
               [ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html) name = [ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html).of(projectId, locationId, parameterId);
         
               // Set the parameter kms key to update.
               [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) parameter = [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html).newBuilder()
                   .setName(name.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html#com_google_cloud_parametermanager_v1_ParameterName_toString__)())
                   .[setKmsKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.Builder.html#com_google_cloud_parametermanager_v1_Parameter_Builder_setKmsKey_java_lang_String_)(kmsKeyName)
                   .build();
         
               // Build the field mask for the kms_key field.
               [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html).fromString("kms_key");
         
               // Update the parameter kms key.
               [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) updatedParameter = client.updateParameter(parameter, fieldMask);
               System.out.printf(
                   "Updated parameter %s with kms key %s\n",
                   updatedParameter.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html#com_google_cloud_parametermanager_v1_Parameter_getName__)(), updatedParameter.[getKmsKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html#com_google_cloud_parametermanager_v1_Parameter_getKmsKey__)());
         
               return updatedParameter;
             }
           }
         }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Parameter Manager Node.js SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-nodejs). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
         
         /**
          * TODO(developer): Uncomment these variables before running the sample.
          */
         // const projectId = 'YOUR_PROJECT_ID';
         // const parameterId = 'YOUR_PARAMETER_ID';
         // const kmsKey = 'YOUR_KMS_KEY'
         
         // Imports the Parameter Manager library
         const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
         
         // Instantiates a client
         const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)();
         
         async function updateParamKmsKey() {
           const name = client.[parameterPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(projectId, 'global', parameterId);
           const request = {
             parameter: {
               name: name,
               kmsKey: kmsKey,
             },
             updateMask: {
               paths: ['kms_key'],
             },
           };
         
           const [parameter] = await client.updateParameter(request);
           console.log(
             `Updated parameter ${parameter.name} with kms_key ${parameter.kmsKey}`
           );
           return parameter;
         }
         
         return await updateParamKmsKey();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
         
         // Import necessary classes for updating a parameter.
         use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
         use Google\Cloud\ParameterManager\V1\GetParameterRequest;
         use Google\Cloud\ParameterManager\V1\UpdateParameterRequest;
         use Google\Protobuf\FieldMask;
         
         /**
          * Update a parameter with kms key using the Parameter Manager SDK for GCP.
          *
          * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
          * @param string $parameterId The Parameter ID (e.g. 'my-param')
          * @param string $kmsKey The KMS key used to encrypt the parameter (e.g. 'projects/my-project/locations/global/keyRings/test/cryptoKeys/test-key')
          */
         function update_param_kms_key(string $projectId, string $parameterId, string $kmsKey): void
         {
             // Create a client for the Parameter Manager service.
             $client = new ParameterManagerClient();
         
             // Build the resource name of the parameter.
             $parameterName = $client->parameterName($projectId, 'global', $parameterId);
         
             // Prepare the request to get the parameter.
             $request = (new GetParameterRequest())
                 ->setName($parameterName);
         
             // Retrieve the parameter using the client.
             $parameter = $client->getParameter($request);
         
             $parameter->setKmsKey($kmsKey);
         
             $updateMask = (new FieldMask())
                 ->setPaths(['kms_key']);
         
             // Prepare the request to update the parameter.
             $request = (new UpdateParameterRequest())
                 ->setUpdateMask($updateMask)
                 ->setParameter($parameter);
         
             // Update the parameter using the client.
             $updatedParameter = $client->updateParameter($request);
         
             // Print the parameter details.
             printf('Updated parameter %s with kms key %s' . PHP_EOL, $updatedParameter->getName(), $updatedParameter->getKmsKey());
         }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
         
         def update_param_kms_key(
             project_id: str, parameter_id: str, kms_key: str
         ) -> parametermanager_v1.Parameter:
             """
             Update the kms key of a specified global parameter
             in the specified project using the Google Cloud Parameter Manager SDK.
         
             Args:
                 project_id (str): The ID of the project where the parameter is located.
                 parameter_id (str): The ID of the parameter for
                 which kms key is to be updated.
                 kms_key (str): The kms_key to be updated for the parameter.
         
             Returns:
                 parametermanager_v1.Parameter: An object representing the
                 updated parameter.
         
             Example:
                 update_param_kms_key(
                     "my-project",
                     "my-global-parameter",
                     "projects/my-project/locations/global/keyRings/test/cryptoKeys/updated-test-key"
                 )
             """
             # Import the necessary library for Google Cloud Parameter Manager.
             from google.cloud import [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest)
             from google.protobuf import field_mask_pb2
         
             # Create the Parameter Manager client.
             client = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterManagerClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html)()
         
             # Build the resource name of the parameter.
             name = client.[parameter_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_parameter_path)(project_id, "global", parameter_id)
         
             # Get the current parameter details.
             parameter = client.[get_parameter](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_get_parameter)(name=name)
         
             # Set the kms key field of the parameter.
             parameter.kms_key = kms_key
         
             # Define the update mask for the kms_key field.
             update_mask = field_mask_pb2.FieldMask(paths=["kms_key"])
         
             # Define the request to update the parameter.
             request = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[UpdateParameterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.UpdateParameterRequest.html)(
                 parameter=parameter, update_mask=update_mask
             )
         
             # Call the API to update (kms_key) the parameter.
             response = client.[update_parameter](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_update_parameter)(request=request)
         
             # Print the parameter ID that was updated.
             print(f"Updated parameter {parameter_id} with kms key {response.kms_key}")

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
         
         require "google/cloud/parameter_manager"
         
         ##
         # Update the KMS key of a parameter
         #
         # @param project_id [String] The Google Cloud project (e.g. "my-project")
         # @param parameter_id [String] The parameter name (e.g. "my-parameter")
         # @param kms_key [String] The KMS key name
         # (e.g. "projects/my-project/locations/global/keyRings/my-keyring/cryptoKeys/my-key")
         #
         def update_param_kms_key project_id:, parameter_id:, kms_key:
           # Create a Parameter Manager client.
           client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html)
         
           # Build the resource name of the parent project.
           name = client.[parameter_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: "global", parameter: parameter_id
         
           parameter = {
             name: name,
             kms_key: kms_key
           }
         
           update_mask = {
             paths: ["kms_key"]
           }
         
           # Update the parameter.
           param = client.update_parameter parameter: parameter, update_mask: update_mask
         
           # Print the parameter name.
           puts "Updated parameter #{param.name} with kms_key #{param.[kms_key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-Parameter.html)}"
         end

**Regional parameters**

### gcloud

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
         
         gcloud parametermanager parameters update "PARAMETER_ID" \
                  --location "LOCATION" \
                  --kms-key "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/parameter-manager-cmek/cryptoKeys/my-other-key"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
         
         gcloud parametermanager parameters update "PARAMETER_ID" `
                  --location "LOCATION" `
                  --kms-key "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/parameter-manager-cmek/cryptoKeys/my-other-key"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
         
         gcloud parametermanager parameters update "PARAMETER_ID" ^
                  --location "LOCATION" ^
                  --kms-key "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/parameter-manager-cmek/cryptoKeys/my-other-key"

### REST

HTTP method and URL: 
         
         PATCH https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PM_PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID?update_mask=kmsKey

Request JSON body: 
         
         {
           "payload": {
             "kmsKey": "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/parameter-manager-cmek/cryptoKeys/my-other-key"
           }
         }
         

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
         
         curl -X PATCH \  
              -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
              -H "Content-Type: application/json; charset=utf-8" \  
              -d @request.json \  
              "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PM_PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID?update_mask=kmsKey"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
         
         $cred = gcloud auth print-access-token  
         $headers = @{ "Authorization" = "Bearer $cred" }  
           
         Invoke-WebRequest `  
             -Method PATCH `  
             -Headers $headers `  
             -ContentType: "application/json; charset=utf-8" `  
             -InFile request.json `  
             -Uri "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PM_PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID?update_mask=kmsKey" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Parameter Manager Go SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-go). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
         
         import (
         	"context"
         	"fmt"
         	"io"
         
         	parametermanager "cloud.google.com/go/parametermanager/apiv1"
         	parametermanagerpb "cloud.google.com/go/parametermanager/apiv1/parametermanagerpb"
         	"google.golang.org/api/option"
         	"google.golang.org/genproto/protobuf/field_mask"
         )
         
         // updateRegionalParamKmsKey updates a regional parameter kms_key using the Parameter Manager SDK for GCP.
         //
         // w: The io.Writer object used to write the output.
         // projectID: The ID of the project where the parameter is located.
         // locationID: The ID of the location where the parameter is located.
         // parameterID: The ID of the parameter to be updated.
         // kmsKey: The ID of the KMS key to be used for encryption.
         // (e.g. "projects/my-project/locations/us-central1/keyRings/my-key-ring/cryptoKeys/my-encryption-key")
         // (For more information, see: https://cloud.google.com/secret-manager/parameter-manager/docs/cmek)
         //
         // The function returns an error if the parameter creation fails.
         func updateRegionalParamKmsKey(w io.Writer, projectID, locationID, parameterID, kmsKey string) error {
         	// Create a context and a Parameter Manager client.
         	ctx := context.Background()
         
         	// Create a Parameter Manager client.
         	endpoint := fmt.Sprintf("parametermanager.%s.rep.googleapis.com:443", locationID)
         	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx, option.WithEndpoint(endpoint))
         	if err != nil {
         		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
         	}
         	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
         
         	// Construct the name of the create parameter.
         	name := fmt.Sprintf("projects/%s/locations/%s/parameters/%s", projectID, locationID, parameterID)
         
         	// Create a parameter with unformatted format.
         	req := &parametermanagerpb.UpdateParameterRequest{
         		Parameter: &parametermanagerpb.Parameter{
         			Name:   name,
         			Format: parametermanagerpb.[ParameterFormat_UNFORMATTED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1/parametermanagerpb.html#cloud_google_com_go_parametermanager_apiv1_parametermanagerpb_ParameterFormat_PARAMETER_FORMAT_UNSPECIFIED_ParameterFormat_UNFORMATTED_ParameterFormat_YAML_ParameterFormat_JSON),
         			KmsKey: &kmsKey,
         		},
         		UpdateMask: &field_mask.FieldMask{
         			Paths: []string{"kms_key"},
         		},
         	}
         	parameter, err := client.UpdateParameter(ctx, req)
         	if err != nil {
         		return fmt.Errorf("failed to update parameter: %w", err)
         	}
         
         	fmt.Fprintf(w, "Updated regional parameter %s with kms_key %s\n", parameter.Name, *parameter.KmsKey)
         	return nil
         }
         

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
         
         import com.google.cloud.parametermanager.v1.[Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html);
         import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
         import com.google.cloud.parametermanager.v1.[ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html);
         import com.google.cloud.parametermanager.v1.[ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html);
         import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
         import com.google.protobuf.util.[FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html);
         import java.io.IOException;
         
         /**
          * This class demonstrates how to change the kms key of a regional 
          * parameter using the Parameter Manager SDK for GCP.
          */
         public class UpdateRegionalParamKmsKey {
         
           public static void main(String[] args) throws IOException {
             // TODO(developer): Replace these variables before running the sample.
             String projectId = "your-project-id";
             String locationId = "your-location-id";
             String parameterId = "your-parameter-id";
             String kmsKeyName = "your-kms-key";
         
             // Call the method to update kms key of a parameter.
             updateRegionalParamKmsKey(projectId, locationId, parameterId, kmsKeyName);
           }
         
           // This is an example snippet for updating the kms key of a parameter.
           public static [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) updateRegionalParamKmsKey(
               String projectId, String locationId, String parameterId, String kmsKeyName)
               throws IOException {
         
             // Endpoint to call the regional parameter manager server
             String apiEndpoint = String.format("parametermanager.%s.rep.googleapis.com:443", locationId);
             [ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html) parameterManagerSettings =
                 [ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html).newBuilder().setEndpoint(apiEndpoint).build();
         
             // Initialize the client that will be used to send requests. This client only needs to be
             // created once, and can be reused for multiple requests.
             try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create(parameterManagerSettings)) {
         
               // Build the parameter name.
               [ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html) name = [ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html).of(projectId, locationId, parameterId);
         
               // Set the parameter kms key to update.
               [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) parameter = [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html).newBuilder()
                   .setName(name.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html#com_google_cloud_parametermanager_v1_ParameterName_toString__)())
                   .[setKmsKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.Builder.html#com_google_cloud_parametermanager_v1_Parameter_Builder_setKmsKey_java_lang_String_)(kmsKeyName)
                   .build();
         
               // Build the field mask for the kms_key field.
               [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html).fromString("kms_key");
         
               // Update the parameter kms key.
               [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) updatedParameter = client.updateParameter(parameter, fieldMask);
               System.out.printf(
                   "Updated regional parameter %s with kms key %s\n",
                   updatedParameter.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html#com_google_cloud_parametermanager_v1_Parameter_getName__)(), updatedParameter.[getKmsKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html#com_google_cloud_parametermanager_v1_Parameter_getKmsKey__)());
         
               return updatedParameter;
             }
           }
         }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Parameter Manager Node.js SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-nodejs). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
         
         /**
          * TODO(developer): Uncomment these variables before running the sample.
          */
         // const projectId = 'YOUR_PROJECT_ID';
         // const locationId = 'YOUR_LOCATION_ID';
         // const parameterId = 'YOUR_PARAMETER_ID';
         // const kmsKey = 'YOUR_KMS_KEY'
         
         // Imports the Parameter Manager library
         const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
         
         // Adding the endpoint to call the regional parameter manager server
         const options = {
           apiEndpoint: `parametermanager.${locationId}.rep.googleapis.com`,
         };
         
         // Instantiates a client with regional endpoint
         const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)(options);
         
         async function updateRegionalParamKmsKey() {
           const name = client.[parameterPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(projectId, locationId, parameterId);
           const request = {
             parameter: {
               name: name,
               kmsKey: kmsKey,
             },
             updateMask: {
               paths: ['kms_key'],
             },
           };
         
           const [parameter] = await client.updateParameter(request);
           console.log(
             `Updated regional parameter ${parameter.name} with kms_key ${parameter.kmsKey}`
           );
           return parameter;
         }
         
         return await updateRegionalParamKmsKey();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
         
         // Import necessary classes for updating a parameter.
         use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
         use Google\Cloud\ParameterManager\V1\GetParameterRequest;
         use Google\Cloud\ParameterManager\V1\UpdateParameterRequest;
         use Google\Protobuf\FieldMask;
         
         /**
          * Update a parameter with kms key using the Parameter Manager SDK for GCP.
          *
          * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
          * @param string $locationId The Parameter Location (e.g. 'us-central1')
          * @param string $parameterId The Parameter ID (e.g. 'my-param')
          * @param string $kmsKey The KMS key used to encrypt the parameter (e.g. 'projects/my-project/locations/global/keyRings/test/cryptoKeys/test-key')
          */
         function update_regional_param_kms_key(string $projectId, string $locationId, string $parameterId, string $kmsKey): void
         {
             // Specify regional endpoint.
             $options = ['apiEndpoint' => "parametermanager.$locationId.rep.googleapis.com"];
         
             // Create a client for the Parameter Manager service.
             $client = new ParameterManagerClient($options);
         
             // Build the resource name of the parameter.
             $parameterName = $client->parameterName($projectId, $locationId, $parameterId);
         
             // Prepare the request to get the parameter.
             $request = (new GetParameterRequest())
                 ->setName($parameterName);
         
             // Retrieve the parameter using the client.
             $parameter = $client->getParameter($request);
         
             $parameter->setKmsKey($kmsKey);
         
             $updateMask = (new FieldMask())
                 ->setPaths(['kms_key']);
         
             // Prepare the request to update the parameter.
             $request = (new UpdateParameterRequest())
                 ->setUpdateMask($updateMask)
                 ->setParameter($parameter);
         
             // Update the parameter using the client.
             $updatedParameter = $client->updateParameter($request);
         
             // Print the parameter details.
             printf('Updated regional parameter %s with kms key %s' . PHP_EOL, $updatedParameter->getName(), $updatedParameter->getKmsKey());
         }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
         
         def update_regional_param_kms_key(
             project_id: str, location_id: str, parameter_id: str, kms_key: str
         ) -> parametermanager_v1.Parameter:
             """
             Update the kms key of a specified regional parameter
             in the specified project using the Google Cloud Parameter Manager SDK.
         
             Args:
                 project_id (str): The ID of the project where the parameter is to be created.
                 location_id (str): The region where the parameter is to be created.
                 parameter_id (str): The ID of the regional parameter for
                 which kms key is to be updated.
                 kms_key (str): The kms_key to be updated for the parameter.
         
             Returns:
                 parametermanager_v1.Parameter: An object representing the
                 updated regional parameter.
         
             Example:
                 update_regional_param_kms_key(
                     "my-project",
                     "us-central1",
                     "my-regional-parameter",
                     "projects/my-project/locations/us-central1/keyRings/test/cryptoKeys/updated-test-key"
                 )
             """
             # Import the necessary library for Google Cloud Parameter Manager.
             from google.cloud import [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest)
             from google.protobuf import field_mask_pb2
         
             # Create the Parameter Manager client.
             api_endpoint = f"parametermanager.{location_id}.rep.googleapis.com"
             # Create the Parameter Manager client for the specified region.
             client = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterManagerClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html)(
                 client_options={"api_endpoint": api_endpoint}
             )
         
             # Build the resource name of the regional parameter.
             name = client.[parameter_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_parameter_path)(project_id, location_id, parameter_id)
         
             # Get the current regional parameter details.
             parameter = client.[get_parameter](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_get_parameter)(name=name)
         
             # Set the kms key field of the regional parameter.
             parameter.kms_key = kms_key
         
             # Define the update mask for the kms_key field.
             update_mask = field_mask_pb2.FieldMask(paths=["kms_key"])
         
             # Define the request to update the parameter.
             request = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[UpdateParameterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.UpdateParameterRequest.html)(
                 parameter=parameter, update_mask=update_mask
             )
         
             # Call the API to update (kms_key) the parameter.
             response = client.[update_parameter](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_update_parameter)(request=request)
         
             # Print the parameter ID that was updated.
             print(f"Updated regional parameter {parameter_id} with kms key {response.kms_key}")

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
         
         require "google/cloud/parameter_manager"
         
         ##
         # Update the KMS key of a regional parameter
         #
         # @param project_id [String] The Google Cloud project (e.g. "my-project")
         # @param location_id [String] The location name (e.g. "us-central1")
         # @param parameter_id [String] The parameter name (e.g. "my-parameter")
         # @param kms_key [String] The KMS key name
         # (e.g. "projects/my-project/locations/us-central1/keyRings/my-keyring/cryptoKeys/my-key")
         #
         def update_regional_param_kms_key project_id:, location_id:, parameter_id:, kms_key:
           # Endpoint for the regional parameter manager service.
           api_endpoint = "parametermanager.#{location_id}.rep.googleapis.com"
         
           # Create the Parameter Manager client.
           client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html) do |config|
             config.endpoint = api_endpoint
           end
         
           # Build the resource name of the parent project.
           name = client.[parameter_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: location_id, parameter: parameter_id
         
           parameter = {
             name: name,
             kms_key: kms_key
           }
         
           update_mask = {
             paths: ["kms_key"]
           }
         
           # Update the parameter.
           param = client.update_parameter parameter: parameter, update_mask: update_mask
         
           # Print the parameter name.
           puts "Updated regional parameter #{param.name} with kms_key #{param.[kms_key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-Parameter.html)}"
         end


**Warning:** Updating the CMEK configuration only applies to new parameter versions. Existing parameter versions are not re-encrypted. Existing parameter versions can't be accessed if the CMEK key that encrypted it is unavailable. If a key is destroyed, the parameter data is unrecoverable.

## View parameter version CMEK configuration

To inspect the metadata of a parameter version, including whether the parameter version is CMEK-enabled and the resource name of the CMEK key version, run the command to view its metadata.

### gcloud
    
    
    gcloud parametermanager parameters versions describe "PARAMETER_VERSION_ID" \
        --parameter= "PARAMETER_ID" \
        --location= "LOCATION"
        --project "PM_PROJECT_ID"

### API
    
    
    curl "https://parametermanager.<var>LOCATION</var>.rep.googleapis.com/v1/projects/PM_PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID?view=FULL" \
        --request "GET" \
        --header "Authorization: Bearer ACCESS_TOKEN" \
        --header "Content-Type: application/json"

This returns the full Cloud KMS resource name of the key version used to encrypt the parameter version. The output is similar to the following:
    
    
       {
          "name": "projects/PM_PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID",
          "createTime": "2024-10-30T05:27:51.206825427Z",
          "updateTime": "2024-10-30T05:27:51.442194863Z",
          "payload": {
            "data": "YTogYgo="
          }
       "kmsKeyVersion": "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/parameter-manager-cmek/cryptoKeys/my-cmek-key/cryptoKeyVersions/1"
       }
    

## Add a Cloud EKM key to a CMEK policy

This section explains how to incorporate an Cloud EKM key into a CMEK policy for parameter encryption and decryption. As Cloud EKM doesn't support the global multi-region, these keys are limited to regional parameters.

To add a Cloud EKM key to a CMEK policy, follow these steps:

  1. [Create a manually managed Cloud EKM key](https://docs.cloud.google.com/kms/docs/create-external-key#create-manual-internet).
  2. [Configure a CMEK enabled parameter](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/\(/secret-manager/parameter-manager/docs/cmek#configure-cmek-parameter\)) that uses this Cloud EKM key.



## Disable CMEK

To remove CMEK configuration from a parameter, use the following command:

**Global parameters**

### gcloud

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
          gcloud parametermanager parameters update "PARAMETER_ID" --clear-kms-key

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
          gcloud parametermanager parameters update "PARAMETER_ID" --clear-kms-key

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
          gcloud parametermanager parameters update "PARAMETER_ID" --clear-kms-key

### REST

HTTP method and URL: 
    
    
    PATCH https://parametermanager.googleapis.com/v1/projects/PM_PROJECT_ID/locations/parameters/PARAMETER_ID?update_mask=kmsKey

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://parametermanager.googleapis.com/v1/projects/PM_PROJECT_ID/locations/parameters/PARAMETER_ID?update_mask=kmsKey"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -Uri "https://parametermanager.googleapis.com/v1/projects/PM_PROJECT_ID/locations/parameters/PARAMETER_ID?update_mask=kmsKey" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Parameter Manager Go SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-go). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	parametermanager "cloud.google.com/go/parametermanager/apiv1"
    	parametermanagerpb "cloud.google.com/go/parametermanager/apiv1/parametermanagerpb"
    	"google.golang.org/genproto/protobuf/field_mask"
    )
    
    // removeParamKmsKey removes a parameter kms_key using the Parameter Manager SDK for GCP.
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // parameterID: The ID of the parameter to be updated.
    //
    // The function returns an error if the parameter creation fails.
    func removeParamKmsKey(w io.Writer, projectID, parameterID string) error {
    	// Create a context and a Parameter Manager client.
    	ctx := context.Background()
    
    	// Create a Parameter Manager client.
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the create parameter.
    	name := fmt.Sprintf("projects/%s/locations/global/parameters/%s", projectID, parameterID)
    
    	// Create a parameter with unformatted format.
    	req := &parametermanagerpb.UpdateParameterRequest{
    		Parameter: &parametermanagerpb.Parameter{
    			Name:   name,
    			Format: parametermanagerpb.[ParameterFormat_UNFORMATTED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1/parametermanagerpb.html#cloud_google_com_go_parametermanager_apiv1_parametermanagerpb_ParameterFormat_PARAMETER_FORMAT_UNSPECIFIED_ParameterFormat_UNFORMATTED_ParameterFormat_YAML_ParameterFormat_JSON),
    		},
    		UpdateMask: &field_mask.FieldMask{
    			Paths: []string{"kms_key"},
    		},
    	}
    	parameter, err := client.UpdateParameter(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to update parameter: %w", err)
    	}
    
    	fmt.Fprintf(w, "Removed kms_key for parameter %s\n", parameter.Name)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.parametermanager.v1.[Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html);
    import com.google.cloud.parametermanager.v1.[ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.protobuf.util.[FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html);
    import java.io.IOException;
    
    /**
     * This class demonstrates how to change the kms key of a parameter
     * using the Parameter Manager SDK for GCP.
     */
    public class RemoveParamKmsKey {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String parameterId = "your-parameter-id";
    
        // Call the method to remove kms key of a parameter.
        removeParamKmsKey(projectId, parameterId);
      }
    
      // This is an example snippet for updating the kms key of a parameter.
      public static [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) removeParamKmsKey(
          String projectId, String parameterId) throws IOException {
        // Initialize the client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests.
        try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create()) {
          String locationId = "global";
    
          // Build the parameter name.
          [ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html) name = [ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html).of(projectId, locationId, parameterId);
    
          // Remove kms key of a parameter  .
          [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) parameter = [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html).newBuilder()
              .setName(name.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html#com_google_cloud_parametermanager_v1_ParameterName_toString__)())
              .[clearKmsKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.Builder.html#com_google_cloud_parametermanager_v1_Parameter_Builder_clearKmsKey__)()
              .build();
    
          // Build the field mask for the kms_key field.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html).fromString("kms_key");
    
          // Update the parameter kms key.
          [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) updatedParameter = client.updateParameter(parameter, fieldMask);
          System.out.printf(
              "Removed kms key for parameter %s\n",
              updatedParameter.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html#com_google_cloud_parametermanager_v1_Parameter_getName__)());
    
          return updatedParameter;
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Parameter Manager Node.js SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-nodejs). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const parameterId = 'YOUR_PARAMETER_ID';
    
    // Imports the Parameter Manager library
    const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
    
    // Instantiates a client
    const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)();
    
    async function removeParamKmsKey() {
      const name = client.[parameterPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(projectId, 'global', parameterId);
      const request = {
        parameter: {
          name: name,
        },
        updateMask: {
          paths: ['kms_key'],
        },
      };
    
      const [parameter] = await client.updateParameter(request);
      console.log(`Removed kms_key for parameter ${parameter.name}`);
      return parameter;
    }
    
    return await removeParamKmsKey();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for updating a parameter.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\GetParameterRequest;
    use Google\Cloud\ParameterManager\V1\UpdateParameterRequest;
    use Google\Protobuf\FieldMask;
    
    /**
     * Update a parameter by removing kms key using the Parameter Manager SDK for GCP.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     */
    function remove_param_kms_key(string $projectId, string $parameterId): void
    {
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient();
    
        // Build the resource name of the parameter.
        $parameterName = $client->parameterName($projectId, 'global', $parameterId);
    
        // Prepare the request to get the parameter.
        $request = (new GetParameterRequest())
            ->setName($parameterName);
    
        // Retrieve the parameter using the client.
        $parameter = $client->getParameter($request);
    
        $parameter->clearKmsKey();
    
        $updateMask = (new FieldMask())
            ->setPaths(['kms_key']);
    
        // Prepare the request to update the parameter.
        $request = (new UpdateParameterRequest())
            ->setUpdateMask($updateMask)
            ->setParameter($parameter);
    
        // Update the parameter using the client.
        $updatedParameter = $client->updateParameter($request);
    
        // Print the parameter details.
        printf('Removed kms key for parameter %s' . PHP_EOL, $updatedParameter->getName());
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    def remove_param_kms_key(
        project_id: str, parameter_id: str
    ) -> parametermanager_v1.Parameter:
        """
        Remove a kms key of a specified global parameter
        in the specified project using the Google Cloud Parameter Manager SDK.
    
        Args:
            project_id (str): The ID of the project where the parameter is located.
            parameter_id (str): The ID of the parameter for
            which kms key is to be removed.
    
        Returns:
            parametermanager_v1.Parameter: An object representing the
            updated parameter.
    
        Example:
            remove_param_kms_key(
                "my-project",
                "my-global-parameter"
            )
        """
        # Import the necessary library for Google Cloud Parameter Manager.
        from google.cloud import parametermanager_v1
        from google.protobuf import field_mask_pb2
    
        # Create the Parameter Manager client.
        client = parametermanager_v1.ParameterManagerClient()
    
        # Build the resource name of the parameter.
        name = client.parameter_path(project_id, "global", parameter_id)
    
        # Get the current parameter details.
        parameter = client.get_parameter(name=name)
    
        parameter.kms_key = None
    
        # Define the update mask for the kms_key field.
        update_mask = field_mask_pb2.FieldMask(paths=["kms_key"])
    
        # Define the request to update the parameter.
        request = parametermanager_v1.UpdateParameterRequest(
            parameter=parameter, update_mask=update_mask
        )
    
        # Call the API to update (kms_key) the parameter.
        response = client.update_parameter(request=request)
    
        # Print the parameter ID that it was disabled.
        print(f"Removed kms key for parameter {parameter_id}")

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/parameter_manager"
    
    ##
    # Remove the KMS key from a parameter
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    # @param parameter_id [String] The parameter name (e.g. "my-parameter")
    #
    def remove_param_kms_key project_id:, parameter_id:
      # Create a Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html)
    
      # Build the resource name of the parent project.
      name = client.[parameter_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: "global", parameter: parameter_id
    
      parameter = {
        name: name
      }
    
      update_mask = {
        paths: ["kms_key"]
      }
    
      # Update the parameter.
      param = client.update_parameter parameter: parameter, update_mask: update_mask
    
      # Print the parameter name.
      puts "Removed kms_key for parameter #{param.name}"
    end

**Regional parameters**

### gcloud

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
          gcloud parametermanager parameters update "PARAMETER_ID" \
              --location "LOCATION" \
              --clear-kms-key

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
          gcloud parametermanager parameters update "PARAMETER_ID" `
              --location "LOCATION" `
              --clear-kms-key

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
          gcloud parametermanager parameters update "PARAMETER_ID" ^
              --location "LOCATION" ^
              --clear-kms-key

### REST

HTTP method and URL: 
    
    
    PATCH https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PM_PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID?update_mask=kmsKey

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PM_PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID?update_mask=kmsKey"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -Uri "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PM_PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID?update_mask=kmsKey" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Parameter Manager Go SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-go). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	parametermanager "cloud.google.com/go/parametermanager/apiv1"
    	parametermanagerpb "cloud.google.com/go/parametermanager/apiv1/parametermanagerpb"
    	"google.golang.org/api/option"
    	"google.golang.org/genproto/protobuf/field_mask"
    )
    
    // removeRegionalParamKmsKey removes a regional parameter kms_key using the Parameter Manager SDK for GCP.
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // locationID: The ID of the location where the parameter is located.
    // parameterID: The ID of the parameter to be updated.
    //
    // The function returns an error if the parameter creation fails.
    func removeRegionalParamKmsKey(w io.Writer, projectID, locationID, parameterID string) error {
    	// Create a context and a Parameter Manager client.
    	ctx := context.Background()
    
    	// Create a Parameter Manager client.
    	endpoint := fmt.Sprintf("parametermanager.%s.rep.googleapis.com:443", locationID)
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx, option.WithEndpoint(endpoint))
    	if err != nil {
    		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the create parameter.
    	name := fmt.Sprintf("projects/%s/locations/%s/parameters/%s", projectID, locationID, parameterID)
    
    	// Create a parameter with unformatted format.
    	req := &parametermanagerpb.UpdateParameterRequest{
    		Parameter: &parametermanagerpb.Parameter{
    			Name:   name,
    			Format: parametermanagerpb.[ParameterFormat_UNFORMATTED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1/parametermanagerpb.html#cloud_google_com_go_parametermanager_apiv1_parametermanagerpb_ParameterFormat_PARAMETER_FORMAT_UNSPECIFIED_ParameterFormat_UNFORMATTED_ParameterFormat_YAML_ParameterFormat_JSON),
    		},
    		UpdateMask: &field_mask.FieldMask{
    			Paths: []string{"kms_key"},
    		},
    	}
    	parameter, err := client.UpdateParameter(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to update parameter: %w", err)
    	}
    
    	fmt.Fprintf(w, "Removed kms_key for regional parameter %s\n", parameter.Name)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.parametermanager.v1.[Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html);
    import com.google.cloud.parametermanager.v1.[ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.protobuf.util.[FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html);
    import java.io.IOException;
    
    /**
     * This class demonstrates how to change the kms key of a parameter 
     * using the Parameter Manager SDK for GCP.
     */
    public class RemoveRegionalParamKmsKey {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "your-location-id";
        String parameterId = "your-parameter-id";
    
        // Call the method to remove kms key of a parameter.
        removeRegionalParamKmsKey(projectId, locationId, parameterId);
      }
    
      // This is an example snippet for updating the kms key of a parameter.
      public static [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) removeRegionalParamKmsKey(
          String projectId, String locationId, String parameterId) throws IOException {
    
        // Endpoint to call the regional parameter manager server
        String apiEndpoint = String.format("parametermanager.%s.rep.googleapis.com:443", locationId);
        [ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html) parameterManagerSettings =
            [ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html).newBuilder().setEndpoint(apiEndpoint).build();
    
        // Initialize the client that will be used to send requests. This client only needs to be
        // created once, and can be reused for multiple requests.
        try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create(parameterManagerSettings)) {
    
          // Build the parameter name.
          [ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html) name = [ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html).of(projectId, locationId, parameterId);
    
          // Remove kms key of a parameter  .
          [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) parameter = [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html).newBuilder()
              .setName(name.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html#com_google_cloud_parametermanager_v1_ParameterName_toString__)())
              .[clearKmsKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.Builder.html#com_google_cloud_parametermanager_v1_Parameter_Builder_clearKmsKey__)()
              .build();
    
          // Build the field mask for the kms_key field.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html).fromString("kms_key");
    
          // Update the parameter kms key.
          [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) updatedParameter = client.updateParameter(parameter, fieldMask);
          System.out.printf(
              "Removed kms key for regional parameter %s\n",
              updatedParameter.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html#com_google_cloud_parametermanager_v1_Parameter_getName__)());
    
          return updatedParameter;
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Parameter Manager Node.js SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-nodejs). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const locationId = 'YOUR_LOCATION_ID';
    // const parameterId = 'YOUR_PARAMETER_ID';
    
    // Imports the Parameter Manager library
    const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
    
    // Adding the endpoint to call the regional parameter manager server
    const options = {
      apiEndpoint: `parametermanager.${locationId}.rep.googleapis.com`,
    };
    
    // Instantiates a client with regional endpoint
    const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)(options);
    
    async function removeRegionalParamKmsKey() {
      const name = client.[parameterPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(projectId, locationId, parameterId);
      const request = {
        parameter: {
          name: name,
        },
        updateMask: {
          paths: ['kms_key'],
        },
      };
    
      const [parameter] = await client.updateParameter(request);
      console.log(`Removed kms_key for regional parameter ${parameter.name}`);
      return parameter;
    }
    
    return await removeRegionalParamKmsKey();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for updating a parameter.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\GetParameterRequest;
    use Google\Cloud\ParameterManager\V1\UpdateParameterRequest;
    use Google\Protobuf\FieldMask;
    
    /**
     * Update a regional parameter by removing kms key using the Parameter Manager SDK for GCP.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $locationId The Parameter Location (e.g. 'us-central1')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     */
    function remove_regional_param_kms_key(string $projectId, string $locationId, string $parameterId): void
    {
        // Specify regional endpoint.
        $options = ['apiEndpoint' => "parametermanager.$locationId.rep.googleapis.com"];
    
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient($options);
    
        // Build the resource name of the parameter.
        $parameterName = $client->parameterName($projectId, $locationId, $parameterId);
    
        // Prepare the request to get the parameter.
        $request = (new GetParameterRequest())
            ->setName($parameterName);
    
        // Retrieve the parameter using the client.
        $parameter = $client->getParameter($request);
    
        $parameter->clearKmsKey();
    
        $updateMask = (new FieldMask())
            ->setPaths(['kms_key']);
    
        // Prepare the request to update the parameter.
        $request = (new UpdateParameterRequest())
            ->setUpdateMask($updateMask)
            ->setParameter($parameter);
    
        // Update the parameter using the client.
        $updatedParameter = $client->updateParameter($request);
    
        // Print the parameter details.
        printf('Removed kms key for regional parameter %s' . PHP_EOL, $updatedParameter->getName());
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    def remove_regional_param_kms_key(
        project_id: str, location_id: str, parameter_id: str
    ) -> parametermanager_v1.Parameter:
        """
        Remove the kms key of a specified regional parameter
        in the specified project using the Google Cloud Parameter Manager SDK.
    
        Args:
            project_id (str): The ID of the project where the parameter is to be created.
            location_id (str): The region where the parameter is to be created.
            parameter_id (str): The ID of the regional parameter for
            which kms key is to be updated.
    
        Returns:
            parametermanager_v1.Parameter: An object representing the
            updated regional parameter.
    
        Example:
            remove_regional_param_kms_key(
                "my-project",
                "us-central1",
                "my-regional-parameter"
            )
        """
        # Import the necessary library for Google Cloud Parameter Manager.
        from google.cloud import [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest)
        from google.protobuf import field_mask_pb2
    
        # Create the Parameter Manager client.
        api_endpoint = f"parametermanager.{location_id}.rep.googleapis.com"
        # Create the Parameter Manager client for the specified region.
        client = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterManagerClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html)(
            client_options={"api_endpoint": api_endpoint}
        )
    
        # Build the resource name of the regional parameter.
        name = client.[parameter_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_parameter_path)(project_id, location_id, parameter_id)
    
        # Get the current regional parameter details.
        parameter = client.[get_parameter](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_get_parameter)(name=name)
    
        # Set the kms key field of the regional parameter.
        parameter.kms_key = None
    
        # Define the update mask for the kms_key field.
        update_mask = field_mask_pb2.FieldMask(paths=["kms_key"])
    
        # Define the request to update the parameter.
        request = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[UpdateParameterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.UpdateParameterRequest.html)(
            parameter=parameter, update_mask=update_mask
        )
    
        # Call the API to update (kms_key) the parameter.
        response = client.[update_parameter](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_update_parameter)(request=request)
    
        # Print the parameter ID that was updated.
        print(f"Removed kms key for regional parameter {parameter_id}")

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/parameter_manager"
    
    ##
    # Remove the KMS key from a regional parameter
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    # @param location_id [String] The location name (e.g. "us-central1")
    # @param parameter_id [String] The parameter name (e.g. "my-parameter")
    #
    def remove_regional_param_kms_key project_id:, location_id:, parameter_id:
      # Endpoint for the regional parameter manager service.
      api_endpoint = "parametermanager.#{location_id}.rep.googleapis.com"
    
      # Create the Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html) do |config|
        config.endpoint = api_endpoint
      end
    
      # Build the resource name of the parent project.
      name = client.[parameter_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: location_id, parameter: parameter_id
    
      parameter = {
        name: name
      }
    
      update_mask = {
        paths: ["kms_key"]
      }
    
      # Update the parameter.
      param = client.update_parameter parameter: parameter, update_mask: update_mask
    
      # Print the parameter name.
      puts "Removed kms_key for regional parameter #{param.name}"
    end

**Warning:** Removing CMEK configuration only applies to new parameter versions. Existing parameter versions are not affected. Existing parameter versions can't be accessed if the CMEK key that encrypted it is unavailable. If a key is destroyed, the parameter data is unrecoverable.

## Additional information

  * Existing parameters can be updated to use CMEK.
  * Parameters that already use CMEK can have their CMEK keys changed, or removed to revert to Google default encryption.



## Error handling

  * Operations fail if the CMEK key is unavailable or if the service identity lacks the necessary permissions.
  * The parameter version creation fails if the CMEK and parameter are not in the same location.



## What's next

  * Learn more about [CMEK](https://docs.cloud.google.com/kms/docs/cmek).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

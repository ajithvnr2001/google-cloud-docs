---
url: https://docs.cloud.google.com/service-directory/docs/samples/servicedirectory-delete-namespace/
title: Delete namespace \u00a0|\u00a0 Service Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:28.898643+00:00
---

# Delete namespace  |  Service Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/samples/servicedirectory-delete-namespace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Samples ](https://docs.cloud.google.com/service-directory/docs/samples)



#  Delete namespace Stay organized with collections  Save and categorize content based on your preferences. 

Delete a Service Directory namespace.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configure Service Directory](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory)



## Code sample

### C#

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.ServiceDirectory.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.html);
    
    public class DeleteNamespaceSample
    {
        public void DeleteNamespace(
            string projectId = "projectId",
            string locationId = "us-east1",
            string namespaceId = "test-namespace")
        {
            // Create client
            [RegistrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html) registrationServiceClient = [RegistrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html#Google_Cloud_ServiceDirectory_V1_RegistrationServiceClient_Create)();
            // Initialize request argument(s)
            var namespaceName = [NamespaceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.NamespaceName.html).[FromProjectLocationNamespace](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.NamespaceName.html#Google_Cloud_ServiceDirectory_V1_NamespaceName_FromProjectLocationNamespace_System_String_System_String_System_String_)(projectId, locationId, namespaceId);
            registrationServiceClient.[DeleteNamespace](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html#Google_Cloud_ServiceDirectory_V1_RegistrationServiceClient_DeleteNamespace_Google_Cloud_ServiceDirectory_V1_DeleteNamespaceRequest_Google_Api_Gax_Grpc_CallSettings_)(namespaceName);
        }
    }
    

### Go

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    
    	servicedirectory "cloud.google.com/go/servicedirectory/apiv1"
    	sdpb "cloud.google.com/go/servicedirectory/apiv1/servicedirectorypb"
    )
    
    func deleteNamespace(projectID string) error {
    	// projectID := "my-project"
    	location := "us-east4"
    	namespaceID := "golang-test-namespace"
    
    	ctx := context.Background()
    	// Create a registration client.
    	client, err := servicedirectory.[NewRegistrationClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicedirectory/latest/apiv1.html#cloud_google_com_go_servicedirectory_apiv1_RegistrationClient_NewRegistrationClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("ServiceDirectory.NewRegistrationClient: %w", err)
    	}
    
    	defer client.Close()
    	// Delete a Namespace.
    	req := &sdpb.DeleteNamespaceRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/namespaces/%s", projectID, location, namespaceID),
    	}
    	if err := client.DeleteNamespace(ctx, req); err != nil {
    		return fmt.Errorf("DeleteNamespace: %w", err)
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.servicedirectory.v1.[NamespaceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.NamespaceName.html);
    import com.google.cloud.servicedirectory.v1.[RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html);
    import java.io.IOException;
    
    public class NamespacesDelete {
    
      public static void deleteNamespace() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // These variables should refer to an existing Service Directory namespace.
        String projectId = "your-project-id";
        String locationId = "your-region";
        String namespaceId = "your-namespace";
        deleteNamespace(projectId, locationId, namespaceId);
      }
    
      // Delete a namespace.
      public static void deleteNamespace(String projectId, String locationId, String namespaceId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html) client = [RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html).create()) {
    
          // The namespace to delete.
          [NamespaceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.NamespaceName.html) namespaceName = [NamespaceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.NamespaceName.html).of(projectId, locationId, namespaceId);
    
          // Send the request to delete the namespace.
          client.deleteNamespace(namespaceName);
    
          // Log the action.
          System.out.println("Deleted Namespace: " + namespaceName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.NamespaceName.html#com_google_cloud_servicedirectory_v1_NamespaceName_toString__)());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //
    // TODO(developer): Uncomment these variables before running the sample.
    //
    // const projectId = 'my-project';
    // const locationId = 'us-central1';
    // const namespaceId = 'my-namespace';
    
    // Imports the Google Cloud client library
    const {
      RegistrationServiceClient,
    } = require('[@google-cloud/service-directory](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)');
    
    // Creates a client
    const registrationServiceClient = new [RegistrationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)();
    
    // Build the namespace name
    const namespaceName = registrationServiceClient.namespacePath(
      projectId,
      locationId,
      namespaceId
    );
    
    async function deleteNamespace() {
      await registrationServiceClient.deleteNamespace({
        name: namespaceName,
      });
    
      console.log(`Deleted namespace: ${namespaceName}`);
    }
    
    deleteNamespace();

### PHP

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\ServiceDirectory\V1\Client\RegistrationServiceClient;
    use Google\Cloud\ServiceDirectory\V1\DeleteNamespaceRequest;
    
    /**
     * @param string $projectId     Your Cloud project ID
     * @param string $locationId    Your GCP region
     * @param string $namespaceId   Your namespace name
     */
    function delete_namespace(
        string $projectId,
        string $locationId,
        string $namespaceId
    ): void {
        // Instantiate a client.
        $client = new RegistrationServiceClient();
    
        // Run request.
        $namespaceName = RegistrationServiceClient::namespaceName($projectId, $locationId, $namespaceId);
        $deleteNamespaceRequest = (new DeleteNamespaceRequest())
            ->setName($namespaceName);
        $client->deleteNamespace($deleteNamespaceRequest);
    
        // Print results.
        printf('Deleted Namespace: %s' . PHP_EOL, $namespaceName);
    }

### Python

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def delete_namespace(project_id: str, location: str, namespace_id: str) -> bool:
        """Deletes a namespace in the given location.
    
        Args:
            project_id: Your Google Cloud project id.
            location: The Google Cloud region containing the namespace to delete.
            namespace_id: The id for the namespace to delete.
        """
    
        client = servicedirectory_v1.RegistrationServiceClient()
    
        namespace_name = client.namespace_path(project_id, location, namespace_id)
    
        client.delete_namespace(name=namespace_name)
        print(f"Deleted namespace {namespace_name}.")
        return True
    
    

### Ruby

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project   = "Your Google Cloud project ID"
    # location  = "The Google Cloud region containing the namespace"
    # namespace = "The name of the namespace"
    
    require "google/cloud/service_directory"
    
    # Initialize the client
    registration_service = Google::Cloud::[ServiceDirectory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1/latest/Google-Cloud-ServiceDirectory.html).[registration_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory/latest/Google-Cloud-ServiceDirectory.html)
    
    # The path of the namespace
    namespace_name = registration_service.namespace_path(
      project: project, location: location, namespace: namespace
    )
    
    # Use the Service Directory API to delete the namespace
    registration_service.delete_namespace name: namespace_name
    puts "Deleted namespace: #{namespace_name}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=servicedirectory). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

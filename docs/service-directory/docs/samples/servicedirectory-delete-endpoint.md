---
url: https://docs.cloud.google.com/service-directory/docs/samples/servicedirectory-delete-endpoint/
title: Delete endpoint \u00a0|\u00a0 Service Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:28.284809+00:00
---

# Delete endpoint  |  Service Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/samples/servicedirectory-delete-endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Samples ](https://docs.cloud.google.com/service-directory/docs/samples)



#  Delete endpoint Stay organized with collections  Save and categorize content based on your preferences. 

Delete a Service Directory endpoint.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configure Service Directory](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory)



## Code sample

### C#

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.ServiceDirectory.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.html);
    
    public class DeleteEndpointSample
    {
        public void DeleteEndpoint(
            string projectId = "my-project",
            string locationId = "us-east1",
            string namespaceId = "test-namespace",
            string serviceId = "test-service",
            string endpointId = "test-endpoint")
        {
            // Create client
            [RegistrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html) registrationServiceClient = [RegistrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html#Google_Cloud_ServiceDirectory_V1_RegistrationServiceClient_Create)();
            // Initialize request argument(s)
            var endpointName = [EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.EndpointName.html).[FromProjectLocationNamespaceServiceEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.EndpointName.html#Google_Cloud_ServiceDirectory_V1_EndpointName_FromProjectLocationNamespaceServiceEndpoint_System_String_System_String_System_String_System_String_System_String_)(projectId, locationId, namespaceId, serviceId, endpointId);
            registrationServiceClient.[DeleteEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html#Google_Cloud_ServiceDirectory_V1_RegistrationServiceClient_DeleteEndpoint_Google_Cloud_ServiceDirectory_V1_DeleteEndpointRequest_Google_Api_Gax_Grpc_CallSettings_)(endpointName);
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
    
    func deleteEndpoint(projectID string) error {
    	// projectID := "my-project"
    	location := "us-east4"
    	namespaceID := "golang-test-namespace"
    	serviceID := "golang-test-service"
    	endpointID := "golang-test-endpoint"
    
    	ctx := context.Background()
    	// Create a registration client.
    	client, err := servicedirectory.[NewRegistrationClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicedirectory/latest/apiv1.html#cloud_google_com_go_servicedirectory_apiv1_RegistrationClient_NewRegistrationClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("ServiceDirectory.NewRegistrationClient: %w", err)
    	}
    
    	defer client.Close()
    	// Delete an Endpoint
    	req := &sdpb.DeleteEndpointRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/namespaces/%s/services/%s/endpoints/%s", projectID, location, namespaceID, serviceID, endpointID),
    	}
    	if err := client.DeleteEndpoint(ctx, req); err != nil {
    		return fmt.Errorf("DeleteEndpoint: %w", err)
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.servicedirectory.v1.[EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.EndpointName.html);
    import com.google.cloud.servicedirectory.v1.[RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html);
    import java.io.IOException;
    
    public class EndpointsDelete {
    
      public static void deleteEndpoint() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // These variables should refer to an existing Service Directory endpoint.
        String projectId = "your-project-id";
        String locationId = "your-region";
        String namespaceId = "your-namespace";
        String serviceId = "your-service";
        String endpointId = "your-endpoint";
        deleteEndpoint(projectId, locationId, namespaceId, serviceId, endpointId);
      }
    
      // Delete an endpoint.
      public static void deleteEndpoint(
          String projectId, String locationId, String namespaceId, String serviceId, String endpointId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html) client = [RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html).create()) {
    
          // The endpoint to delete.
          [EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.EndpointName.html) endpointName =
              [EndpointName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.EndpointName.html).of(projectId, locationId, namespaceId, serviceId, endpointId);
    
          // Send the request to delete the endpoint.
          client.deleteEndpoint(endpointName);
    
          // Log the action.
          System.out.println("Deleted Endpoint: " + endpointName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.EndpointName.html#com_google_cloud_servicedirectory_v1_EndpointName_toString__)());
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
    // const serviceId = 'my-service';
    // const endpointId = 'my-endpoint';
    
    // Imports the Google Cloud client library
    const {
      RegistrationServiceClient,
    } = require('[@google-cloud/service-directory](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)');
    
    // Creates a client
    const registrationServiceClient = new [RegistrationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)();
    
    // Build the endpoint name
    const endpointName = registrationServiceClient.endpointPath(
      projectId,
      locationId,
      namespaceId,
      serviceId,
      endpointId
    );
    
    async function deleteEndpoint() {
      await registrationServiceClient.deleteEndpoint({
        name: endpointName,
      });
    
      console.log(`Deleted endpoint: ${endpointName}`);
    }
    
    deleteEndpoint();

### PHP

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\ServiceDirectory\V1\Client\RegistrationServiceClient;
    use Google\Cloud\ServiceDirectory\V1\DeleteEndpointRequest;
    
    /**
     * @param string $projectId     Your Cloud project ID
     * @param string $locationId    Your GCP region
     * @param string $namespaceId   Your namespace name
     * @param string $serviceId     Your service name
     * @param string $endpointId    Your endpoint name
     */
    function delete_endpoint(
        string $projectId,
        string $locationId,
        string $namespaceId,
        string $serviceId,
        string $endpointId
    ): void {
        // Instantiate a client.
        $client = new RegistrationServiceClient();
    
        // Run request.
        $endpointName = RegistrationServiceClient::endpointName($projectId, $locationId, $namespaceId, $serviceId, $endpointId);
        $deleteEndpointRequest = (new DeleteEndpointRequest())
            ->setName($endpointName);
        $client->deleteEndpoint($deleteEndpointRequest);
    
        // Print results.
        printf('Deleted Endpoint: %s' . PHP_EOL, $endpointName);
    }

### Python

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def delete_endpoint(
        project_id: str,
        location: str,
        namespace_id: str,
        service_id: str,
        endpoint_id: str,
    ) -> bool:
        """Deletes a endpoint in the given service.
    
        Args:
            project_id: Your Google Cloud project id.
            location: The Google Cloud region containing the namespace.
            namespace_id: The id of the parent namespace.
            service_id: The id of the parent service.
            endpoint_id: The id of the endpoint to delete.
        """
    
        client = servicedirectory_v1.RegistrationServiceClient()
    
        endpoint_name = client.endpoint_path(
            project_id, location, namespace_id, service_id, endpoint_id
        )
    
        client.delete_endpoint(name=endpoint_name)
        print(f"Deleted endpoint {endpoint_name}.")
        return True
    
    

### Ruby

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project   = "Your Google Cloud project ID"
    # location  = "The Google Cloud region containing the namespace"
    # namespace = "The name of the parent namespace"
    # service   = "The name of the parent service"
    # endpoint  = "The name of the endpoint"
    
    require "google/cloud/service_directory"
    
    # Initialize the client
    registration_service = Google::Cloud::[ServiceDirectory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1/latest/Google-Cloud-ServiceDirectory.html).[registration_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory/latest/Google-Cloud-ServiceDirectory.html)
    
    # The path of the endpoint
    endpoint_path = registration_service.endpoint_path(
      project:   project,
      location:  location,
      namespace: namespace,
      service:   service,
      endpoint:  endpoint
    )
    
    # Use the Service Directory API to delete the endpoint
    registration_service.delete_endpoint name: endpoint_path
    puts "Deleted endpoint: #{endpoint_path}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=servicedirectory). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

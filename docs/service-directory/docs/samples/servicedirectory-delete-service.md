---
url: https://docs.cloud.google.com/service-directory/docs/samples/servicedirectory-delete-service/
title: Delete service \u00a0|\u00a0 Service Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:27.972602+00:00
---

# Delete service  |  Service Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/samples/servicedirectory-delete-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Samples ](https://docs.cloud.google.com/service-directory/docs/samples)



#  Delete service Stay organized with collections  Save and categorize content based on your preferences. 

Delete a Service Directory service.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configure Service Directory](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory)



## Code sample

### C#

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.ServiceDirectory.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.html);
    
    public class DeleteServiceSample
    {
        public void DeleteService(
            string projectId = "my-project",
            string locationId = "us-east1",
            string namespaceId = "test-namespace",
            string serviceId = "test-service")
        {
            // Create client
            [RegistrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html) registrationServiceClient = [RegistrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html#Google_Cloud_ServiceDirectory_V1_RegistrationServiceClient_Create)();
            // Initialize request argument(s)
            var serviceName = [ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.ServiceName.html).[FromProjectLocationNamespaceService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.ServiceName.html#Google_Cloud_ServiceDirectory_V1_ServiceName_FromProjectLocationNamespaceService_System_String_System_String_System_String_System_String_)(projectId, locationId, namespaceId, serviceId);
            registrationServiceClient.[DeleteService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html#Google_Cloud_ServiceDirectory_V1_RegistrationServiceClient_DeleteService_Google_Cloud_ServiceDirectory_V1_DeleteServiceRequest_Google_Api_Gax_Grpc_CallSettings_)(serviceName);
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
    
    func deleteService(projectID string) error {
    	// projectID := "my-project"
    	location := "us-east4"
    	namespaceID := "golang-test-namespace"
    	serviceID := "golang-test-service"
    
    	ctx := context.Background()
    	// Create a registration client.
    	client, err := servicedirectory.[NewRegistrationClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicedirectory/latest/apiv1.html#cloud_google_com_go_servicedirectory_apiv1_RegistrationClient_NewRegistrationClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("ServiceDirectory.NewRegistrationClient: %w", err)
    	}
    
    	defer client.Close()
    	// Delete a service
    	req := &sdpb.DeleteServiceRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/namespaces/%s/services/%s", projectID, location, namespaceID, serviceID),
    	}
    	if err := client.DeleteService(ctx, req); err != nil {
    		return fmt.Errorf("DeleteService: %w", err)
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.servicedirectory.v1.[RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html);
    import com.google.cloud.servicedirectory.v1.[ServiceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ServiceName.html);
    import java.io.IOException;
    
    public class ServicesDelete {
    
      public static void deleteService() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // These variables should refer to an existing Service Directory service.
        String projectId = "your-project-id";
        String locationId = "your-region";
        String namespaceId = "your-namespace";
        String serviceId = "your-service";
        deleteService(projectId, locationId, namespaceId, serviceId);
      }
    
      // Delete a service.
      public static void deleteService(
          String projectId, String locationId, String namespaceId, String serviceId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html) client = [RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html).create()) {
    
          // The service to delete.
          [ServiceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ServiceName.html) serviceName = [ServiceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ServiceName.html).of(projectId, locationId, namespaceId, serviceId);
    
          // Send the request to delete the service.
          client.deleteService(serviceName);
    
          // Log the action.
          System.out.println("Deleted Service: " + serviceName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ServiceName.html#com_google_cloud_servicedirectory_v1_ServiceName_toString__)());
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
    
    // Imports the Google Cloud client library
    const {
      RegistrationServiceClient,
    } = require('[@google-cloud/service-directory](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)');
    
    // Creates a client
    const registrationServiceClient = new [RegistrationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)();
    
    // Build the service name
    const serviceName = registrationServiceClient.servicePath(
      projectId,
      locationId,
      namespaceId,
      serviceId
    );
    
    async function deleteService() {
      await registrationServiceClient.deleteService({
        name: serviceName,
      });
    
      console.log(`Deleted service: ${serviceName}`);
    }
    
    deleteService();

### PHP

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\ServiceDirectory\V1\Client\RegistrationServiceClient;
    use Google\Cloud\ServiceDirectory\V1\DeleteServiceRequest;
    
    /**
     * @param string $projectId     Your Cloud project ID
     * @param string $locationId    Your GCP region
     * @param string $namespaceId   Your namespace name
     * @param string $serviceId     Your service name
     */
    function delete_service(
        string $projectId,
        string $locationId,
        string $namespaceId,
        string $serviceId
    ): void {
        // Instantiate a client.
        $client = new RegistrationServiceClient();
    
        // Run request.
        $serviceName = RegistrationServiceClient::serviceName($projectId, $locationId, $namespaceId, $serviceId);
        $deleteServiceRequest = (new DeleteServiceRequest())
            ->setName($serviceName);
        $client->deleteService($deleteServiceRequest);
    
        // Print results.
        printf('Deleted Service: %s' . PHP_EOL, $serviceName);
    }

### Python

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def delete_service(
        project_id: str, location: str, namespace_id: str, service_id: str
    ) -> bool:
        """Deletes a service in the given namespace.
    
        Args:
            project_id: Your Google Cloud project id.
            location: The Google Cloud region containing the namespace.
            namespace_id: The id of the parent namespace.
            service_id: The id of the service to delete.
        """
    
        client = servicedirectory_v1.RegistrationServiceClient()
    
        service_name = client.service_path(project_id, location, namespace_id, service_id)
    
        client.delete_service(name=service_name)
        print(f"Deleted service {service_name}.")
        return True
    
    

### Ruby

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project   = "Your Google Cloud project ID"
    # location  = "The Google Cloud region containing the namespace"
    # namespace = "The name of the parent namespace"
    # service   = "The name of the service"
    
    require "google/cloud/service_directory"
    
    # Initialize the client
    registration_service = Google::Cloud::[ServiceDirectory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1/latest/Google-Cloud-ServiceDirectory.html).[registration_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory/latest/Google-Cloud-ServiceDirectory.html)
    
    # The path of the service
    service_path = registration_service.service_path(
      project:   project,
      location:  location,
      namespace: namespace,
      service:   service
    )
    
    # Use the Service Directory API to delete the service
    registration_service.delete_service name: service_path
    puts "Deleted service: #{service_path}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=servicedirectory). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

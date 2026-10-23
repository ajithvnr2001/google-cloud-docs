---
url: https://docs.cloud.google.com/service-directory/docs/samples/servicedirectory-create-service/
title: Create service \u00a0|\u00a0 Service Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:27.795934+00:00
---

# Create service  |  Service Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/samples/servicedirectory-create-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Samples ](https://docs.cloud.google.com/service-directory/docs/samples)



#  Create service Stay organized with collections  Save and categorize content based on your preferences. 

Create a Service Directory service.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configure Service Directory](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory)



## Code sample

### C#

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.ServiceDirectory.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.html);
    
    public class CreateServiceSample
    {
        public Service CreateService(
            string projectId = "my-project",
            string locationId = "us-east1",
            string namespaceId = "test-namespace",
            string serviceId = "test-service")
        {
            // Create client
            [RegistrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html) registrationServiceClient = [RegistrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html#Google_Cloud_ServiceDirectory_V1_RegistrationServiceClient_Create)();
            // Initialize request argument(s)
            var namespaceName = [NamespaceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.NamespaceName.html).[FromProjectLocationNamespace](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.NamespaceName.html#Google_Cloud_ServiceDirectory_V1_NamespaceName_FromProjectLocationNamespace_System_String_System_String_System_String_)(projectId, locationId, namespaceId);
            return registrationServiceClient.[CreateService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html#Google_Cloud_ServiceDirectory_V1_RegistrationServiceClient_CreateService_Google_Cloud_ServiceDirectory_V1_CreateServiceRequest_Google_Api_Gax_Grpc_CallSettings_)(namespaceName, new Service(), serviceId);
        }
    }
    
    

### Go

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	servicedirectory "cloud.google.com/go/servicedirectory/apiv1"
    	sdpb "cloud.google.com/go/servicedirectory/apiv1/servicedirectorypb"
    )
    
    func createService(w io.Writer, projectID string) error {
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
    	// Create a Service.
    	req := &sdpb.CreateServiceRequest{
    		Parent:    fmt.Sprintf("projects/%s/locations/%s/namespaces/%s", projectID, location, namespaceID),
    		ServiceId: serviceID,
    		Service: &sdpb.Service{
    			Annotations: map[string]string{
    				"key1": "value1",
    				"key2": "value2",
    			},
    		},
    	}
    	service, err := client.CreateService(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateSerice: %w", err)
    	}
    	fmt.Fprintf(w, "servicedirectory.Createservice result %s\n", service.Name)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.servicedirectory.v1.[NamespaceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.NamespaceName.html);
    import com.google.cloud.servicedirectory.v1.[RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html);
    import com.google.cloud.servicedirectory.v1.[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Service.html);
    import java.io.IOException;
    
    public class ServicesCreate {
    
      public static void createService() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // These variables should refer to an existing Service Directory namespace.
        String projectId = "your-project-id";
        String locationId = "your-region";
        String namespaceId = "your-namespace";
        // This is user-created; must be unique within the namespace above.
        String serviceId = "your-service";
        createService(projectId, locationId, namespaceId, serviceId);
      }
    
      // Create a new service.
      public static void createService(
          String projectId, String locationId, String namespaceId, String serviceId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html) client = [RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html).create()) {
    
          // The namespace to create the service in.
          [NamespaceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.NamespaceName.html) parent = [NamespaceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.NamespaceName.html).of(projectId, locationId, namespaceId);
    
          // The service object to create.
          // Optionally add some annotations for the service.
          [Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Service.html) service = [Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Service.html).newBuilder().putAnnotations("protocol", "tcp").build();
    
          // Send the request to create the namespace.
          [Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Service.html) createdService = client.createService(parent, service, serviceId);
    
          // Process the response.
          System.out.println("Created Service: " + createdService.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Service.html#com_google_cloud_servicedirectory_v1_Service_getName__)());
          System.out.println("Annotations: " + createdService.[getAnnotationsMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Service.html#com_google_cloud_servicedirectory_v1_Service_getAnnotationsMap__)());
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
    
    // Build the namespace name
    const namespaceName = registrationServiceClient.namespacePath(
      projectId,
      locationId,
      namespaceId
    );
    
    async function createService() {
      const [service] = await registrationServiceClient.createService({
        parent: namespaceName,
        serviceId: serviceId,
      });
    
      console.log(`Created service: ${service.name}`);
      return service;
    }
    
    return createService();

### PHP

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\ServiceDirectory\V1\Client\RegistrationServiceClient;
    use Google\Cloud\ServiceDirectory\V1\CreateServiceRequest;
    use Google\Cloud\ServiceDirectory\V1\Service;
    
    /**
     * @param string $projectId Your Cloud project ID
     * @param string $locationId Your GCP region
     * @param string $namespaceId Your namespace name
     * @param string $serviceId Your service name
     */
    function create_service(
        string $projectId,
        string $locationId,
        string $namespaceId,
        string $serviceId
    ): void {
        // Instantiate a client.
        $client = new RegistrationServiceClient();
    
        // Run request.
        $namespaceName = RegistrationServiceClient::namespaceName($projectId, $locationId, $namespaceId);
        $createServiceRequest = (new CreateServiceRequest())
            ->setParent($namespaceName)
            ->setServiceId($serviceId)
            ->setService(new Service());
        $service = $client->createService($createServiceRequest);
    
        // Print results.
        printf('Created Service: %s' . PHP_EOL, $service->getName());
    }

### Python

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def create_service(
        project_id: str, location: str, namespace_id: str, service_id: str
    ) -> Service:
        """Creates a service in the given namespace.
    
        Args:
            project_id: Your Google Cloud project id.
            location: The Google Cloud region containing the namespace.
            namespace_id: The id of the parent namespace.
            service_id: The id of the service you are creating. Service names must be unique within a namespace and follow
                conventions for DNS labels.
    
        Returns:
            The created service.
        """
    
        client = servicedirectory_v1.RegistrationServiceClient()
    
        service = servicedirectory_v1.Service(
            name=client.service_path(project_id, location, namespace_id, service_id)
        )
    
        response = client.create_service(
            parent=client.namespace_path(project_id, location, namespace_id),
            service=service,
            service_id=service_id,
        )
    
        print(f"Created service {response.name}.")
    
        return response
    
    

### Ruby

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project   = "Your Google Cloud project ID"
    # location  = "The Google Cloud region containing the namespace"
    # namespace = "The name of the parent namespace"
    # service   = "The name of the service you are creating"
    
    require "google/cloud/service_directory"
    
    # Initialize the client
    registration_service = Google::Cloud::[ServiceDirectory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1/latest/Google-Cloud-ServiceDirectory.html).[registration_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory/latest/Google-Cloud-ServiceDirectory.html)
    
    # The parent path of the service
    parent = registration_service.namespace_path(
      project: project, location: location, namespace: namespace
    )
    
    # Use the Service Directory API to create the service
    response = registration_service.create_service parent: parent, service_id: service
    puts "Created service: #{response.name}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=servicedirectory). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

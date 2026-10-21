---
url: https://docs.cloud.google.com/service-directory/docs/samples/servicedirectory-create-endpoint/
title: Create endpoint \u00a0|\u00a0 Service Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:14.077445+00:00
---

# Create endpoint  |  Service Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/samples/servicedirectory-create-endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Samples ](https://docs.cloud.google.com/service-directory/docs/samples)



#  Create endpoint Stay organized with collections  Save and categorize content based on your preferences. 

Create a Service Directory endpoint.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configure Service Directory](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory)



## Code sample

### C#

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.ServiceDirectory.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.html);
    
    public class CreateEndpointSample
    {
    	public Endpoint CreateEndpoint(
            string projectId = "my-project",
            string locationId = "us-east1",
            string namespaceId = "test-namespace",
            string serviceId = "test-service",
            string endpointId = "test-endpoint")
        {
            [RegistrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html) registrationServiceClient = [RegistrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html#Google_Cloud_ServiceDirectory_V1_RegistrationServiceClient_Create)();
            var serviceName = [ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.ServiceName.html).[FromProjectLocationNamespaceService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.ServiceName.html#Google_Cloud_ServiceDirectory_V1_ServiceName_FromProjectLocationNamespaceService_System_String_System_String_System_String_System_String_)(projectId, locationId, namespaceId, serviceId);
            return registrationServiceClient.[CreateEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html#Google_Cloud_ServiceDirectory_V1_RegistrationServiceClient_CreateEndpoint_Google_Cloud_ServiceDirectory_V1_CreateEndpointRequest_Google_Api_Gax_Grpc_CallSettings_)(serviceName, new [Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.Endpoint.html)(), endpointId);
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
    
    func createEndpoint(w io.Writer, projectID string) error {
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
    	// Create an Endpoint.
    	req := &sdpb.CreateEndpointRequest{
    		Parent:     fmt.Sprintf("projects/%s/locations/%s/namespaces/%s/services/%s", projectID, location, namespaceID, serviceID),
    		EndpointId: endpointID,
    		Endpoint: &sdpb.Endpoint{
    			Address: "8.8.8.8",
    			Port:    8080,
    			Annotations: map[string]string{
    				"key1": "value1",
    				"key2": "value2",
    			},
    		},
    	}
    	endpoint, err := client.CreateEndpoint(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateEndpoint: %w", err)
    	}
    	fmt.Fprintf(w, "servicedirectory.CreateEndpoint result: %s", endpoint.Name)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.servicedirectory.v1.[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint.html);
    import com.google.cloud.servicedirectory.v1.[RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html);
    import com.google.cloud.servicedirectory.v1.[ServiceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ServiceName.html);
    import java.io.IOException;
    
    public class EndpointsCreate {
    
      public static void createEndpoint() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // These variables should refer to an existing Service Directory service.
        String projectId = "your-project-id";
        String locationId = "your-region";
        String namespaceId = "your-namespace";
        String serviceId = "your-service";
        // This is user-created; must be unique within the service above.
        String endpointId = "your-endpoint";
        createEndpoint(projectId, locationId, namespaceId, serviceId, endpointId);
      }
    
      // Create a new endpoint.
      public static void createEndpoint(
          String projectId, String locationId, String namespaceId, String serviceId, String endpointId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html) client = [RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html).create()) {
    
          // The service to create the endpoint in.
          [ServiceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ServiceName.html) parent = [ServiceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ServiceName.html).of(projectId, locationId, namespaceId, serviceId);
    
          // The endpoint to create, with fields filled in.
          // Optionally set an IP address and port for the endpoint.
          [Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint.html) endpoint = [Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint.html).newBuilder().[setAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint.Builder.html#com_google_cloud_servicedirectory_v1_Endpoint_Builder_setAddress_java_lang_String_)("10.0.0.1").[setPort](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint.Builder.html#com_google_cloud_servicedirectory_v1_Endpoint_Builder_setPort_int_)(443).build();
    
          // Send the request to create the endpoint.
          [Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint.html) createdEndpoint = client.createEndpoint(parent, endpoint, endpointId);
    
          // Process the response.
          System.out.println("Created Endpoint: " + createdEndpoint.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint.html#com_google_cloud_servicedirectory_v1_Endpoint_getName__)());
          System.out.println("IP Address: " + createdEndpoint.[getAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint.html#com_google_cloud_servicedirectory_v1_Endpoint_getAddress__)());
          System.out.println("Port: " + createdEndpoint.[getPort](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint.html#com_google_cloud_servicedirectory_v1_Endpoint_getPort__)());
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
    
    // Build the service name
    const serviceName = registrationServiceClient.servicePath(
      projectId,
      locationId,
      namespaceId,
      serviceId
    );
    
    async function createEndpoint() {
      const [endpoint] = await registrationServiceClient.createEndpoint({
        parent: serviceName,
        endpointId: endpointId,
        endpoint: {address: '10.0.0.1', port: 8080},
      });
    
      console.log(`Created endpoint: ${endpoint.name}`);
      return endpoint;
    }
    
    return createEndpoint();

### PHP

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\ServiceDirectory\V1\Client\RegistrationServiceClient;
    use Google\Cloud\ServiceDirectory\V1\CreateEndpointRequest;
    use Google\Cloud\ServiceDirectory\V1\Endpoint;
    
    /**
     * @param string $projectId     Your Cloud project ID
     * @param string $locationId    Your GCP region
     * @param string $namespaceId   Your namespace name
     * @param string $serviceId     Your service name
     * @param string $endpointId    Your endpoint name
     * @param string $ip            (Optional) Defaults to ''
     * @param int    $port          (Optional) Defaults to 0
     */
    function create_endpoint(
        string $projectId,
        string $locationId,
        string $namespaceId,
        string $serviceId,
        string $endpointId,
        string $ip = '',
        int $port = 0
    ): void {
        // Instantiate a client.
        $client = new RegistrationServiceClient();
    
        // Construct Endpoint object.
        $endpointObject = (new Endpoint())
            ->setAddress($ip)
            ->setPort($port);
    
        // Run request.
        $serviceName = RegistrationServiceClient::serviceName($projectId, $locationId, $namespaceId, $serviceId);
        $createEndpointRequest = (new CreateEndpointRequest())
            ->setParent($serviceName)
            ->setEndpointId($endpointId)
            ->setEndpoint($endpointObject);
        $endpoint = $client->createEndpoint($createEndpointRequest);
    
        // Print results.
        printf('Created Endpoint: %s' . PHP_EOL, $endpoint->getName());
        printf('  IP: %s' . PHP_EOL, $endpoint->getAddress());
        printf('  Port: %d' . PHP_EOL, $endpoint->getPort());
    }

### Python

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def create_endpoint(
        project_id: str,
        location: str,
        namespace_id: str,
        service_id: str,
        endpoint_id: str,
        address: str,
        port: str,
    ) -> Endpoint:
        """Creates a endpoint in the given service.
    
        An endpoint consists of a unique name, an optional IP address and a port, and key-value annotations.
    
        Args:
            project_id: Your Google Cloud project id.
            location: The Google Cloud region containing the namespace.
            namespace_id: The id of the parent namespace.
            service_id: The id of the parent service.
            endpoint_id: A name for the endpoint you are creating.
            address: IP address for the endpoint.
            port: Port number for the endpoint.
    
        Returns:
            The created endpoint.
        """
    
        client = servicedirectory_v1.RegistrationServiceClient()
    
        endpoint = servicedirectory_v1.Endpoint(
            name=client.endpoint_path(
                project_id, location, namespace_id, service_id, endpoint_id
            ),
            address=address,
            port=port,
        )
    
        response = client.create_endpoint(
            parent=client.service_path(project_id, location, namespace_id, service_id),
            endpoint=endpoint,
            endpoint_id=endpoint_id,
        )
    
        print(f"Created endpoint {response.name}.")
    
        return response
    
    

### Ruby

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project   = "Your Google Cloud project ID"
    # location  = "The Google Cloud region containing the namespace"
    # namespace = "The name of the parent namespace"
    # service   = "The name of the parent service"
    # endpoint  = "The name of the endpoint you are creating"
    
    require "google/cloud/service_directory"
    
    # Initialize the client
    registration_service = Google::Cloud::[ServiceDirectory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1/latest/Google-Cloud-ServiceDirectory.html).[registration_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory/latest/Google-Cloud-ServiceDirectory.html)
    
    # The parent path of the endpoint
    parent = registration_service.service_path(
      project:   project,
      location:  location,
      namespace: namespace,
      service:   service
    )
    
    # Set the IP Address and Port on the Endpoint
    endpoint_data = Google::Cloud::[ServiceDirectory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1/latest/Google-Cloud-ServiceDirectory.html)::[V1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1/latest/Google-Cloud-ServiceDirectory-V1.html)::Endpoint.new(
      address: "10.0.0.1",
      port:    443
    )
    
    # Use the Service Directory API to create the endpoint
    response = registration_service.create_endpoint(
      parent: parent, endpoint_id: endpoint, endpoint: endpoint_data
    )
    puts "Created endpoint: #{response.name}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=servicedirectory). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

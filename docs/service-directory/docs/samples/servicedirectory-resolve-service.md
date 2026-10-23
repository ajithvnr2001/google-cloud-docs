---
url: https://docs.cloud.google.com/service-directory/docs/samples/servicedirectory-resolve-service/
title: Resolve service \u00a0|\u00a0 Service Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:28.136133+00:00
---

# Resolve service  |  Service Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/samples/servicedirectory-resolve-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Samples ](https://docs.cloud.google.com/service-directory/docs/samples)



#  Resolve service Stay organized with collections  Save and categorize content based on your preferences. 

Resolve a Service Directory service.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configure Service Directory](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory)



## Code sample

### C#

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.ServiceDirectory.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.html);
    
    public class ResolveServiceSample
    {
        public Service ResolveService(
            string projectId = "my-project",
            string locationId = "us-east1",
            string namespaceId = "test-namespace",
            string serviceId = "test-service")
        {
            // Create client
            [LookupServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.LookupServiceClient.html) lookupServiceClient = [LookupServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.LookupServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.LookupServiceClient.html#Google_Cloud_ServiceDirectory_V1_LookupServiceClient_Create)();
            // Initialize request argument(s)
            [ResolveServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.ResolveServiceRequest.html) request = new [ResolveServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.ResolveServiceRequest.html)
            {
                ServiceName = [ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.ServiceName.html).[FromProjectLocationNamespaceService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.ServiceName.html#Google_Cloud_ServiceDirectory_V1_ServiceName_FromProjectLocationNamespaceService_System_String_System_String_System_String_System_String_)(projectId, locationId, namespaceId, serviceId),
            };
            // Make the request
            [ResolveServiceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.ResolveServiceResponse.html) response = lookupServiceClient.[ResolveService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.LookupServiceClient.html#Google_Cloud_ServiceDirectory_V1_LookupServiceClient_ResolveService_Google_Cloud_ServiceDirectory_V1_ResolveServiceRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
            return response.[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.ResolveServiceResponse.html#Google_Cloud_ServiceDirectory_V1_ResolveServiceResponse_Service);
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
    
    func resolveService(w io.Writer, projectID string) error {
    	// projectID := "my-project"
    	location := "us-east4"
    	namespaceID := "golang-test-namespace"
    	serviceID := "golang-test-service"
    
    	ctx := context.Background()
    	// Create a lookup client.
    	resolver, err := servicedirectory.[NewLookupClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicedirectory/latest/apiv1.html#cloud_google_com_go_servicedirectory_apiv1_LookupClient_NewLookupClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("ServiceDirectory.NewLookupClient: %w", err)
    	}
    
    	defer resolver.Close()
    	// Now Resolve the service.
    	req := &sdpb.ResolveServiceRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/namespaces/%s/services/%s", projectID, location, namespaceID, serviceID),
    	}
    	result, err := resolver.ResolveService(ctx, req)
    	if err != nil {
    		return fmt.Errorf("ResolveService: %w", err)
    	}
    
    	fmt.Fprintf(w, "Successfully Resolved Service %v\n", result)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.servicedirectory.v1.[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint.html);
    import com.google.cloud.servicedirectory.v1.[LookupServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.LookupServiceClient.html);
    import com.google.cloud.servicedirectory.v1.[ResolveServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ResolveServiceRequest.html);
    import com.google.cloud.servicedirectory.v1.[ResolveServiceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ResolveServiceResponse.html);
    import com.google.cloud.servicedirectory.v1.[ServiceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ServiceName.html);
    import java.io.IOException;
    
    public class ServicesResolve {
    
      public static void resolveService() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // These variables should refer to an existing Service Directory service.
        String projectId = "your-project-id";
        String locationId = "your-region";
        String namespaceId = "your-namespace";
        String serviceId = "your-service";
        resolveService(projectId, locationId, namespaceId, serviceId);
      }
    
      // Resolve a service.
      public static void resolveService(
          String projectId, String locationId, String namespaceId, String serviceId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([LookupServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.LookupServiceClient.html) client = [LookupServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.LookupServiceClient.html).create()) {
          // The service to resolve.
          [ServiceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ServiceName.html) name = [ServiceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ServiceName.html).of(projectId, locationId, namespaceId, serviceId);
    
          // Construct the resolve request to be sent to the client.
          [ResolveServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ResolveServiceRequest.html) request =
              [ResolveServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ResolveServiceRequest.html).newBuilder().setName(name.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ServiceName.html#com_google_cloud_servicedirectory_v1_ServiceName_toString__)()).build();
    
          // Send the request to resolve the service.
          [ResolveServiceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ResolveServiceResponse.html) resolveResponse = client.resolveService(request);
    
          // Process the response.
          System.out.println("Resolved Service: " + resolveResponse.[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ResolveServiceResponse.html#com_google_cloud_servicedirectory_v1_ResolveServiceResponse_getService__)().getName());
    
          System.out.println("Endpoints found:");
          for ([Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Endpoint.html) endpoint : resolveResponse.[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.ResolveServiceResponse.html#com_google_cloud_servicedirectory_v1_ResolveServiceResponse_getService__)().getEndpointsList()) {
            System.out.println(
                endpoint.getName() + " -- " + endpoint.getAddress() + ":" + endpoint.getPort());
          }
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
    const {LookupServiceClient} = require('[@google-cloud/service-directory](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)');
    
    // Creates a client
    const lookupServiceClient = new [LookupServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)();
    
    // Build the service name
    const serviceName = lookupServiceClient.servicePath(
      projectId,
      locationId,
      namespaceId,
      serviceId
    );
    
    async function resolveService() {
      const [response] = await lookupServiceClient.resolveService({
        name: serviceName,
      });
    
      console.log(`Resolved service: ${response.service.name}`);
      for (const e of response.service.endpoints) {
        console.log(`\n${e.name}`);
        console.log(`Address: ${e.address}`);
        console.log(`Port: ${e.port}\n`);
      }
      return response.service;
    }
    
    return resolveService();

### PHP

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\ServiceDirectory\V1\Client\LookupServiceClient;
    use Google\Cloud\ServiceDirectory\V1\ResolveServiceRequest;
    use Google\Cloud\ServiceDirectory\V1\Service;
    
    /**
     * @param string $projectId     Your Cloud project ID
     * @param string $locationId    Your GCP region
     * @param string $namespaceId   Your namespace name
     * @param string $serviceId     Your service name
     */
    function resolve_service(
        string $projectId,
        string $locationId,
        string $namespaceId,
        string $serviceId
    ): void {
        // Instantiate a client.
        $client = new LookupServiceClient();
    
        // Run request.
        $serviceName = LookupServiceClient::serviceName($projectId, $locationId, $namespaceId, $serviceId);
        $resolveServiceRequest = (new ResolveServiceRequest())
            ->setName($serviceName);
        $service = $client->resolveService($resolveServiceRequest)->getService();
    
        // Print results.
        printf('Resolved Service: %s' . PHP_EOL, $service->getName());
        print('Endpoints:' . PHP_EOL);
        foreach ($service->getEndpoints() as $endpoint) {
            printf('  Name: %s' . PHP_EOL, $endpoint->getName());
            printf('    IP: %s' . PHP_EOL, $endpoint->getAddress());
            printf('    Port: %d' . PHP_EOL, $endpoint->getPort());
        }
    }

### Python

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def resolve_service(
        project_id: str, location: str, namespace_id: str, service_id: str
    ) -> ResolveServiceResponse:
        """Resolves a service in the given namespace.
    
        Args:
            project_id: Your Google Cloud project id.
            location: The Google Cloud region containing the namespace.
            namespace_id: The id of the parent namespace.
            service_id: The id of the service to resolve.
    
        Returns:
            The resolved service response, which returns all properties of the service, all endpoints, and all annotations.
        """
    
        client = servicedirectory_v1.LookupServiceClient()
    
        request = servicedirectory_v1.ResolveServiceRequest(
            name=servicedirectory_v1.RegistrationServiceClient().service_path(
                project_id, location, namespace_id, service_id
            )
        )
    
        response = client.resolve_service(request=request)
    
        print("Endpoints found:")
        for endpoint in response.service.endpoints:
            print(f"{endpoint.name} -- {endpoint.address}:{endpoint.port}")
    
        return response
    
    

### Ruby

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project   = "Your Google Cloud project ID"
    # location  = "The Google Cloud region containing the namespace"
    # namespace = "The name of the parent namespace"
    # service   = "The name of the service"
    
    require "google/cloud/service_directory"
    
    # Initialize the client
    lookup_service = Google::Cloud::[ServiceDirectory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1/latest/Google-Cloud-ServiceDirectory.html).[lookup_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory/latest/Google-Cloud-ServiceDirectory.html)
    
    # The name of the service
    service_path = lookup_service.service_path(
      project:   project,
      location:  location,
      namespace: namespace,
      service:   service
    )
    
    # Use the Service Directory API to resolve the service
    response = lookup_service.resolve_service name: service_path
    puts "Resolved service: #{response.service.name}"
    puts "Endpoints: "
    response.service.endpoints.each do |endpoint|
      puts "#{endpoint.name} #{endpoint.address} #{endpoint.port}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=servicedirectory). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

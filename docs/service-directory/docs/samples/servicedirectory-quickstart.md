---
url: https://docs.cloud.google.com/service-directory/docs/samples/servicedirectory-quickstart/
title: Quickstart \u00a0|\u00a0 Service Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:53.350632+00:00
---

# Quickstart  |  Service Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/samples/servicedirectory-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Samples ](https://docs.cloud.google.com/service-directory/docs/samples)



#  Quickstart Stay organized with collections  Save and categorize content based on your preferences. 

Basic usage of the Service Directory client library.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries)



## Code sample

### Go

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample quickstart is a program that uses Cloud Service Directory
    // create. delete, and resolve functionality.
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	servicedirectory "cloud.google.com/go/servicedirectory/apiv1"
    	sdpb "cloud.google.com/go/servicedirectory/apiv1/servicedirectorypb"
    )
    
    func main() {
    	projectID := "your-project-id"
    	location := "us-west1"
    	serviceID := "golang-quickstart-service"
    	namespaceID := "golang-quickstart-namespace"
    	endpointID := "golang-quickstart-endpoint"
    
    	ctx := context.Background()
    	// Create a registration client.
    	registry, err := servicedirectory.[NewRegistrationClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicedirectory/latest/apiv1.html#cloud_google_com_go_servicedirectory_apiv1_RegistrationClient_NewRegistrationClient)(ctx)
    	if err != nil {
    		log.Fatalf("servicedirectory.NewRegistrationClient: %v", err)
    	}
    	defer registry.Close()
    
    	// Create a lookup client.
    	resolver, err := servicedirectory.[NewLookupClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/servicedirectory/latest/apiv1.html#cloud_google_com_go_servicedirectory_apiv1_LookupClient_NewLookupClient)(ctx)
    	if err != nil {
    		log.Fatalf("servicedirectory.NewLookupClient: %v", err)
    	}
    	defer resolver.Close()
    
    	// Create a Namespace.
    	createNsReq := &sdpb.CreateNamespaceRequest{
    		Parent:      fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		NamespaceId: namespaceID,
    	}
    	namespace, err := registry.CreateNamespace(ctx, createNsReq)
    	if err != nil {
    		log.Fatalf("servicedirectory.CreateNamespace: %v", err)
    	}
    
    	// Create a Service.
    	createServiceReq := &sdpb.CreateServiceRequest{
    		Parent:    namespace.Name,
    		ServiceId: serviceID,
    		Service: &sdpb.Service{
    			Annotations: map[string]string{
    				"key1": "value1",
    				"key2": "value2",
    			},
    		},
    	}
    	service, err := registry.CreateService(ctx, createServiceReq)
    	if err != nil {
    		log.Fatalf("servicedirectory.CreateService: %v", err)
    	}
    
    	// Create an Endpoint.
    	createEndpointReq := &sdpb.CreateEndpointRequest{
    		Parent:     service.Name,
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
    	_, err = registry.CreateEndpoint(ctx, createEndpointReq)
    	if err != nil {
    		log.Fatalf("servicedirectory.CreateEndpoint: %v", err)
    	}
    
    	// Now Resolve the service.
    	lookupRequest := &sdpb.ResolveServiceRequest{
    		Name: service.Name,
    	}
    	result, err := resolver.ResolveService(ctx, lookupRequest)
    	if err != nil {
    		log.Fatalf("servicedirectory.ResolveService: %v", err)
    		return
    	}
    
    	fmt.Printf("Successfully Resolved Service %v", result)
    
    	// Delete the namespace.
    	deleteNsReq := &sdpb.DeleteNamespaceRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/namespaces/%s",
    			projectID, location, namespaceID),
    	}
    	registry.DeleteNamespace(ctx, deleteNsReq) // Ignore results.
    }
    

### Java

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.servicedirectory.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.LocationName.html);
    import com.google.cloud.servicedirectory.v1.[Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Namespace.html);
    import com.google.cloud.servicedirectory.v1.[RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html);
    import com.google.cloud.servicedirectory.v1.[RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html).[ListNamespacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.ListNamespacesPagedResponse.html);
    import java.io.IOException;
    
    public class Quickstart {
    
      public static void quickstart() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "your-region";
        quickstart(projectId, locationId);
      }
    
      public static void quickstart(String projectId, String locationId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html) client = [RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html).create()) {
    
          // The project and location that hold the namespace to list.
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.LocationName.html).of(projectId, locationId);
    
          // Call the API.
          [ListNamespacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.ListNamespacesPagedResponse.html) response = client.listNamespaces(parent);
    
          // Iterate over each namespace and print its name.
          System.out.println("Namespaces:");
          for ([Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Namespace.html) namespace : response.iterateAll()) {
            System.out.println(namespace.getName());
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
    
    // Imports the Google Cloud client library
    const {
      RegistrationServiceClient,
    } = require('[@google-cloud/service-directory](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)');
    
    // Creates a client
    const registrationServiceClient = new [RegistrationServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/service-directory/latest/overview.html)();
    
    // Build the location name
    const locationName = registrationServiceClient.locationPath(
      projectId,
      locationId
    );
    
    async function listNamespaces() {
      const [namespaces] = await registrationServiceClient.listNamespaces({
        parent: locationName,
      });
    
      console.log('Namespaces: ');
      for (const n of namespaces) {
        console.log(`${n.name}`);
      }
      return namespaces;
    }
    
    return listNamespaces();

### PHP

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\ServiceDirectory\V1\Client\RegistrationServiceClient;
    use Google\Cloud\ServiceDirectory\V1\ListNamespacesRequest;
    
    /** Uncomment and populate these variables in your code */
    // $projectId = '[YOUR_PROJECT_ID]';
    // $locationId = '[YOUR_GCP_REGION]';
    
    // Instantiate a client.
    $client = new RegistrationServiceClient();
    
    // Run request.
    $locationName = RegistrationServiceClient::locationName($projectId, $locationId);
    $listNamespacesRequest = (new ListNamespacesRequest())
        ->setParent($locationName);
    $pagedResponse = $client->listNamespaces($listNamespacesRequest);
    
    // Iterate over each namespace and print its name.
    print('Namespaces: ' . PHP_EOL);
    foreach ($pagedResponse->iterateAllElements() as $namespace) {
        print($namespace->getName() . PHP_EOL);
    }

### Python

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [servicedirectory_v1](https://docs.cloud.google.com/python/docs/reference/servicedirectory/latest)
    from google.cloud.servicedirectory_v1.services.registration_service.pagers import (
        [ListNamespacesPager](https://docs.cloud.google.com/python/docs/reference/servicedirectory/latest/google.cloud.servicedirectory_v1.services.registration_service.pagers.ListNamespacesPager.html),
    )
    
    
    def list_namespaces(project_id: str, location: str) -> ListNamespacesPager:
        """Lists all namespaces in the given location.
    
        Args:
            project_id: The Google Cloud project id.
            location: The location which contains the namespaces to list.
    
        Returns:
            All namespaces in the given location.
        """
    
        client = [servicedirectory_v1](https://docs.cloud.google.com/python/docs/reference/servicedirectory/latest).[RegistrationServiceClient](https://docs.cloud.google.com/python/docs/reference/servicedirectory/latest/google.cloud.servicedirectory_v1.services.registration_service.RegistrationServiceClient.html)()
    
        response = client.[list_namespaces](https://docs.cloud.google.com/python/docs/reference/servicedirectory/latest/google.cloud.servicedirectory_v1.services.registration_service.RegistrationServiceClient.html#google_cloud_servicedirectory_v1_services_registration_service_RegistrationServiceClient_list_namespaces)(
            parent=f"projects/{project_id}/locations/{location}"
        )
    
        print(f"Listed namespaces in {location}.")
        for namespace in response:
            print(f"Namespace: {namespace.name}")
    
        return response
    
    

### Ruby

To learn how to install and use the client library for Service Directory, see [Service Directory client libraries](https://docs.cloud.google.com/service-directory/docs/reference/libraries). 

To authenticate to Service Directory, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the Google Cloud client library
    require "google/cloud/service_directory"
    
    # Your Google Cloud Platform project ID
    project = ENV["GOOGLE_CLOUD_PROJECT"]
    
    # Location of the Service Directory Namespace
    location = "us-central1"
    
    # Initialize a client
    registration_service = Google::Cloud::[ServiceDirectory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1/latest/Google-Cloud-ServiceDirectory.html).[registration_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory/latest/Google-Cloud-ServiceDirectory.html)
    
    # The resource name of the project
    location_name = registration_service.location_path(
      project: project, location: location
    )
    
    # Request list of namespaces in the project
    response = registration_service.list_namespaces parent: location_name
    
    # List all namespaces for your project
    puts "Namespaces: "
    response.each do |namespace|
      puts namespace.name
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=servicedirectory). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

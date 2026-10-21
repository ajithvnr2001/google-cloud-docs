---
url: https://docs.cloud.google.com/service-directory/docs/configuring-service-directory/
title: Configure Service Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:01.749295+00:00
---

# Configure Service Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/configuring-service-directory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Guides ](https://docs.cloud.google.com/service-directory/docs/overview)



Send feedback 

#  Configure Service Directory Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to set up a Service Directory namespace, register a service in the namespace, and add endpoints to a service. You can create a namespace when you're registering a service or before registering a service.

Before running the commands listed on this page, familiarize yourself with the concepts in the [Service Directory overview](https://docs.cloud.google.com/service-directory/docs/overview) and [key terms](https://docs.cloud.google.com/service-directory/docs/key-terms) related to Service Directory.

## Set up your project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Service Directory API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=servicedirectory.googleapis.com)

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

  10. Enable the Service Directory API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=servicedirectory.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




## Configure Service Directory resources

To populate Service Directory with services, create a namespace and register your service in the namespace. 

### Configure a namespace

For your project, create a namespace in your region. This region doesn't have to be where all your services and endpoints are running but must be close, if possible.

You can register your services in any Service Directory region; they are still globally resolvable. Within a region, projects can have multiple namespaces, and those namespaces can be in different regions. A single namespace can't span multiple regions.

### Console

  1. In the Google Cloud console, go to the **Service Directory namespaces** page.

[Go to Service Directory namespaces](https://console.cloud.google.com/net-services/service-directory/namespaces)

  2. Click **Create namespace**.
  3. In the **Region** list, select a region for your namespace.
  4. In the **Namespace name** field, give the namespace a name.
  5. Click **Create**.



### gcloud

To use Service Directory on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).

  1. Create a namespace
         
         gcloud service-directory namespaces create NAMESPACE \
            --location REGION
         

Replace the following:

     * `NAMESPACE`: the name of the namespace that you are creating.
     * `REGION`: the Google Cloud region that contains the namespace.
  2. Optional: Set an [IAM policy](https://docs.cloud.google.com/service-directory/docs/access-control) on your namespace. This gives the specified user or group the specified role for this namespace and all services that belong to the namespace.
         
         gcloud service-directory namespaces add-iam-policy-binding NAMESPACE \
         --member user:someone@example.com \
         --role ROLE \
         --location REGION
         

Replace the following:

     * `NAMESPACE`: the name of the namespace that you created.
     * `ROLE`: the role that you are granting.
     * `REGION`: the Google Cloud region that contains the namespace.



### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Service Directory C# SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-csharp).
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.ServiceDirectory.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.html);
    
    public class CreateNamespaceSample
    {
        public Namespace CreateNamespace(
            string projectId = "my-project",
            string locationId = "us-east1",
            string namespaceId = "test-namespace")
        {
            // Create client
            [RegistrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html) registrationServiceClient = [RegistrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html#Google_Cloud_ServiceDirectory_V1_RegistrationServiceClient_Create)();
            // Initialize request argument(s)
            var locationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)(projectId, locationId);
            return registrationServiceClient.[CreateNamespace](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.RegistrationServiceClient.html#Google_Cloud_ServiceDirectory_V1_RegistrationServiceClient_CreateNamespace_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_ServiceDirectory_V1_Namespace_System_String_Google_Api_Gax_Grpc_CallSettings_)(locationName, new [Namespace](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.Namespace.html)(), namespaceId);
        }
    }
    

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Service Directory Go SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-go).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	servicedirectory "cloud.google.com/go/servicedirectory/apiv1"
    	sdpb "cloud.google.com/go/servicedirectory/apiv1/servicedirectorypb"
    )
    
    func createNamespace(w io.Writer, projectID string) error {
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
    	// Create a Namespace.
    	req := &sdpb.CreateNamespaceRequest{
    		Parent:      fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		NamespaceId: namespaceID,
    	}
    	resp, err := client.CreateNamespace(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateNamespace: %w", err)
    	}
    	fmt.Fprintf(w, "servicedirectory.CreateNamespace result: %s\n", resp.Name)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Service Directory Java SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-java).
    
    
    import com.google.cloud.servicedirectory.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.LocationName.html);
    import com.google.cloud.servicedirectory.v1.[Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Namespace.html);
    import com.google.cloud.servicedirectory.v1.[RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html);
    import java.io.IOException;
    
    public class NamespacesCreate {
    
      public static void createNamespace() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "your-region";
        // This is user-created; must be unique within the project/region above.
        String namespaceId = "your-namespace";
        createNamespace(projectId, locationId, namespaceId);
      }
    
      // Create a new namespace.
      public static void createNamespace(String projectId, String locationId, String namespaceId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html) client = [RegistrationServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.RegistrationServiceClient.html).create()) {
    
          // The project and location to create the namespace in.
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.LocationName.html).of(projectId, locationId);
    
          // The namespace object to create. Here, we use the default instance.
          [Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Namespace.html) namespace = [Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Namespace.html).newBuilder().build();
    
          // Send the request to create the namespace.
          [Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Namespace.html) createdNamespace = client.createNamespace(parent, namespace, namespaceId);
    
          // Process the response.
          System.out.println("Created Namespace: " + createdNamespace.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1.Namespace.html#com_google_cloud_servicedirectory_v1_Namespace_getName__)());
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Service Directory Node.js SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-nodejs).
    
    
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
    
    // Build the location name
    const locationName = registrationServiceClient.locationPath(
      projectId,
      locationId
    );
    
    async function createNamespace() {
      const [namespace] = await registrationServiceClient.createNamespace({
        parent: locationName,
        namespaceId: namespaceId,
      });
    
      console.log(`Created namespace: ${namespace.name}`);
      return namespace;
    }
    
    return createNamespace();

### PHP

To run this code, first [set up a PHP development environment](https://docs.cloud.google.com/php/docs) and [install the Service Directory PHP SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-php).
    
    
    use Google\Cloud\ServiceDirectory\V1\Client\RegistrationServiceClient;
    use Google\Cloud\ServiceDirectory\V1\CreateNamespaceRequest;
    use Google\Cloud\ServiceDirectory\V1\PBNamespace;
    
    /**
     * @param string $projectId     Your Cloud project ID
     * @param string $locationId    Your GCP region
     * @param string $namespaceId   Your namespace name
     */
    function create_namespace(
        string $projectId,
        string $locationId,
        string $namespaceId
    ): void {
        // Instantiate a client.
        $client = new RegistrationServiceClient();
    
        // Run request.
        $locationName = RegistrationServiceClient::locationName($projectId, $locationId);
        $createNamespaceRequest = (new CreateNamespaceRequest())
            ->setParent($locationName)
            ->setNamespaceId($namespaceId)
            ->setNamespace(new PBNamespace());
        $namespace = $client->createNamespace($createNamespaceRequest);
    
        // Print results.
        printf('Created Namespace: %s' . PHP_EOL, $namespace->getName());
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Service Directory Python SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-python).
    
    
    def create_namespace(project_id: str, location: str, namespace_id: str) -> Namespace:
        """Creates a namespace in the given location.
    
        Args:
            project_id: Your Google Cloud project id.
            location: The Google Cloud region containing the new namespace.
            namespace_id: A unique id for the namespace.
    
        Returns:
            The created namespace.
        """
    
        client = servicedirectory_v1.RegistrationServiceClient()
    
        namespace = servicedirectory_v1.Namespace(
            name=client.namespace_path(project_id, location, namespace_id)
        )
    
        response = client.create_namespace(
            parent=f"projects/{project_id}/locations/{location}",
            namespace=namespace,
            namespace_id=namespace_id,
        )
    
        print(f"Created namespace {response.name}.")
    
        return response
    
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Service Directory Ruby SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-ruby).
    
    
    # project   = "Your Google Cloud project ID"
    # location  = "The Google Cloud region containing the new namespace"
    # namespace = "The name of the namespace you are creating"
    
    require "google/cloud/service_directory"
    
    # Initialize the client
    registration_service = Google::Cloud::[ServiceDirectory](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory-v1/latest/Google-Cloud-ServiceDirectory.html).[registration_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_directory/latest/Google-Cloud-ServiceDirectory.html)
    
    # The parent path of the namespace
    parent = registration_service.location_path(
      project: project, location: location
    )
    
    # Use the Service Directory API to create the namespace
    response = registration_service.create_namespace(
      parent: parent, namespace_id: namespace
    )
    puts "Created namespace: #{response.name}"

### Configure a service

Create a service in the namespace. A service consists of a name and optional service-related annotations. There are some restrictions on the format of service names:

  * Service names must be unique within a namespace.
  * Service names must follow the naming convention for DNS labels.



To create a Private Service Connect forwarding rule and register it as a service with Service Directory, see [Register a Private Service Connect endpoint with Service Directory](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#configure-sd-manual).

To register a standard service with Service Directory, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Service Directory** page.

[Go to Service Directory](https://console.cloud.google.com/net-services/service-directory/services)

  2. Click **Register Service**.
  3. Click **Standard** , and then click **Next**.
  4. Choose a **Region** to register your service in.
  5. Choose a **Namespace** to register your service in. If you don't have a namespace, follow these steps to create one: 
     1. In the **Namespace** box, click **Create namespace**.
     2. Enter a **Namespace** name.
     3. Click **Create**. 
  6. Enter a **Service name**.
  7. Optional: If you want to add annotations to the service, do the following: 
     1. Click **Add annotation**.
     2. Add a **Key** and **Value**.
     3. To add more annotations, click **Add annotation** again.
  8. Click **Create**.



### gcloud

To use Service Directory on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).

  1. Create a service in a namespace.
         
         gcloud service-directory services create SERVICE \
            --annotations KEY_1=VALUE_1,KEY_2=VALUE_2 \
            --namespace NAMESPACE \
            --location REGION
         

Replace the following:

     * `SERVICE`: the name of the service that you are creating.
     * `NAMESPACE`: the name of the namespace that contains your service.
     * `REGION`: the Google Cloud region that contains the namespace.
     * `KEY_1`,`VALUE_1`,`KEY_2`, `VALUE_2`: key and value string set in pairs.
  2. Optional: Set an [IAM policy](https://docs.cloud.google.com/service-directory/docs/access-control) on your service. This gives the specified user or group the specified role for this service and all endpoints that belong to the service.
         
         gcloud service-directory services add-iam-policy-binding SERVICE \
         --member user:someone@example.com \
         --role ROLE \
         --namespace NAMESPACE \
         --location REGION
         

Replace the following:

     * `SERVICE`: the name that you gave your service.
     * `NAMESPACE`: the name of the namespace that contains your service
     * `ROLE`: the [role](https://docs.cloud.google.com/service-directory/docs/access-control) that you are granting.
     * `REGION`: the Google Cloud region that contains the namespace.



### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Service Directory C# SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-csharp).
    
    
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

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Service Directory Go SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-go).
    
    
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

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Service Directory Java SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-java).
    
    
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

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Service Directory Node.js SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-nodejs).
    
    
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

To run this code, first [set up a PHP development environment](https://docs.cloud.google.com/php/docs) and [install the Service Directory PHP SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-php).
    
    
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

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Service Directory Python SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-python).
    
    
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

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Service Directory Ruby SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-ruby).
    
    
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

### Configure an endpoint

After you have registered the service, add some endpoints. An endpoint consists of a unique name, an optional IP address and a port, and key-value annotations. The IP address, if specified, must be a valid IPv4 or IPv6 address.

### Console

  1. In the Google Cloud console, go to the **Service Directory** page.

[Go to Service Directory](https://console.cloud.google.com/net-services/service-directory/services)

  2. Click a service.
  3. Click **Add endpoint**.
  4. Provide an **Endpoint name**.
  5. Enter an IPv4 or IPv6 **IP address**.
  6. Enter a **Port** number.
  7. Optional: If you want to add annotations to the endpoint, do the following: 
     1. Under **Annotations** , click **Add annotation**.
     2. Add a **Key** and **Value**.
     3. To add more annotations, click **Add annotation** again.
  8. Click **Create**.



### gcloud

To use Service Directory on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).

Once the service is registered, add some endpoints.
    
    
    gcloud service-directory endpoints create ENDPOINT \
       --address IP_ADDRESS \
       --port PORT_NUMBER \
       --annotations KEY_1=VALUE_1,KEY_2=VALUE_2 \
       --service SERVICE \
       --namespace NAMESPACE \
       --location REGION
    
    
    
    gcloud service-directory endpoints create ENDPOINT2 \
       --address IP_ADDRESS2 \
       --port PORT_NUMBER2 \
       --service SERVICE \
       --namespace NAMESPACE \
       --location REGION
    

Replace the following:

  * `ENDPOINT` and `ENDPOINT2`: the names of the endpoints that you are creating in your service.
  * `IP_ADDRESS` and `IP_ADDRESS2`: the IPv6 and IPv4 addresses of the endpoints, respectively.
  * `PORT_NUMBER` and `PORT_NUMBER2`: the ports that the endpoints are running on.
  * `SERVICE`: the name of the service that contains your endpoint.
  * `NAMESPACE`: the name of the namespace that contains your service.
  * `REGION`: the Google Cloud region that contains the namespace.
  * `KEY_1`,`VALUE_1`,`KEY_2`, `VALUE_2`: key and value string set in pairs. 



### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Service Directory C# SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-csharp).
    
    
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

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Service Directory Go SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-go).
    
    
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

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Service Directory Java SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-java).
    
    
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

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Service Directory Node.js SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-nodejs).
    
    
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

To run this code, first [set up a PHP development environment](https://docs.cloud.google.com/php/docs) and [install the Service Directory PHP SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-php).
    
    
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

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Service Directory Python SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-python).
    
    
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

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Service Directory Ruby SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-ruby).
    
    
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

## Resolve a service

Service Directory lets clients resolve services by using DNS, HTTP, and gRPC. Resolving the service returns all properties of the service, all endpoints, and all annotations.

### gcloud

To use Service Directory on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud service-directory services resolve SERVICE \
       --namespace NAMESPACE \
       --location REGION
    

Replace the following:

  * `SERVICE`: the name of the service that you are resolving.
  * `NAMESPACE`: the name of the namespace that contains your service.
  * `REGION`: the Google Cloud region that contains the namespace.



### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Service Directory C# SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-csharp).
    
    
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

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Service Directory Go SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-go).
    
    
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

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Service Directory Java SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-java).
    
    
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

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Service Directory Node.js SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-nodejs).
    
    
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

To run this code, first [set up a PHP development environment](https://docs.cloud.google.com/php/docs) and [install the Service Directory PHP SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-php).
    
    
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

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Service Directory Python SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-python).
    
    
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

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Service Directory Ruby SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-ruby).
    
    
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

## Delete resources

If you don't need a resource, you can delete it from Service Directory.

### Delete an endpoint from a service

### Console

  1. In the Google Cloud console, go to the **Service Directory** page.

[Go to Service Directory](https://console.cloud.google.com/net-services/service-directory/services)

  2. Click the service that you want to delete the endpoint from.
  3. Select the checkbox next to the endpoint that you want to delete.
  4. Click **Delete**.
  5. In the confirmation dialog, click **Delete** again.



### gcloud

To use Service Directory on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud service-directory endpoints delete ENDPOINT \
        --service=SERVICE \
        --namespace=NAMESPACE \
        --location=REGION
    

Replace the following:

  * `ENDPOINT`: the name of the endpoint that you are deleting.
  * `SERVICE`: the name of the service that contains your endpoint.
  * `NAMESPACE`: the name of the namespace that contains your service.
  * `REGION`: the Google Cloud region that contains the namespace.



### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Service Directory C# SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-csharp).
    
    
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

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Service Directory Go SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-go).
    
    
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

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Service Directory Java SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-java).
    
    
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

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Service Directory Node.js SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-nodejs).
    
    
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

To run this code, first [set up a PHP development environment](https://docs.cloud.google.com/php/docs) and [install the Service Directory PHP SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-php).
    
    
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

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Service Directory Python SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-python).
    
    
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

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Service Directory Ruby SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-ruby).
    
    
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

### Delete a service from a namespace

You can delete a service that has endpoints. When a service is deleted, all of its endpoints are deleted as well.

You can delete a service that has a [Service Directory zone](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory-zone) pointing to it. Any further DNS queries for that service return `NXDOMAIN`.

### Console

  1. In the Google Cloud console, go to the **Service Directory** page.

[Go to Service Directory](https://console.cloud.google.com/net-services/service-directory/services)

  2. Select the checkbox next to the service that you want to delete.
  3. Click **Delete**.
  4. In the confirmation dialog, click **Delete** again.



### gcloud

To use Service Directory on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud service-directory services delete SERVICE \
        --namespace=NAMESPACE \
        --location=REGION
    

Replace the following:

  * `SERVICE`: the name of the service that you are deleting.
  * `NAMESPACE`: the name of the namespace that contains your service.
  * `REGION`: the Google Cloud region that contains the namespace.



### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Service Directory C# SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-csharp).
    
    
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

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Service Directory Go SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-go).
    
    
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

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Service Directory Java SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-java).
    
    
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

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Service Directory Node.js SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-nodejs).
    
    
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

To run this code, first [set up a PHP development environment](https://docs.cloud.google.com/php/docs) and [install the Service Directory PHP SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-php).
    
    
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

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Service Directory Python SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-python).
    
    
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

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Service Directory Ruby SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-ruby).
    
    
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

### Delete a namespace

You can delete a namespace that has services and endpoints. When a namespace is deleted, all of its services and endpoints are deleted as well.

You can delete a namespace that has a [Service Directory zone](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory-zone) pointing to it. Any further DNS queries (not including SOA/NS requests for the zone origin) return `NXDOMAIN`.

### Console

  1. In the Google Cloud console, go to the **Service Directory namespaces** page.

[Go to Service Directory namespaces](https://console.cloud.google.com/net-services/service-directory/namespaces)

  2. Select the checkbox next to the namespace that you want to delete.
  3. Click **Delete**.
  4. In the confirmation dialog, click **Delete** again.



### gcloud

To use Service Directory on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud service-directory namespaces delete NAMESPACE \
        --location=REGION
    

Replace the following:

  * `NAMESPACE`: the name of the namespace that you are deleting.
  * `REGION`: the Google Cloud region that contains the namespace.



### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Service Directory C# SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-csharp).
    
    
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

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Service Directory Go SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-go).
    
    
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

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Service Directory Java SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-java).
    
    
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

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Service Directory Node.js SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-nodejs).
    
    
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

To run this code, first [set up a PHP development environment](https://docs.cloud.google.com/php/docs) and [install the Service Directory PHP SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-php).
    
    
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

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Service Directory Python SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-python).
    
    
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

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Service Directory Ruby SDK](https://docs.cloud.google.com/service-directory/docs/reference/libraries#client-libraries-install-ruby).
    
    
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

  * To configure a Service Directory zone so that you can query your service using DNS, see [Configure a Service Directory zone](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory-zone).
  * To get an overview of Service Directory, see the [Service Directory overview](https://docs.cloud.google.com/service-directory/docs/overview).
  * To find solutions for common issues that you might encounter when using Service Directory, see [Troubleshooting](https://docs.cloud.google.com/service-directory/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/tenants/
title: Tenant basics (v4beta1) \u00a0|\u00a0 Cloud Talent Solution - Job Search v4beta1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:34.036250+00:00
---

# Tenant basics (v4beta1)  |  Cloud Talent Solution - Job Search v4beta1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/tenants/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Job Search v4beta1 (deprecated) ](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs)



Send feedback 

#  Tenant basics (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

[Tenants](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/reference/rest/v4beta1/projects.tenants) are entities that own any jobs and companies objects assigned to them. They create a middle layer of organization between a Google Cloud project and your uploaded data. Tenants allow you to isolate different groupings of your data without the need for multiple projects by preventing any data from being shared across tenancy barriers. Multi-tenancy is useful in situations where you may have more than one customer and don't want to share data between them, but would like to maintain a single Google Cloud project for internal billing and reporting. For example:

  * Job site providers building job sites for organizations with multiple subsidiary companies.
  * Hiring agencies building applicant tracking systems for multiple businesses.



Each Google Cloud project is assigned a `tenant_id` for a single default tenant. Optionally, you can change the default by creating more than one tenant within a given project.

Tenants are fully isolated from one another. All APIs ask for only a single tenant to prevent data being queried across multiple tenants in a single API call. Machine learning (ML) similarly treats tenants as discrete units and does not cross tenancy barriers. A project can support as many tenants as required.

## Default tenants

In Job Search v4beta1 and newer, a Tenant entity is required. All projects are assigned a `tenant_id` for a single default tenant. If you don't want to use multiple tenants, you can either:

  1. **Use your project's default tenant (Recommended)**. You don't need to reference the tenant specifically in order to do this. You can use the format `projects/{project_id}/jobs/{job_id}` and the Cloud Talent Solution backend will assume that you're using the default tenant.

  2. **[Create a single tenant](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/tenants#create_a_tenant) and use it in place of the default tenant**. If you create your own tenant, you need to reference it: `projects/{project_id}/tenants/{tenant_id}/jobs/{job_id}`.




The default `tenant_id` is unique to each project and is never overwritten or replaced if you create additional tenants. You cannot call CRUD methods on the default tenant.

**Note:** If you choose to use the default tenant, the CTS backend uses your assigned `tenant_id` value automatically without you needing to enter it (Option 1, above). If you would like to find your default `tenant_id` value, [create a company](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/companies#create_a_company) without a tenant. The default `tenant_id` appears in the company resource name in the response.

## Created tenants (optional)

Creating your own tenants is optional. Each Job Search project is assigned a default tenant by the CTS backend. If you do not want to use multi-tenancy to separate subdivisions of your data, we recommend that you use the default tenant.

### Create a tenant

You are required to create a unique `externalId` value and assign it to the new tenant. The call then returns a unique `name` assigned by our backend system, also assigned to that tenant. Be sure to record and store both the `name` and `externalId` values, as they are used to update/delete/reference.

The code sample below creates a new tenant:

### Java

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/overview). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.talent.v4beta1.CreateTenantRequest;
    import com.google.cloud.talent.v4beta1.ProjectName;
    import com.google.cloud.talent.v4beta1.Tenant;
    import com.google.cloud.talent.v4beta1.TenantServiceClient;
    import java.io.IOException;
    
    public class JobSearchCreateTenant {
    
      public static void createTenant() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String externalId = "your-external-id";
        createTenant(projectId, externalId);
      }
    
      // Create Tenant for scoping resources, e.g. companies and jobs.
      public static void createTenant(String projectId, String externalId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try (TenantServiceClient tenantServiceClient = TenantServiceClient.create()) {
          ProjectName parent = ProjectName.of(projectId);
          Tenant tenant = Tenant.newBuilder().setExternalId(externalId).build();
    
          CreateTenantRequest request =
              CreateTenantRequest.newBuilder().setParent(parent.toString()).setTenant(tenant).build();
    
          Tenant response = tenantServiceClient.createTenant(request);
          System.out.println("Created Tenant");
          System.out.format("Name: %s%n", response.getName());
          System.out.format("External ID: %s%n", response.getExternalId());
        }
      }
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    from google.cloud import talent
    
    
    def create_tenant(project_id, external_id):
        """Create Tenant for scoping resources, e.g. companies and jobs"""
    
        client = talent.[TenantServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient.html)()
    
        # project_id = 'Your Google Cloud Project ID'
        # external_id = 'Your Unique Identifier for Tenant'
    
        if isinstance(project_id, bytes):
            project_id = project_id.decode("utf-8")
        if isinstance(external_id, bytes):
            external_id = external_id.decode("utf-8")
        parent = f"projects/{project_id}"
        tenant = talent.[Tenant](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Tenant.html)(external_id=external_id)
    
        response = client.[create_tenant](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient.html#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_create_tenant)(parent=parent, tenant=tenant)
        print("Created Tenant")
        print(f"Name: {response.name}")
        print(f"External ID: {response.external_id}")
        return response.name
    
    

### Retrieve a tenant

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    import com.google.cloud.talent.v4beta1.GetTenantRequest;
    import com.google.cloud.talent.v4beta1.Tenant;
    import com.google.cloud.talent.v4beta1.TenantName;
    import com.google.cloud.talent.v4beta1.TenantServiceClient;
    import java.io.IOException;
    
    public class JobSearchGetTenant {
    
      public static void getTenant() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String tenantId = "your-tenant-id";
        getTenant(projectId, tenantId);
      }
    
      // Get Tenant by name.
      public static void getTenant(String projectId, String tenantId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try (TenantServiceClient tenantServiceClient = TenantServiceClient.create()) {
          TenantName name = TenantName.of(projectId, tenantId);
    
          GetTenantRequest request = GetTenantRequest.newBuilder().setName(name.toString()).build();
    
          Tenant response = tenantServiceClient.getTenant(request);
          System.out.format("Name: %s%n", response.getName());
          System.out.format("External ID: %s%n", response.getExternalId());
        }
      }
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    from google.cloud import talent
    
    
    def get_tenant(project_id, tenant_id):
        """Get Tenant by name"""
    
        client = talent.[TenantServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient.html)()
    
        # project_id = 'Your Google Cloud Project ID'
        # tenant_id = 'Your Tenant ID'
    
        if isinstance(project_id, bytes):
            project_id = project_id.decode("utf-8")
        if isinstance(tenant_id, bytes):
            tenant_id = tenant_id.decode("utf-8")
        name = client.[tenant_path](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient.html#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_tenant_path)(project_id, tenant_id)
    
        response = client.[get_tenant](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient.html#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_get_tenant)(name=name)
        print(f"Name: {response.name}")
        print(f"External ID: {response.external_id}")
    
    

### List tenants

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    import com.google.cloud.talent.v4beta1.ListTenantsRequest;
    import com.google.cloud.talent.v4beta1.ProjectName;
    import com.google.cloud.talent.v4beta1.Tenant;
    import com.google.cloud.talent.v4beta1.TenantServiceClient;
    import java.io.IOException;
    
    public class JobSearchListTenants {
    
      public static void listTenants() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        listTenants(projectId);
      }
    
      // List Tenants.
      public static void listTenants(String projectId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try (TenantServiceClient tenantServiceClient = TenantServiceClient.create()) {
          ProjectName parent = ProjectName.of(projectId);
    
          ListTenantsRequest request =
              ListTenantsRequest.newBuilder().setParent(parent.toString()).build();
    
          for (Tenant responseItem : tenantServiceClient.listTenants(request).iterateAll()) {
            System.out.format("Tenant Name: %s%n", responseItem.getName());
            System.out.format("External ID: %s%n", responseItem.getExternalId());
          }
        }
      }
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    from google.cloud import talent
    
    
    def list_tenants(project_id):
        """List Tenants"""
    
        client = talent.[TenantServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient.html)()
    
        # project_id = 'Your Google Cloud Project ID'
    
        if isinstance(project_id, bytes):
            project_id = project_id.decode("utf-8")
        parent = f"projects/{project_id}"
    
        # Iterate over all results
        for response_item in client.[list_tenants](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient.html#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_list_tenants)(parent=parent):
            print(f"Tenant Name: {response_item.name}")
            print(f"External ID: {response_item.external_id}")
    
    

### Delete a tenant

### Java

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    import com.google.cloud.talent.v4beta1.DeleteTenantRequest;
    import com.google.cloud.talent.v4beta1.TenantName;
    import com.google.cloud.talent.v4beta1.TenantServiceClient;
    import java.io.IOException;
    
    public class JobSearchDeleteTenant {
    
      public static void deleteTenant() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String tenantId = "your-tenant-id";
        deleteTenant(projectId, tenantId);
      }
    
      // Delete Tenant.
      public static void deleteTenant(String projectId, String tenantId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try (TenantServiceClient tenantServiceClient = TenantServiceClient.create()) {
          TenantName name = TenantName.of(projectId, tenantId);
    
          DeleteTenantRequest request =
              DeleteTenantRequest.newBuilder().setName(name.toString()).build();
    
          tenantServiceClient.deleteTenant(request);
          System.out.println("Deleted Tenant.");
        }
      }
    }

### Python

For more on installing and creating a Cloud Talent Solution client, see [Cloud Talent Solution Client Libraries](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/libraries). 
    
    
    from google.cloud import talent
    
    
    def delete_tenant(project_id, tenant_id):
        """Delete Tenant"""
    
        client = talent.[TenantServiceClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient.html)()
    
        # project_id = 'Your Google Cloud Project ID'
        # tenant_id = 'Your Tenant ID)'
    
        if isinstance(project_id, bytes):
            project_id = project_id.decode("utf-8")
        if isinstance(tenant_id, bytes):
            tenant_id = tenant_id.decode("utf-8")
        name = client.[tenant_path](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient.html#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_tenant_path)(project_id, tenant_id)
    
        client.[delete_tenant](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient.html#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_delete_tenant)(name=name)
        print("Deleted Tenant.")
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

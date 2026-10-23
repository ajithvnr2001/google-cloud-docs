---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-delete-tenant/
title: Delete tenant (v4beta1) \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:45.258869+00:00
---

# Delete tenant (v4beta1)  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/samples/job-search-delete-tenant/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Samples ](https://docs.cloud.google.com/talent-solution/job-search/docs/samples)



#  Delete tenant (v4beta1) Stay organized with collections  Save and categorize content based on your preferences. 

Delete tenant.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Tenant basics](https://docs.cloud.google.com/talent-solution/job-search/docs/tenants)
  * [Tenant basics (v4beta1)](https://docs.cloud.google.com/talent-solution/job-search/v4beta1/docs/tenants)



## Code sample

### Node.js

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const talent = require('[@google-cloud/talent](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)').v4;
    
    /** Delete Tenant */
    function sampleDeleteTenant(projectId, tenantId) {
      const client = new talent.[TenantServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)();
      // const projectId = 'Your Google Cloud Project ID';
      // const tenantId = 'Your Tenant ID)';
      const formattedName = client.tenantPath(projectId, tenantId);
      client.deleteTenant({name: formattedName}).catch(err => {
        console.error(err);
      });
      console.log('Deleted Tenant.');
    }
    

### Python

To learn how to install and use the client library for CTS, see [CTS client libraries](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries). For more information, see the [CTS Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/talent/latest). 

To authenticate to CTS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=talentsolution). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

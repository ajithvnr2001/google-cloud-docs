---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-delete-security-health-analytics-custom-module/
title: Delete a Security Health Analytics custom module \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:59.609030+00:00
---

# Delete a Security Health Analytics custom module  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-delete-security-health-analytics-custom-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Delete a Security Health Analytics custom module Stay organized with collections  Save and categorize content based on your preferences. 

Sample code to delete Security Health Analytics custom modules

## Code sample

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycentermanagement.v1.[DeleteSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.DeleteSecurityHealthAnalyticsCustomModuleRequest.html);
    import com.google.cloud.securitycentermanagement.v1.[SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.html);
    import java.io.IOException;
    
    public class DeleteSecurityHealthAnalyticsCustomModule {
    
      public static void main(String[] args) throws IOException {
        // https://cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.securityHealthAnalyticsCustomModules/delete
        // TODO: Developer should replace project_id with a real project ID before running this code
        String projectId = "project_id";
    
        String customModuleId = "custom_module_id";
    
        deleteSecurityHealthAnalyticsCustomModule(projectId, customModuleId);
      }
    
      public static boolean deleteSecurityHealthAnalyticsCustomModule(
          String projectId, String customModuleId) throws IOException {
    
        // Initialize client that will be used to send requests. This client only needs
        // to be created
        // once, and can be reused for multiple requests.
        try ([SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.html) client = [SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.html).create()) {
    
          String name =
              String.format(
                  "projects/%s/locations/global/securityHealthAnalyticsCustomModules/%s",
                  projectId, customModuleId);
    
          [DeleteSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.DeleteSecurityHealthAnalyticsCustomModuleRequest.html) request =
              [DeleteSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.DeleteSecurityHealthAnalyticsCustomModuleRequest.html).newBuilder().setName(name).build();
    
          client.deleteSecurityHealthAnalyticsCustomModule(request);
    
          return true;
        }
      }
    }

### Node.js

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // npm install '@google-cloud/securitycentermanagement'
    const {
      SecurityCenterManagementClient,
    } = require('[@google-cloud/securitycentermanagement](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/overview.html)');
    
    const client = new [SecurityCenterManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/overview.html)();
    
    /*
     * Required. Resource name of security health analytics module.
     *     Its format is
     *    `organizations/[organization_id]/locations/[location_id]/securityHealthAnalyticsCustomModules/[custom_module]`
     *    `folders/[folder_id]/locations/[location_id]/securityHealthAnalyticsCustomModules/[custom_module]`
     *    `projects/[project_id]/locations/[location_id]/securityHealthAnalyticsCustomModules/[custom_module]`
     */
    const name = `organizations/${organizationId}/locations/${locationId}/securityHealthAnalyticsCustomModules/${customModuleId}`;
    
    async function deleteSecurityHealthAnalyticsCustomModule() {
      const [response] = await client.deleteSecurityHealthAnalyticsCustomModule({
        name: name,
      });
      console.log(
        'Security Health Analytics Custom Module delete succeeded: ',
        response
      );
    }
    
    deleteSecurityHealthAnalyticsCustomModule();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def delete_security_health_analytics_custom_module(parent: str, module_id: str):
        """
        Deletes a Security Health Analytics custom module.
        Args:
            parent: Use any one of the following options:
                    - organizations/{organization_id}/locations/{location_id}
                    - folders/{folder_id}/locations/{location_id}
                    - projects/{project_id}/locations/{location_id}
        Returns:
            The deleted Security Health Analytics custom module.
        Raises:
            NotFound: If the specified custom module does not exist.
        """
        client = securitycentermanagement_v1.SecurityCenterManagementClient()
    
        try:
            request = securitycentermanagement_v1.DeleteSecurityHealthAnalyticsCustomModuleRequest(
                name=f"{parent}/securityHealthAnalyticsCustomModules/{module_id}",
            )
    
            client.delete_security_health_analytics_custom_module(request=request)
            print(f"Deleted SecurityHealthAnalyticsCustomModule Successfully: {module_id}")
        except NotFound as e:
            print(f"Custom Module not found: {module_id}")
            raise e

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

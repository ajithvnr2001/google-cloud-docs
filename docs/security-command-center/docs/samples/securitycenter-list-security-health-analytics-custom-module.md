---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-security-health-analytics-custom-module/
title: List Security Health Analytics custom modules \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:34:31.864229+00:00
---

# List Security Health Analytics custom modules  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-security-health-analytics-custom-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  List Security Health Analytics custom modules Stay organized with collections  Save and categorize content based on your preferences. 

Sample code to list Security Health Analytics custom modules

## Code sample

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycentermanagement.v1.[ListSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListSecurityHealthAnalyticsCustomModulesRequest.html);
    import com.google.cloud.securitycentermanagement.v1.[SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.html);
    import com.google.cloud.securitycentermanagement.v1.[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule.html);
    import com.google.common.collect.ImmutableList;
    import java.io.IOException;
    
    public class ListSecurityHealthAnalyticsCustomModules {
    
      public static void main(String[] args) throws IOException {
        // https://cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.securityHealthAnalyticsCustomModules/list
        // TODO: Developer should replace project_id with a real project ID before running this code
        String projectId = "project_id";
    
        listSecurityHealthAnalyticsCustomModules(projectId);
      }
    
      public static ImmutableList<SecurityHealthAnalyticsCustomModule>
          listSecurityHealthAnalyticsCustomModules(String projectId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs
        // to be created
        // once, and can be reused for multiple requests.
        try ([SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.html) client = [SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.html).create()) {
    
          [ListSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListSecurityHealthAnalyticsCustomModulesRequest.html) request =
              [ListSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListSecurityHealthAnalyticsCustomModulesRequest.html).newBuilder()
                  .setParent(String.format("projects/%s/locations/global", projectId))
                  .build();
    
          return ImmutableList.copyOf(
              client.listSecurityHealthAnalyticsCustomModules(request).iterateAll());
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
     * Required. The name of the parent resource of security health analytics module
     *     Its format is
     *    `organizations/[organization_id]/locations/[location_id]`
     *    `folders/[folder_id]/locations/[location_id]`
     *    `projects/[project_id]/locations/[location_id]`
     */
    const parent = `organizations/${organizationId}/locations/${locationId}`;
    
    async function listSecurityHealthAnalyticsCustomModule() {
      const [response] = await client.listSecurityHealthAnalyticsCustomModules({
        parent: parent,
      });
      console.log(
        'Security Health Analytics Custom Module list succeeded: ',
        response
      );
    }
    
    listSecurityHealthAnalyticsCustomModule();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def list_security_health_analytics_custom_module(parent: str):
        """
        Retrieves list of Security Health Analytics custom module.
        Args:
            parent: Use any one of the following options:
                    - organizations/{organization_id}/locations/{location_id}
                    - folders/{folder_id}/locations/{location_id}
                    - projects/{project_id}/locations/{location_id}
        Returns:
            List of retrieved Security Health Analytics custom modules.
        Raises:
            NotFound: If the specified custom module does not exist.
        """
    
        client = securitycentermanagement_v1.SecurityCenterManagementClient()
    
        try:
            request = securitycentermanagement_v1.ListSecurityHealthAnalyticsCustomModulesRequest(
                parent=parent,
            )
    
            response = client.list_security_health_analytics_custom_modules(request=request)
    
            custom_modules = []
            for custom_module in response:
                print(f"Custom Module: {custom_module.name}")
                custom_modules.append(custom_module)
            return custom_modules
        except NotFound as e:
            print(f"Parent resource not found: {parent}")
            raise e
        except Exception as e:
            print(f"An error occurred while listing custom modules: {e}")
            raise e

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

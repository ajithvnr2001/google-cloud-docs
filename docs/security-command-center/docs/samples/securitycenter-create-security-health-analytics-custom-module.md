---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-create-security-health-analytics-custom-module/
title: Create a Security Health Analytics custom module \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:47.159326+00:00
---

# Create a Security Health Analytics custom module  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-create-security-health-analytics-custom-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Create a Security Health Analytics custom module Stay organized with collections  Save and categorize content based on your preferences. 

Sample code to create Security Health Analytics custom modules

## Code sample

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycentermanagement.v1.[CreateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CreateSecurityHealthAnalyticsCustomModuleRequest.html);
    import com.google.cloud.securitycentermanagement.v1.[CustomConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CustomConfig.html);
    import com.google.cloud.securitycentermanagement.v1.[CustomConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CustomConfig.html).[ResourceSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CustomConfig.ResourceSelector.html);
    import com.google.cloud.securitycentermanagement.v1.[CustomConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CustomConfig.html).Severity;
    import com.google.cloud.securitycentermanagement.v1.[SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.html);
    import com.google.cloud.securitycentermanagement.v1.[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule.html);
    import com.google.cloud.securitycentermanagement.v1.[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule.html).EnablementState;
    import com.google.type.[Expr](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Expr.html);
    import java.io.IOException;
    
    public class CreateSecurityHealthAnalyticsCustomModule {
    
      public static void main(String[] args) throws IOException {
        // https://cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.securityHealthAnalyticsCustomModules/create
        // TODO: Developer should replace project_id with a real project ID before running this code
        String projectId = "project_id";
    
        String customModuleDisplayName = "custom_module_display_name";
    
        createSecurityHealthAnalyticsCustomModule(projectId, customModuleDisplayName);
      }
    
      public static [SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule.html) createSecurityHealthAnalyticsCustomModule(
          String projectId, String customModuleDisplayName) throws IOException {
    
        // Initialize client that will be used to send requests. This client only needs
        // to be created
        // once, and can be reused for multiple requests.
        try ([SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.html) client = [SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.html).create()) {
    
          String name =
              String.format(
                  "projects/%s/locations/global/securityHealthAnalyticsCustomModules/%s",
                  projectId, "custom_module");
    
          // define the CEL expression here and this will scans for keys that have not been rotated in
          // the last 30 days, change it according to the your requirements
          [Expr](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Expr.html) expr =
              [Expr](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Expr.html).newBuilder()
                  .[setExpression](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Expr.Builder.html#com_google_type_Expr_Builder_setExpression_java_lang_String_)(
                      "has(resource.rotationPeriod) && (resource.rotationPeriod > "
                          + "duration('2592000s'))")
                  .build();
    
          // define the resource selector
          [ResourceSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CustomConfig.ResourceSelector.html) resourceSelector =
              [ResourceSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CustomConfig.ResourceSelector.html).newBuilder()
                  .[addResourceTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CustomConfig.ResourceSelector.Builder.html#com_google_cloud_securitycentermanagement_v1_CustomConfig_ResourceSelector_Builder_addResourceTypes_java_lang_String_)("cloudkms.googleapis.com/CryptoKey")
                  .build();
    
          // define the custom module configuration, update the severity, description,
          // recommendation below
          [CustomConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CustomConfig.html) customConfig =
              [CustomConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CustomConfig.html).newBuilder()
                  .[setPredicate](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CustomConfig.Builder.html#com_google_cloud_securitycentermanagement_v1_CustomConfig_Builder_setPredicate_com_google_type_Expr_)(expr)
                  .[setResourceSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CustomConfig.Builder.html#com_google_cloud_securitycentermanagement_v1_CustomConfig_Builder_setResourceSelector_com_google_cloud_securitycentermanagement_v1_CustomConfig_ResourceSelector_)(resourceSelector)
                  .setSeverity(Severity.MEDIUM)
                  .setDescription("add your description here")
                  .[setRecommendation](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CustomConfig.Builder.html#com_google_cloud_securitycentermanagement_v1_CustomConfig_Builder_setRecommendation_java_lang_String_)("add your recommendation here")
                  .build();
    
          // define the security health analytics custom module configuration, update the
          // EnablementState below
          [SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule.html) securityHealthAnalyticsCustomModule =
              [SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule.html).newBuilder()
                  .setName(name)
                  .setDisplayName(customModuleDisplayName)
                  .setEnablementState(EnablementState.ENABLED)
                  .setCustomConfig(customConfig)
                  .build();
    
          [CreateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CreateSecurityHealthAnalyticsCustomModuleRequest.html) request =
              [CreateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CreateSecurityHealthAnalyticsCustomModuleRequest.html).newBuilder()
                  .setParent(String.format("projects/%s/locations/global", projectId))
                  .setSecurityHealthAnalyticsCustomModule(securityHealthAnalyticsCustomModule)
                  .build();
    
          [SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule.html) response =
              client.createSecurityHealthAnalyticsCustomModule(request);
    
          return response;
        }
      }
    }

### Node.js

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // npm install '@google-cloud/securitycentermanagement'
    const {
      SecurityCenterManagementClient,
      protos,
    } = require('[@google-cloud/securitycentermanagement](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/overview.html)');
    
    const client = new [SecurityCenterManagementClient](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/overview.html)();
    
    const EnablementState =
      protos.google.cloud.securitycentermanagement.v1
        .[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.cloud.securitycentermanagement.v1.securityhealthanalyticscustommodule-class.html).EnablementState;
    
    const Severity =
      protos.google.cloud.securitycentermanagement.v1.[CustomConfig](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.cloud.securitycentermanagement.v1.customconfig-class.html).[Severity](https://docs.cloud.google.com/nodejs/docs/reference/securitycentermanagement/latest/securitycentermanagement/protos.google.cloud.securitycentermanagement.v1.customconfig.severity.html);
    
    /*
     * Required. The name of the parent resource of security health analytics module
     *     Its format is
     *    `organizations/[organization_id]/locations/[location_id]`
     *    `folders/[folder_id]/locations/[location_id]`
     *    `projects/[project_id]/locations/[location_id]`
     */
    const parent = `organizations/${organizationId}/locations/${locationId}`;
    
    /*
     * Required. Resource name of security health analytics module.
     *     Its format is
     *    `organizations/[organization_id]/locations/[location_id]/securityHealthAnalyticsCustomModules/[custom_module]`
     *    `folders/[folder_id]/locations/[location_id]/securityHealthAnalyticsCustomModules/[custom_module]`
     *    `projects/[project_id]/locations/[location_id]/securityHealthAnalyticsCustomModules/[custom_module]`
     */
    const name = `organizations/${organizationId}/locations/${locationId}/securityHealthAnalyticsCustomModules/custom_module`;
    
    // define the CEL expression here and this will scans for keys that have not been rotated in
    // the last 30 days, change it according to your requirements
    const expr = {
      expression: `has(resource.rotationPeriod) && (resource.rotationPeriod > duration('2592000s'))`,
    };
    
    // define the resource selector
    const resourceSelector = {
      resourceTypes: ['cloudkms.googleapis.com/CryptoKey'],
    };
    
    // define the custom module configuration, update the severity, description,
    // recommendation below
    const customConfig = {
      predicate: expr,
      resourceSelector: resourceSelector,
      severity: Severity.MEDIUM,
      description: 'add your description here',
      recommendation: 'add your recommendation here',
    };
    
    // define the security health analytics custom module configuration, update the
    // EnablementState below
    const securityHealthAnalyticsCustomModule = {
      name: name,
      displayName: customModuleDisplayName,
      enablementState: EnablementState.ENABLED,
      customConfig: customConfig,
    };
    
    async function createSecurityHealthAnalyticsCustomModule() {
      const [response] = await client.createSecurityHealthAnalyticsCustomModule({
        parent: parent,
        securityHealthAnalyticsCustomModule: securityHealthAnalyticsCustomModule,
      });
      console.log(
        'Security Health Analytics Custom Module creation succeeded: ',
        response
      );
    }
    
    createSecurityHealthAnalyticsCustomModule();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def create_security_health_analytics_custom_module(parent: str) -> securitycentermanagement_v1.SecurityHealthAnalyticsCustomModule:
        """
        Creates a Security Health Analytics custom module.
    
        This custom module evaluates Cloud KMS CryptoKeys to ensure their rotation period exceeds 30 days (2592000 seconds),
        as per security best practices. A shorter rotation period helps reduce the risk of exposure in the event of a compromise.
    
        Args:
            parent: Use any one of the following options:
                    - organizations/{organization_id}/locations/{location_id}
                    - folders/{folder_id}/locations/{location_id}
                    - projects/{project_id}/locations/{location_id}
        Returns:
            Dict: Created custom module details.
        """
        client = securitycentermanagement_v1.SecurityCenterManagementClient()
    
        try:
            # Generate a unique suffix
            unique_suffix = str(uuid.uuid4()).replace("-", "_")
            # Generate a unique display name
            display_name = f"python_sample_sha_custom_module_{unique_suffix}"
    
            # Define the custom module configuration
            custom_module = {
                "display_name": display_name,
                "enablement_state": "ENABLED",
                "custom_config": {
                    "description": (
                        "Sample custom module for testing purposes. This custom module evaluates "
                        "Cloud KMS CryptoKeys to ensure their rotation period exceeds 30 days (2592000 seconds)."
                    ),
                    "predicate": {
                        "expression": "has(resource.rotationPeriod) && (resource.rotationPeriod > duration('2592000s'))",
                        "title": "Cloud KMS CryptoKey Rotation Period",
                        "description": (
                            "Evaluates whether the rotation period of a Cloud KMS CryptoKey exceeds 30 days. "
                            "A longer rotation period might increase the risk of exposure."
                        ),
                    },
                    "recommendation": (
                        "Review and adjust the rotation period for Cloud KMS CryptoKeys to align with your security policies. "
                        "Consider setting a shorter rotation period if possible."
                    ),
                    "resource_selector": {"resource_types": ["cloudkms.googleapis.com/CryptoKey"]},
                    "severity": "CRITICAL",
                    "custom_output": {
                        "properties": [
                            {
                                "name": "example_property",
                                "value_expression": {
                                    "description": "The resource name of the CryptoKey being evaluated.",
                                    "expression": "resource.name",
                                    "location": "global",
                                    "title": "CryptoKey Resource Name",
                                },
                            }
                        ]
                    },
                },
            }
    
            request = securitycentermanagement_v1.CreateSecurityHealthAnalyticsCustomModuleRequest(
                parent=parent,
                security_health_analytics_custom_module=custom_module,
            )
    
            response = client.create_security_health_analytics_custom_module(request=request)
            print(f"Created SecurityHealthAnalytics Custom Module: {response.name}")
            return response
    
        except GoogleAPICallError as e:
            print(f"Failed to create EventThreatDetectionCustomModule: {e}")
            raise

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

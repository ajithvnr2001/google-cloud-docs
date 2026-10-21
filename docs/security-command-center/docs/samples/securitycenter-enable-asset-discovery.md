---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-enable-asset-discovery/
title: Enable asset discovery \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:27.333000+00:00
---

# Enable asset discovery  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-enable-asset-discovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Enable asset discovery Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to enable or disable asset discovery

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configuring asset discovery using the Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/how-to-api-configure-asset-discovery)



## Code sample

### Go

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv1"
    	"cloud.google.com/go/securitycenter/apiv1/securitycenterpb"
    	"google.golang.org/genproto/protobuf/field_mask"
    )
    
    // Turns on asset discovery for orgID and prints out updated settings to w.
    // settings. orgID is the numeric Organization ID.
    func enableAssetDiscovery(w io.Writer, orgID string) error {
    	// orgID := "12321311"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)() // Closing the client safely cleans up background resources.
    
    	req := &securitycenterpb.UpdateOrganizationSettingsRequest{
    		OrganizationSettings: &securitycenterpb.OrganizationSettings{
    			Name:                 fmt.Sprintf("organizations/%s/organizationSettings", orgID),
    			EnableAssetDiscovery: true,
    		},
    		// Only update the asset discovery setting.
    		UpdateMask: &field_mask.FieldMask{
    			Paths: []string{"enable_asset_discovery"},
    		},
    	}
    	settings, err := client.UpdateOrganizationSettings(ctx, req)
    	if err != nil {
    		return fmt.Errorf("UpdateOrganizationSettings: %w", err)
    	}
    	fmt.Fprintf(w, "Updated Settings for: %s\n", settings.Name)
    	fmt.Fprintf(w, "Asset discovery on? %v\n", settings.EnableAssetDiscovery)
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static OrganizationSettings updateOrganizationSettings(OrganizationName organizationName) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // Start setting up a request to update OrganizationSettings for.
        // OrganizationName organizationName = OrganizationName.of(/*organizationId=*/"123234324");
        OrganizationSettings organizationSettings =
            OrganizationSettings.newBuilder()
                .setName(organizationName.toString() + "/organizationSettings")
                .setEnableAssetDiscovery(true)
                .build();
        FieldMask updateMask = FieldMask.newBuilder().addPaths("enable_asset_discovery").build();
    
        UpdateOrganizationSettingsRequest.Builder request =
            UpdateOrganizationSettingsRequest.newBuilder()
                .setOrganizationSettings(organizationSettings)
                .setUpdateMask(updateMask);
    
        // Call the API.
        OrganizationSettings response = client.updateOrganizationSettings(request.build());
    
        System.out.println("Organization Settings have been updated:");
        System.out.println(response);
        return response;
      } catch (IOException e) {
        throw new RuntimeException("Couldn't create client.", e);
      }
    }

### Node.js

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library.
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)');
    
    // Creates a new client.
    const client = new [SecurityCenterClient](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)();
    
    async function updateOrgSettings() {
      //  organizationId is the numeric ID of the organization.
      /*
       * TODO(developer): Uncomment the following lines
       */
      // const organizationId = "111122222444";
      const orgName = client.organizationPath(organizationId);
      const [newSettings] = await client.updateOrganizationSettings({
        organizationSettings: {
          name: `${orgName}/organizationSettings`,
          enableAssetDiscovery: true,
        },
        // Only update the enableAssetDiscovery field.
        updateMask: {paths: ['enable_asset_discovery']},
      });
    
      console.log('New settings: %j', newSettings);
    }
    updateOrgSettings();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import securitycenter
    from google.protobuf import field_mask_pb2
    
    # Create the client
    client = securitycenter.SecurityCenterClient()
    # organization_id is numeric ID for the organization. e.g.
    # organization_id = "111112223333"
    org_settings_name = "organizations/{org_id}/organizationSettings".format(
        org_id=organization_id
    )
    # Only update the enable_asset_discovery_value (leave others untouched).
    field_mask = field_mask_pb2.FieldMask(paths=["enable_asset_discovery"])
    # Call the service.
    updated = client.[update_organization_settings](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_organization_settings)(
        request={
            "organization_settings": {
                "name": org_settings_name,
                "enable_asset_discovery": True,
            },
            "update_mask": field_mask,
        }
    )
    print(f"Asset Discovery Enabled? {updated.enable_asset_discovery}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

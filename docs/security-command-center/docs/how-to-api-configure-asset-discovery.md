---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-api-configure-asset-discovery/
title: Configuring asset discovery using the Security Command Center API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:18.376086+00:00
---

# Configuring asset discovery using the Security Command Center API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-api-configure-asset-discovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Configuring asset discovery using the Security Command Center API Stay organized with collections  Save and categorize content based on your preferences. 

**Deprecated:** As of June 20, 2023, the following asset management features of Security Command Center are deprecated:

  * The `Assets` object and related methods and fields in the Security Command Center API and client libraries
  * The `gcloud scc assets` command



If your organization activated Security Command Center **after June 20, 2023** , the preceding features are not included with your activation of Security Command Center, so the asset functionalities documented on this page do not apply to you. 

If your organization activated Security Command Center **before June 20, 2023** , plan to migrate your asset management operations from the Security Command Center API and the `gcloud scc assets` commands to Cloud Asset Inventory by June 20, 2024. These Security Command Center asset management features will be removed from Security Command Center for all users on or after June 20, 2024. 

Cloud Asset Inventory discovers assets automatically, so you do not need to enable or otherwise configure discovery. For more information, see [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/overview). 

The Security Command Center API enables you to control whether asset discovery for Security Command Center is turned on or off for an organization. This guide shows you how to get an organization's current configuration settings and use the API to turn on asset discovery.

Asset discovery is not required unless you are using the deprecated asset functionality of the Security Command Center API or the asset-related Security Command Center commands of the Google Cloud CLI. Asset discovery does not affect the assets that are displayed on the **Assets** page.

**Organization-level activations only** : the information on this page does not apply to [project-level activations of Security Command Center](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#project-level-activation-overview). This page applies only to organization-level activations.

The IAM roles for Security Command Center can be granted at the organization, folder, or project level. Your ability to view, edit, create, or update findings, assets, and security sources depends on the level that you're granted access for. To learn more about Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). 

## Before you begin

Before you configure asset discovery, you need to [authenticate with the Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/reference/authentication).

## Getting organization settings configuration

### Python
    
    
    from google.cloud import securitycenter
    
    client = securitycenter.SecurityCenterClient()
    # organization_id is numeric ID for the organization. e.g.
    # organization_id = "111112223333"
    
    org_settings_name = client.[organization_settings_path](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_organization_settings_path)(organization_id)
    
    org_settings = client.[get_organization_settings](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_get_organization_settings)(request={"name": org_settings_name})
    print(org_settings)

### Java
    
    
    static OrganizationSettings getOrganizationSettings(OrganizationName organizationName) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // Start setting up a request to get OrganizationSettings for.
        // OrganizationName organizationName = OrganizationName.of(/*organizationId=*/"123234324");
        GetOrganizationSettingsRequest.Builder request =
            GetOrganizationSettingsRequest.newBuilder()
                .setName(organizationName.toString() + "/organizationSettings");
    
        // Call the API.
        OrganizationSettings response = client.getOrganizationSettings(request.build());
    
        System.out.println("Organization Settings:");
        System.out.println(response);
        return response;
      } catch (IOException e) {
        throw new RuntimeException("Couldn't create client.", e);
      }
    }

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv1"
    	"cloud.google.com/go/securitycenter/apiv1/securitycenterpb"
    )
    
    // getOrgSettings gets and prints the current organization asset discovery
    // settings to w. orgID is the numeric Organization ID.
    func getOrgSettings(w io.Writer, orgID string) error {
    	// orgID := "12321311"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)() // Closing the client safely cleans up background resources.
    
    	req := &securitycenterpb.GetOrganizationSettingsRequest{
    		Name: fmt.Sprintf("organizations/%s/organizationSettings", orgID),
    	}
    	settings, err := client.GetOrganizationSettings(ctx, req)
    	if err != nil {
    		return fmt.Errorf("GetOrganizationSettings: %w", err)
    	}
    	fmt.Fprintf(w, "Retrieved Settings for: %s\n", settings.Name)
    	fmt.Fprintf(w, "Asset Discovery on? %v", settings.EnableAssetDiscovery)
    	return nil
    }
    

### Node.js
    
    
    // Imports the Google Cloud client library.
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)');
    
    // Creates a new client.
    const client = new [SecurityCenterClient](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)();
    
    async function getOrgSettings() {
      //  organizationId is the numeric ID of the organization.
      /*
       * TODO(developer): Uncomment the following lines
       */
      // const organizaionId = "111122222444";
      const orgName = client.organizationPath(organizationId);
      const [settings] = await client.getOrganizationSettings({
        name: `${orgName}/organizationSettings`,
      });
    
      console.log('Current settings: %j', settings);
    }
    getOrgSettings();

## Turning on asset discovery

The API call below uses a field mask so only the setting for asset discovery is turned on or off.

### Python
    
    
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

### Java
    
    
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

### Go
    
    
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
    

### Node.js
    
    
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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-get-org-settings/
title: Get organization settings \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:48.225134+00:00
---

# Get organization settings  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-get-org-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Get organization settings Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to retrieve organization settings configurations

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
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Node.js

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import securitycenter
    
    client = securitycenter.SecurityCenterClient()
    # organization_id is numeric ID for the organization. e.g.
    # organization_id = "111112223333"
    
    org_settings_name = client.[organization_settings_path](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_organization_settings_path)(organization_id)
    
    org_settings = client.[get_organization_settings](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_get_organization_settings)(request={"name": org_settings_name})
    print(org_settings)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-assets-with-filter/
title: List assets with filter \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:29.872548+00:00
---

# List assets with filter  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-assets-with-filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  List assets with filter Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to filter and list assets by project

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Listing assets using the Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-assets)



## Code sample

### Go

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv1"
    	"cloud.google.com/go/securitycenter/apiv1/securitycenterpb"
    	"google.golang.org/api/iterator"
    )
    
    // listAllProjectAssets lists all current GCP project assets in orgID and
    // prints out results to w. orgID is the numeric organization ID of interest.
    func listAllProjectAssets(w io.Writer, orgID string) error {
    	// orgID := "12321311"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)() // Closing the client safely cleans up background resources.
    	req := &securitycenterpb.ListAssetsRequest{
    		// Parent must be in one of the following formats:
    		//		"organizations/{orgId}"
    		//		"projects/{projectId}"
    		//		"folders/{folderId}"
    		Parent: fmt.Sprintf("organizations/%s", orgID),
    		Filter: `security_center_properties.resource_type="google.cloud.resourcemanager.Project"`,
    	}
    
    	assetsFound := 0
    	it := client.ListAssets(ctx, req)
    	for {
    		result, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("ListAssets: %w", err)
    		}
    		asset := result.Asset
    		properties := asset.SecurityCenterProperties
    		fmt.Fprintf(w, "Asset Name: %s,", asset.Name)
    		fmt.Fprintf(w, "Resource Name %s,", properties.ResourceName)
    		fmt.Fprintf(w, "Resource Type %s\n", properties.ResourceType)
    		assetsFound++
    	}
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static ImmutableList<ListAssetsResult> listAssetsWithFilter(OrganizationName organizationName) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // Start setting up a request to search for all assets in an organization, project, or folder.
        //
        // Parent must be in one of the following formats:
        //    OrganizationName organizationName = OrganizationName.of("organization-id");
        //    ProjectName projectName = ProjectName.of("project-id");
        //    FolderName folderName = FolderName.of("folder-id");
        ListAssetsRequest.Builder request =
            ListAssetsRequest.newBuilder()
                .setParent(organizationName.toString())
                .setFilter(
                    "security_center_properties.resource_type=\"google.cloud.resourcemanager.Project\"");
    
        // Call the API.
        ListAssetsPagedResponse response = client.listAssets(request.build());
    
        // This creates one list for all assets.  If your organization has a large number of assets
        // this can cause out of memory issues.  You can process them incrementally by returning
        // the Iterable returned response.iterateAll() directly.
        ImmutableList<ListAssetsResult> results = ImmutableList.copyOf(response.iterateAll());
        System.out.println("Project assets:");
        System.out.println(results);
        return results;
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
    //  organizationId is the numeric ID of the organization.
    /*
     * TODO(developer): Uncomment the following lines
     */
    // const organizationId = "1234567777";
    const orgName = client.organizationPath(organizationId);
    
    // Call the API with automatic pagination.
    // You can also list assets in a project/ folder. To do so, modify the parent
    // value and filter condition.
    async function listFilteredAssets() {
      const [response] = await client.listAssets({
        parent: orgName,
        filter:
          'security_center_properties.resource_type="google.cloud.resourcemanager.Project"',
      });
      let count = 0;
      Array.from(response).forEach(result =>
        console.log(
          `${++count} ${result.asset.name} ${
            result.asset.securityCenterProperties.resourceName
          } ${result.stateChange}`
        )
      );
    }
    
    listFilteredAssets();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import securitycenter
    
    client = securitycenter.SecurityCenterClient()
    
    # 'parent' must be in one of the following formats:
    #   "organizations/{organization_id}"
    #   "projects/{project_id}"
    #   "folders/{folder_id}"
    parent = f"organizations/{organization_id}"
    
    project_filter = (
        "security_center_properties.resource_type="
        + '"google.cloud.resourcemanager.Project"'
    )
    # Call the API and print results.
    asset_iterator = client.[list_assets](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_assets)(
        request={"parent": parent, "filter": project_filter}
    )
    for i, asset_result in enumerate(asset_iterator):
        print(i, asset_result)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

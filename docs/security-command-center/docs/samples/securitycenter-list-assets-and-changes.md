---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-assets-and-changes/
title: List assets with state change \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:36.991233+00:00
---

# List assets with state change  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-assets-and-changes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  List assets with state change Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to list assets with state changes

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
    	"time"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv1"
    	"cloud.google.com/go/securitycenter/apiv1/securitycenterpb"
    	"github.com/golang/protobuf/ptypes"
    	"google.golang.org/api/iterator"
    )
    
    // listAllProjectAssetsAndStateChange lists all current GCP project assets in
    // orgID and prints the projects and there change from a day ago out to w.
    // orgID is the numeric // organization ID of interest.
    func listAllProjectAssetsAndStateChanges(w io.Writer, orgID string) error {
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
    		Parent:          fmt.Sprintf("organizations/%s", orgID),
    		Filter:          `security_center_properties.resource_type="google.cloud.resourcemanager.Project"`,
    		CompareDuration: ptypes.DurationProto(24 * time.Hour),
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
    		fmt.Fprintf(w, "Resource Type %s", properties.ResourceType)
    		fmt.Fprintf(w, "State Change %s\n", result.StateChange)
    		assetsFound++
    	}
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    static ImmutableList<ListAssetsResult> listAssetAndStatusChanges(
        OrganizationName organizationName, Duration timeSpan, Instant asOf) {
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
        request
            .getCompareDurationBuilder()
            .setSeconds(timeSpan.getSeconds())
            .setNanos(timeSpan.getNano());
    
        // Set read time to either the instant passed in or now.
        asOf = MoreObjects.firstNonNull(asOf, Instant.now());
        request.getReadTimeBuilder().setSeconds(asOf.getEpochSecond()).setNanos(asOf.getNano());
    
        // Call the API.
        ListAssetsPagedResponse response = client.listAssets(request.build());
    
        // This creates one list for all assets.  If your organization has a large number of assets
        // this can cause out of memory issues.  You can process them incrementally by returning
        // the Iterable returned response.iterateAll() directly.
        ImmutableList<ListAssetsResult> results = ImmutableList.copyOf(response.iterateAll());
        System.out.println("Projects:");
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
    // parent: must be in one of the following formats:
    //    `organizations/${organization_id}`
    //    `projects/${project_id}`
    //    `folders/${folder_id}`
    const parent = `organizations/${organizationId}`;
    // Call the API with automatic pagination.
    async function listAssetsAndChanges() {
      const [response] = await client.listAssets({
        parent: parent,
        compareDuration: {seconds: 30 * /*Second in Day=*/ 86400, nanos: 0},
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
    
    listAssetsAndChanges();

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from datetime import timedelta
    
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
    
    # List assets and their state change the last 30 days
    compare_delta = timedelta(days=30)
    
    # Call the API and print results.
    asset_iterator = client.[list_assets](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_assets)(
        request={
            "parent": parent,
            "filter": project_filter,
            "compare_duration": compare_delta,
        }
    )
    for i, asset in enumerate(asset_iterator):
        print(i, asset)
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

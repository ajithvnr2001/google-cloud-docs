---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-assets/
title: Listing assets using the Security Command Center API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:32.622268+00:00
---

# Listing assets using the Security Command Center API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-assets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Listing assets using the Security Command Center API Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

**Deprecated:** As of June 20, 2023, the following asset management features of Security Command Center are deprecated:

  * The `Assets` object and related methods and fields in the Security Command Center API and client libraries
  * The `gcloud scc assets` command



If your organization activated Security Command Center **after June 20, 2023** , the preceding features are not included with your activation of Security Command Center, so the asset functionalities documented on this page do not apply to you. 

If your organization activated Security Command Center **before June 20, 2023** , plan to migrate your asset management operations from the Security Command Center API and the `gcloud scc assets` commands to Cloud Asset Inventory by June 20, 2024. These Security Command Center asset management features will be removed from Security Command Center for all users on or after June 20, 2024. 

To list assets by using Cloud Asset Inventory, see [List assets](https://docs.cloud.google.com/asset-inventory/docs/listing-assets). 

Assets are an organization's Google Cloud resources, like Compute Engine instances or Cloud Storage buckets.

This guide shows you how to use Security Command Center client libraries to access the deprecated records that Security Command Center maintains for the assets in a project or organization.

Security Command Center keeps records for only a subset of the assets in Cloud Asset Inventory. For the most complete list of assets in your environment, use Cloud Asset Inventory to list assets.

For more information, see the following:

  * [Cloud Asset Inventory asset list service](https://docs.cloud.google.com/asset-inventory/docs/listing-assets)
  * [Supported asset types in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/supported-asset-types)



## Grant-levels for IAM roles

The IAM roles for Security Command Center can be granted at the organization, folder, or project level. Your ability to view, edit, create, or update findings, assets, and security sources depends on the level that you're granted access for. To learn more about Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). 

## Before you begin

Before you set up a source, you need to complete the following:

  * [Authenticate with the Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/reference/authentication)



### Page Size

All Security Command Center list APIs are paginated. Each response returns a page of results and a token to return the next page. The page size is configurable. The default pageSize is 10, it can be set to a minimum of 1, and maximum of 1000.

### Resource types

The `resourceType` attribute in Security Command Center uses a different naming convention than [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types). For a list of resource type formats, see [Supported asset types in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/supported-asset-types).

## List all assets

These examples show how to list all assets:

### gcloud

To list all assets in a project, folder, or organization, run the following command:
    
    
    gcloud scc assets list PARENT_ID

Replace `PARENT_ID` with one of the following values:

  * An organization ID in the following format: `ORGANIZATION_ID` (the numerical ID only)
  * A folder ID in the following format: `folders/FOLDER_ID`
  * A project ID in the following format: `projects/PROJECT_ID`



For more examples, run: 
    
    
     gcloud scc assets list --help

For examples in the documentation, see [gcloud scc assets list](https://docs.cloud.google.com/sdk/gcloud/reference/scc/assets/list).

### Python
    
    
    from google.cloud import securitycenter
    
    client = securitycenter.SecurityCenterClient()
    # 'parent' must be in one of the following formats:
    #   "organizations/{organization_id}"
    #   "projects/{project_id}"
    #   "folders/{folder_id}"
    parent = f"organizations/{organization_id}"
    
    # Call the API and print results.
    asset_iterator = client.[list_assets](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_assets)(request={"parent": parent})
    for i, asset_result in enumerate(asset_iterator):
        print(i, asset_result)

### Java
    
    
    static ImmutableList<ListAssetsResult> listAssets(OrganizationName organizationName) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // Start setting up a request to search for all assets in an organization, project, or folder.
        //
        // Parent must be in one of the following formats:
        //    OrganizationName organizationName = OrganizationName.of("organization-id");
        //    ProjectName projectName = ProjectName.of("project-id");
        //    FolderName folderName = FolderName.of("folder-id");
        ListAssetsRequest.Builder request =
            ListAssetsRequest.newBuilder().setParent(organizationName.toString());
    
        // Call the API.
        ListAssetsPagedResponse response = client.listAssets(request.build());
    
        // This creates one list for all assets.  If your organization has a large number of assets
        // this can cause out of memory issues.  You can process them incrementally by returning
        // the Iterable returned response.iterateAll() directly.
        ImmutableList<ListAssetsResult> results = ImmutableList.copyOf(response.iterateAll());
        System.out.println("All assets:");
        System.out.println(results);
        return results;
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
    	"google.golang.org/api/iterator"
    )
    
    // listAllAssets prints every asset to w for orgID. orgID is the numeric
    // Organization ID.
    func listAllAssets(w io.Writer, orgID string) error {
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
    

### Node.js
    
    
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
    async function listAssets() {
      const [response] = await client.listAssets({parent: parent});
      let count = 0;
      Array.from(response).forEach(result =>
        console.log(
          `${++count} ${result.asset.name} ${
            result.asset.securityCenterProperties.resourceName
          }`
        )
      );
    }
    
    listAssets();

The output for each asset is a JSON object that resembles the following:
    
    
    asset:
      createTime: '2020-10-05T17:55:14.823Z'
      iamPolicy:
        policyBlob: '{"bindings":[{"role":"roles/owner","members":["serviceAccount:SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com","user:USER_EMAIL@gmail.com"]}]}'
      name: organizations/ORGANIZATION_ID/assets/ASSET_ID
      resourceProperties:
        createTime: '2020-10-05T17:36:17.915Z'
        lifecycleState: ACTIVE
        name: PROJECT_ID
        parent: '{"id":"ORGANIZATION_ID","type":"organization"}'
        projectId: PROJECT_ID
        projectNumber: 'PROJECT_NUMBER'
      securityCenterProperties:
        resourceDisplayName: PROJECT_ID
        resourceName: //cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER
        resourceOwners:
        - serviceAccount:SERVICE_ACCOUNT@PROJECT_ID.iam.gserviceaccount.com
        - user:USER_EMAIL@gmail.com
        resourceParent: //cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_ID
        resourceParentDisplayName: ORGANIZATION_NAME
        resourceProject: //cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER
        resourceProjectDisplayName: PROJECT_ID
        resourceType: google.cloud.resourcemanager.Project
      securityMarks:
        name: organizations/ORGANIZATION_ID/assets/ASSET_ID/securityMarks
      updateTime: '2020-10-05T17:55:14.823Z'
    
    

## Filter assets

A project, folder, or organization might have many assets. The preceding example doesn't use any filters, so all assets are returned. Security Command Center lets you use asset filters to get information about specific assets. Filters are like "where" clauses in SQL statements except, instead of columns, they apply to the objects returned by the API.

The sample output in the preceding example shows some fields and subfields, and their properties, that can be used in asset filters. Security Command Center supports full JSON arrays and objects as potential property types. You can filter on:

  * Array elements
  * Full JSON objects with partial string match within the object
  * JSON object subfields



Sub-fields must be numbers, strings, or booleans and filter expressions must use the following comparison operators:

  * Strings: 
    * Full equality `=`
    * Partial string matching `:`
  * Numbers: 
    * Inequalities `<`, `>`, `<=`, `>=`
    * Equality `=`
  * Booleans: 
    * Equality `=`



The following examples filter assets:

### gcloud

Use the following command to filter assets:
    
    
    gcloud scc assets list PARENT_ID --filter="FILTER"

Replace the following:

  * `FILTER` with the filter you need to use. For example, the following filter returns only project resources: 
        
        --filter="security_center_properties.resource_type=\"google.cloud.resourcemanager.Project\""

  * `PARENT_ID` with one of the following values: 
    * An organization ID in the following format: `ORGANIZATION_ID` (the numerical ID only)
    * A folder ID in the following format: `folders/FOLDER_ID`
    * A project ID in the following format: `projects/PROJECT_ID`



For more examples, run:
    
    
    gcloud scc assets list --help

For examples in the documentation, see [gcloud scc assets list](https://docs.cloud.google.com/sdk/gcloud/reference/scc/assets/list).

### Python
    
    
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

### Java
    
    
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

### Go
    
    
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
    

### Node.js
    
    
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

## List at a point in time

The previous examples show how to list a current set of assets. Security Command Center also enables you to view a historical snapshot of assets. The following examples return the state of all assets at a specific point in time. Security Command Center supports millisecond time resolutions.

### gcloud

Use the following command to list assets as of a specific point in time:
    
    
    gcloud scc assets list PARENT_ID --read-time="READ_TIME"

Replace the following:

  * `READ_TIME` with the time at which to list assets. Use the following format: `YYYY-MM-DDThh:mm:ss.ffffffZ`. For example: 
        
        --read-time="2022-12-21T07:00:06.861Z"

  * `PARENT_ID` with one of the following values: 
    * An organization ID in the following format: `ORGANIZATION_ID` (the numerical ID only)
    * A project ID in the following format: `projects/PROJECT_ID`
    * A folder ID in the following format: `folders/FOLDER_ID`



For more examples, run:
    
    
    gcloud scc assets list --help

For examples in the documentation, see [gcloud scc assets list](https://docs.cloud.google.com/sdk/gcloud/reference/scc/assets/list).

### Python
    
    
    from datetime import datetime, timedelta, timezone
    
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
    
    # Lists assets as of yesterday.
    read_time = datetime.now(tz=timezone.utc) - timedelta(days=1)
    
    # Call the API and print results.
    asset_iterator = client.[list_assets](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_assets)(
        request={"parent": parent, "filter": project_filter, "read_time": read_time}
    )
    for i, asset_result in enumerate(asset_iterator):
        print(i, asset_result)

### Java
    
    
    static ImmutableList<ListAssetsResult> listAssetsAsOfYesterday(
        OrganizationName organizationName, Instant asOf) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // Start setting up a request to search for all assets in an organization, project, or folder.
        //
        // Parent must be in one of the following formats:
        //    OrganizationName organizationName = OrganizationName.of("organization-id");
        //    ProjectName projectName = ProjectName.of("project-id");
        //    FolderName folderName = FolderName.of("folder-id");
        // Initialize the builder with the parent and filter
        ListAssetsRequest.Builder request =
            ListAssetsRequest.newBuilder()
                .setParent(organizationName.toString())
                .setFilter(
                    "security_center_properties.resource_type=\"google.cloud.resourcemanager.Project\"");
    
        // Set read time to either the instant passed in or one day ago.
        asOf = MoreObjects.firstNonNull(asOf, Instant.now().minus(Duration.ofDays(1)));
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

### Go
    
    
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
    
    // listAllProjectAssets lists all GCP Projects in orgID at asOf time and prints
    // out results to w. orgID is the numeric organization ID of interest.
    func listAllProjectAssetsAtTime(w io.Writer, orgID string, asOf time.Time) error {
    	// orgID := "12321311"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)() // Closing the client safely cleans up background resources.
    
    	// Convert the time to a Timestamp protobuf
    	readTime, err := ptypes.TimestampProto(asOf)
    	if err != nil {
    		return fmt.Errorf("TimestampProto(%v): %w", asOf, err)
    	}
    
    	// You can also list assets in a project/ folder. To do so, modify the parent and
    	// filter condition.
    	req := &securitycenterpb.ListAssetsRequest{
    		// Parent must be in one of the following formats:
    		//		"organizations/{orgId}"
    		//		"projects/{projectId}"
    		//		"folders/{folderId}"
    		Parent:   fmt.Sprintf("organizations/%s", orgID),
    		Filter:   `security_center_properties.resource_type="google.cloud.resourcemanager.Project"`,
    		ReadTime: readTime,
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
    

### Node.js
    
    
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
    
    const oneDayAgo = new Date();
    oneDayAgo.setDate(oneDayAgo.getDate() - 1);
    
    // Call the API with automatic pagination.
    async function listAssetsAtTime() {
      const [response] = await client.listAssets({
        parent: parent,
        filter:
          'security_center_properties.resource_type="google.cloud.resourcemanager.Project"',
        // readTime must be in the form of a google.protobuf.Timestamp object
        // which takes seconds and nanoseconds.
        readTime: {
          seconds: Math.floor(oneDayAgo.getTime() / 1000),
          nanos: (oneDayAgo.getTime() % 1000) * 1e6,
        },
      });
      let count = 0;
      Array.from(response).forEach(result =>
        console.log(
          `${++count} ${result.asset.name} ${
            result.asset.securityCenterProperties.resourceName
          }`
        )
      );
    }
    
    listAssetsAtTime();

## List assets with state changes

Security Command Center lets you compare an asset at two points in time to identify if it was added, removed, or present during the specified time period. The following examples compare projects that exist at `READ_TIME` to a previous point in time specified by `COMPARE_DURATION`. `COMPARE_DURATION` is provided in seconds.

When `COMPARE_DURATION` is set, the `stateChange` attribute on list asset results is updated with one of the following values:

  * `ADDED`: the asset was not present at the start of `compareDuration`, but present at `readTime`.
  * `REMOVED`: the asset was present at the start of `compareDuration`, but not present at `readTime`.
  * `ACTIVE`: the asset was present at both the start and the end of the time period defined by `compareDuration` and `readTime`.




### gcloud

Use the following command to compare the state of assets at two points in time:
    
    
    gcloud scc assets list PARENT_ID \
        --filter="FILTER" \
        --read-time=READ_TIME \
        --compare-duration=COMPARE_DURATION

Replace the following:

  * `COMPARE_DURATION` with a number of seconds that defines a point in time prior to the time that is specified on the `--read-time` flag. For example: 
        
        --compare-duration=84600s

  * `FILTER` with the filter you need to use. For example, the following filter returns only project resources: 
        
        --filter="security_center_properties.resource_type=\"google.cloud.resourcemanager.Project\""

  * `PARENT_ID` with one of the following values: 
    * An organization ID in the following format: `ORGANIZATION_ID` (the numerical ID only)
    * A project ID in the following format: `projects/PROJECT_ID`
    * A folder ID in the following format: `folders/FOLDER_ID`
  * `READ_TIME` with the time at which to list assets. Use the following format: `YYYY-MM-DDThh:mm:ss.ffffffZ`. For example: 
        
        --read-time="2022-12-21T07:00:06.861Z"

For more examples, run:


    
    
    gcloud scc assets list --help

For examples in the documentation, see [gcloud scc assets list](https://docs.cloud.google.com/sdk/gcloud/reference/scc/assets/list).

### Python
    
    
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
    

### Java
    
    
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

### Go
    
    
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
    

### Node.js
    
    
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

**Note:** When `COMPARE_DURATION` is set, sorting list asset results with `ORDER_BY` expressions is not supported. The sort order in `ORDER_BY` expressions is not applied to results.

## Filter examples

The following are some other useful asset filters. You can use `AND` and `OR` in filters to combine parameters and expand or refine results.

### Find a Project Asset with a specific owner
    
    
    "security_center_properties.resource_type = \"google.cloud.resourcemanager.Project\" AND security_center_properties.resource_owners : \"$USER\""
    

`$USER` is typically in the format `user:someone@domain.com`. The comparison for `user` uses the substring operator `:` and an exact match isn't necessary.

### Firewall rules that have open HTTP Ports
    
    
    "security_center_properties.resource_type = \"google.compute.Firewall\" AND resource_properties.name =\"default-allow-http\""
    

### Resources that belong to specific projects
    
    
    "security_center_properties.resource_parent = \"$PROJECT_1_NAME\" OR security_center_properties.resource_parent = \"$PROJECT_2_NAME\""
    

`$PROJECT_1_NAME` and `$PROJECT_2_NAME` are resource identifiers in the form of `//cloudresourcemanager.googleapis.com/projects/$PROJECT_ID`, where `$PROJECT_ID` is the project number. A complete example would be something like: `//cloudresourcemanager.googleapis.com/projects/100090906`

### Finding Compute Engine images whose names contain a specific string

This filter returns Compute Engine images that contain substring "Debia":
    
    
    "security_center_properties.resource_type = \"google.compute.Image\" AND resource_properties.name : \"Debia\""
    

### Resources whose properties contain key-value pairs

This filter returns Cloud Storage buckets where `bucketPolicyOnly` is disabled. The value of `resourceProperties.iamConfiguration` is encoded as a string. You use the `\` character to escape special characters in strings, including the operator `:` between the key name and value.
    
    
    "resourceProperties.iamConfiguration:"\"bucketPolicyOnly\"\:{\"enabled\"\:false""
    

### Finding Project Assets created at or before a specific time

These example filters match assets created at or before July 18, 2019 at 8:26:21PM GMT. With the `create_time` filter, you can express time using the following formats and types:

  * Unix time (in milliseconds) as an integer literal
        
        "create_time <= 1563481581000"
        

  * RFC 3339 as a string literal
        
        "create_time <= \"2019-07-18T20:26:21+00:00\""
        




### Excluding assets from results

To exclude an asset from results, use negation by placing a `-` character in front of a parameter. The operation is similar to using the NOT operator in an SQL statement.

This filter returns all project resources except `Debia`:
    
    
    "security_center_properties.resource_type = \"google.cloud.resourcemanager.Project\" AND -resource_properties.projectId = \"Debia\""
    

## What's next

Learn more about [accessing Security Command Center using a client library](https://docs.cloud.google.com/security-command-center/docs/reference/libraries).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

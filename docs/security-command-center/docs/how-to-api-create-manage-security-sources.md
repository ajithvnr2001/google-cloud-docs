---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-api-create-manage-security-sources/
title: Managing security sources using the Security Command Center API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:30:46.989793+00:00
---

# Managing security sources using the Security Command Center API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-api-create-manage-security-sources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Managing security sources using the Security Command Center API Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This guide walks you through using the Security Command Center API to create a source to generate findings. When you add a source, Security Command Center creates appropriate sources and assigns them the relevant permissions.

The IAM roles for Security Command Center can be granted at the organization, folder, or project level. Your ability to view, edit, create, or update findings, assets, and security sources depends on the level that you're granted access for. To learn more about Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). 

## Before you begin

Before you set up a source, you need to [authenticate with the Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/reference/authentication).

## Creating a source

This example shows how to create a source with a specific display name and description that is used in Security Command Center.

The server automatically assigns an ID to the source.

### REST

In the API, make a request to the [`organizations.sources.create`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources/create) method. The request body contains an instance of [`Source`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources#Source).
    
    
      POST https://securitycenter.googleapis.com/v2/organizations/ORGANIZATION_ID/sources
    
      {
        "name": "SOURCE_NAME",
        "description": "SOURCE_DESCRIPTION",
        "displayName": "DISPLAY_NAME"
      }
    

Replace the following:

  * `ORGANIZATION_ID`: your organization ID.
  * `SOURCE_NAME`: the name of the source.
  * `SOURCE_DESCRIPTION`: a description of the source (max: 1,024 characters).
  * `DISPLAY_NAME`: the display name of the source (between one and 64 characters).



### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv2"
    	"cloud.google.com/go/securitycenter/apiv2/securitycenterpb"
    )
    
    // createSource creates a new source for organization orgID. orgID is
    // the numeric identifier of the organization
    func createSource(w io.Writer, orgID string) error {
    	// orgID := "12321311"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_Close)() // Closing the client safely cleans up background resources.
    
    	req := &securitycenterpb.CreateSourceRequest{
    		Source: &securitycenterpb.Source{
    			DisplayName: "Customized Display Name",
    			Description: "A new custom source that does X",
    		},
    		Parent: fmt.Sprintf("organizations/%s", orgID),
    	}
    	source, err := client.CreateSource(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateSource: %w", err)
    	}
    
    	fmt.Fprintf(w, "New source created: %s\n", source.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_BulkMuteFindingsOperation_Name))
    	fmt.Fprintf(w, "Display Name: %s\n", source.DisplayName)
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.securitycenter.v2.[CreateSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.CreateSourceRequest.html);
    import com.google.cloud.securitycenter.v2.[OrganizationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.OrganizationName.html);
    import com.google.cloud.securitycenter.v2.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html);
    import com.google.cloud.securitycenter.v2.[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source.html);
    import java.io.IOException;
    
    public class CreateSource {
    
      public static void main(String[] args) throws IOException {
        // TODO: Replace the sample resource name
        // organizationId: Google Cloud Organization id.
        String organizationId = "{google-cloud-organization-id}";
    
        createSource(organizationId);
      }
    
      /**
       * Creates a new "source" in the Security Command Center.
       */
      public static [Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source.html) createSource(String organizationId) throws IOException {
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html).create()) {
          // Start setting up a request to create a source in an organization.
          [OrganizationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.OrganizationName.html) organizationName = [OrganizationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.OrganizationName.html).of(organizationId);
    
          [Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source.html) source =
              [Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source.html).newBuilder()
                  .setDisplayName("Custom display name")
                  .setDescription("A source that does X")
                  .build();
    
          [CreateSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.CreateSourceRequest.html) createSourceRequest =
              [CreateSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.CreateSourceRequest.html).newBuilder()
                  .setParent(organizationName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.OrganizationName.html#com_google_cloud_securitycenter_v2_OrganizationName_toString__)())
                  .setSource(source)
                  .build();
    
          // The source is not visible in the Security Command Center dashboard
          // until it generates findings.
          [Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source.html) response = client.createSource(createSourceRequest);
          return response;
        }
      }
    }

### Node.js
    
    
    // Import the Google Cloud client library.
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)').v2;
    
    // Create a new Security Center client
    const client = new [SecurityCenterClient](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)();
    
    // TODO(developer): Update for your own environment.
    const organizationId = '1081635000895';
    
    // Resource name of the new source's parent. Format is:
    // "organizations/[organization_id]".
    const parent = client.organizationPath(organizationId);
    
    // The source object.
    const source = {
      displayName: 'Customized Display Name V2',
      description: 'A new custom source that does X',
    };
    
    // Build the create source request.
    const createSourceRequest = {
      parent,
      source,
    };
    
    // The source is not visible in the Security Command Center dashboard
    // until it generates findings.
    // Call the API
    async function createSource() {
      const [source] = await client.createSource(createSourceRequest);
      console.log('New Source created: %j', source);
    }
    
    await createSource();

### Python
    
    
    def create_source(organization_id) -> Dict:
        """
        Create a new findings source
        Args:
            organization_id: organization_id is the numeric ID of the organization. e.g.:organization_id = "111122222444"
        Returns:
             Dict: returns the created findings source details.
        """
        from google.cloud import securitycenter_v2
    
        client = securitycenter_v2.SecurityCenterClient()
        org_name = f"organizations/{organization_id}"
    
        response = client.[create_source](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_create_source)(
            request={
                "parent": org_name,
                "source": {
                    "display_name": "Customized Display Name",
                    "description": "A new custom source that does X",
                },
            }
        )
        print(f"Created Source: {response.name}")
        return response
    
    

The source is not visible in the Security Command Center console until it generates findings. You can verify it was created by following the instructions in [Get a specific source](https://docs.cloud.google.com/security-command-center/docs/how-to-api-create-manage-security-sources#get_a_specific_source).

## Updating a source

You can update a source's display name and description after it's created. You can also use a field mask to update only one field. The following example uses a field mask to only update the display name, leaving the description unchanged.

**Note:** Sources cannot be deleted or disabled.

### REST

In the API, make a request to the [`organizations.sources.patch`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources/patch) method. The request body contains an instance of [`Source`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources#Source).
    
    
      PATCH https://securitycenter.googleapis.com/v2/organizations/ORGANIZATION_ID/sources/SOURCE_ID?updateMask=displayName -d
    
      {
        "description": "SOURCE_DESCRIPTION",
        "displayName": "DISPLAY_NAME",
      }
    

Replace the following:

  * `ORGANIZATION_ID`: your organization ID.
  * `SOURCE_ID`: the source ID; to learn how to find a source ID, see [Getting the source ID](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications#get-source-id).
  * `SOURCE_DESCRIPTION`: a description of the source (max: 1024 characters).
  * `DISPLAY_NAME`: the display name of the source (between one and 64 characters).



### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv2"
    	"cloud.google.com/go/securitycenter/apiv2/securitycenterpb"
    	"google.golang.org/genproto/protobuf/field_mask"
    )
    
    // updateSource changes a sources display name to "New Display Name" for a
    // specific source. sourceName is the full resource name of the source to be
    // updated.
    func updateSource(w io.Writer, sourceName string) error {
    	// sourceName := "organizations/111122222444/sources/1234"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_Close)() // Closing the client safely cleans up background resources.
    
    	req := &securitycenterpb.UpdateSourceRequest{
    		Source: &securitycenterpb.Source{
    			Name:        sourceName,
    			DisplayName: "New Display Name",
    		},
    		// Only update the display name field (if not set all mutable
    		// fields of the source will be updated.
    		UpdateMask: &field_mask.FieldMask{
    			Paths: []string{"display_name"},
    		},
    	}
    	source, err := client.UpdateSource(ctx, req)
    	if err != nil {
    		return fmt.Errorf("UpdateSource: %w", err)
    	}
    	fmt.Fprintf(w, "Source Name: %s, ", source.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_BulkMuteFindingsOperation_Name))
    	fmt.Fprintf(w, "Display name: %s, ", source.DisplayName)
    	fmt.Fprintf(w, "Description: %s\n", source.Description)
    
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.securitycenter.v2.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html);
    import com.google.cloud.securitycenter.v2.[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source.html);
    import com.google.cloud.securitycenter.v2.[SourceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SourceName.html);
    import com.google.cloud.securitycenter.v2.[UpdateSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateSourceRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    
    public class UpdateSource {
    
      public static void main(String[] args) throws IOException {
        // TODO: Replace the below variables.
        // organizationId: Google Cloud Organization id.
        String organizationId = "{google-cloud-organization-id}";
    
        // Specify the source-id.
        String sourceId = "{source-id}";
    
        updateSource(organizationId, sourceId);
      }
    
      // Demonstrates how to update a source.
      public static [Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source.html) updateSource(String organizationId, String sourceId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html).create()) {
    
          // Start setting up a request to get a source.
          [SourceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SourceName.html) sourceName = [SourceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SourceName.html).[ofOrganizationSourceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SourceName.html#com_google_cloud_securitycenter_v2_SourceName_ofOrganizationSourceName_java_lang_String_java_lang_String_)(organizationId, sourceId);
          [Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source.html) source = [Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source.html).newBuilder()
              .setDisplayName("Updated Display Name")
              .setName(sourceName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SourceName.html#com_google_cloud_securitycenter_v2_SourceName_toString__)())
              .build();
    
          // Set the update mask to specify which properties should be updated.
          // If empty, all mutable fields will be updated.
          // For more info on constructing field mask path, see the proto or:
          // https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) updateMask = [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder()
              .[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("display_name")
              .build();
    
          [UpdateSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateSourceRequest.html) request = [UpdateSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateSourceRequest.html).newBuilder()
              .setSource(source)
              .setUpdateMask(updateMask)
              .build();
    
          // Call the API.
          [Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source.html) response = client.updateSource(request);
    
          System.out.println("Updated Source: " + response);
          return response;
        }
      }
    }

### Node.js
    
    
    // npm install '@google-cloud/security-center'
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)').v2;
    
    const client = new [SecurityCenterClient](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)();
    
    // TODO(developer): Update the following for your own environment.
    const organizationId = '1081635000895';
    const location = 'global';
    
    async function createSampleFinding() {
      const uuid = require('uuid');
    
      const [source] = await client.createSource({
        source: {
          displayName: 'Customized Display Name V2',
          description: 'A new custom source that does X',
        },
        parent: client.organizationPath(organizationId),
      });
    
      const sourceId = source.name.split('/')[3];
    
      // Resource name of the new finding's parent. Examples:
      //  - `organizations/[organization_id]/sources/[source_id]`
      //  - `organizations/[organization_id]/sources/[source_id]/locations/[location_id]`
      const parent = `organizations/${organizationId}/sources/${sourceId}/locations/${location}`;
    
      // The resource this finding applied to. The Cloud Security Command Center UI can link the
      // findings for a resource to the corresponding asset of a resource if there are matches.
      const resourceName = `//cloudresourcemanager.googleapis.com/organizations/${organizationId}`;
    
      // Unique identifier provided by the client within the parent scope.
      // It must be alphanumeric and less than or equal to 32 characters and
      // greater than 0 characters in length.
      const findingId = uuid.v4().replace(/-/g, '');
    
      // Get the current timestamp.
      const eventDate = new Date();
    
      // Finding category.
      const category = 'MEDIUM_RISK_ONE';
    
      // Build the finding request object.
      const createFindingRequest = {
        parent: parent,
        findingId: findingId,
        finding: {
          resourceName,
          category,
          state: 'ACTIVE',
          // The time associated with discovering the issue.
          eventTime: {
            seconds: Math.floor(eventDate.getTime() / 1000),
            nanos: (eventDate.getTime() % 1000) * 1e6,
          },
        },
      };
    
      await client.createFinding(createFindingRequest);
      return sourceId;
    }
    
    const sourceId = await createSampleFinding();
    
    /**
     *  Required. The source resource to update.
     */
    const sourceName = client.organizationSourcePath(organizationId, sourceId);
    
    // Set the update mask to specify which properties should be updated.
    // If empty, all mutable fields will be updated.
    // For more info on constructing field mask path, see the proto or:
    // https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask
    const updateMask = {
      paths: ['display_name'],
    };
    
    // Build the request.
    
    const source = {
      name: sourceName,
      displayName: 'New Display Name',
    };
    
    async function updateSource() {
      const [response] = await client.updateSource({updateMask, source});
      console.log('Updated Source: %j', response);
    }
    
    await updateSource();

### Python
    
    
    def update_source(source_name) -> Dict:
        """
        Updates a source's display name.
        Args:
            source_name: is the resource path for a source that has been created
        Returns:
             Dict: returns the details of updated source.
        """
        from google.cloud import securitycenter_v2
        from google.protobuf import field_mask_pb2
    
        client = securitycenter_v2.SecurityCenterClient()
    
        # Field mask to only update the display name.
        field_mask = field_mask_pb2.FieldMask(paths=["display_name"])
    
        # 'source_name' is the resource path for a source that has been
        # created previously (you can use list_sources to find a specific one).
        # Its format is:
        # source_name = "organizations/{organization_id}/sources/{source_id}"
        # e.g.:
        # source_name = "organizations/111122222444/sources/1234"
        updated = client.[update_source](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_source)(
            request={
                "source": {"name": source_name, "display_name": "Updated Display Name"},
                "update_mask": field_mask,
            }
        )
        print(f"Updated Source: {updated}")
        return updated
    
    

## Get a specific source

Verify that a source is created or updated appropriately by querying Security Command Center with the source's absolute resource name:

### gcloud
    
    
    gcloud scc sources describe ORGANIZATION_ID --source=SOURCE_ID

Replace the following:

  * `ORGANIZATION_ID`: your organization ID.
  * `SOURCE_ID`: the source ID.



### REST

In the API, make a request to the [`organizations.sources.get`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources/get) method:
    
    
    GET https://securitycenter.googleapis.com/v2/organizations/ORGANIZATION_ID/sources/SOURCE_ID
    

Replace the following:

  * `ORGANIZATION_ID`: your organization ID.
  * `SOURCE_ID`: the source ID.



### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv2"
    	"cloud.google.com/go/securitycenter/apiv2/securitycenterpb"
    )
    
    // getSource retrieves a source by its resource name and print it to w.
    // sourceName is the full resource name of the source to be updated.
    func getSource(w io.Writer, sourceName string) error {
    	// sourceName := "organizations/111122222444/sources/1234"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_Close)() // Closing the client safely cleans up background resources.
    
    	req := &securitycenterpb.GetSourceRequest{
    		Name: sourceName,
    	}
    	source, err := client.GetSource(ctx, req)
    	if err != nil {
    		return fmt.Errorf("GetSource: %w", err)
    	}
    	fmt.Fprintf(w, "Source: %v\n", source.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_BulkMuteFindingsOperation_Name))
    	fmt.Fprintf(w, "Display Name: %v\n", source.DisplayName)
    	fmt.Fprintf(w, "Description: %v\n", source.Description)
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.securitycenter.v2.[GetSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.GetSourceRequest.html);
    import com.google.cloud.securitycenter.v2.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html);
    import com.google.cloud.securitycenter.v2.[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source.html);
    import com.google.cloud.securitycenter.v2.[SourceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SourceName.html);
    import java.io.IOException;
    
    public class GetSource {
    
      public static void main(String[] args) throws IOException {
        // TODO: Replace the below variables.
        // organizationId: Google Cloud Organization id.
        String organizationId = "{google-cloud-organization-id}";
    
        // Specify the source-id.
        String sourceId = "{source-id}";
    
        getSource(organizationId, sourceId);
      }
    
      // Demonstrates how to retrieve a specific source.
      public static [Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source.html) getSource(String organizationId, String sourceId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html).create()) {
    
          // Start setting up a request to get a source.
          [SourceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SourceName.html) sourceName = [SourceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SourceName.html).[ofOrganizationSourceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SourceName.html#com_google_cloud_securitycenter_v2_SourceName_ofOrganizationSourceName_java_lang_String_java_lang_String_)(organizationId, sourceId);
    
          [GetSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.GetSourceRequest.html) request = [GetSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.GetSourceRequest.html).newBuilder()
              .setName(sourceName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SourceName.html#com_google_cloud_securitycenter_v2_SourceName_toString__)())
              .build();
    
          // Call the API.
          [Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source.html) response = client.getSource(request);
    
          System.out.println("Source: " + response);
          return response;
        }
      }
    }

### Node.js
    
    
    // Imports the Google Cloud client library.
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)').v2;
    
    // Create a Security Center client
    const client = new [SecurityCenterClient](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)();
    
    // TODO(developer): Update the following for your own environment.
    const organizationId = '1081635000895';
    const location = 'global';
    
    async function createSampleFinding() {
      const uuid = require('uuid');
    
      const [source] = await client.createSource({
        source: {
          displayName: 'Customized Display Name V2',
          description: 'A new custom source that does X',
        },
        parent: client.organizationPath(organizationId),
      });
    
      const sourceId = source.name.split('/')[3];
    
      // Resource name of the new finding's parent. Examples:
      //  - `organizations/[organization_id]/sources/[source_id]`
      //  - `organizations/[organization_id]/sources/[source_id]/locations/[location_id]`
      const parent = `organizations/${organizationId}/sources/${sourceId}/locations/${location}`;
    
      // The resource this finding applied to. The Cloud Security Command Center UI can link the
      // findings for a resource to the corresponding asset of a resource if there are matches.
      const resourceName = `//cloudresourcemanager.googleapis.com/organizations/${organizationId}`;
    
      // Unique identifier provided by the client within the parent scope.
      // It must be alphanumeric and less than or equal to 32 characters and
      // greater than 0 characters in length.
      const findingId = uuid.v4().replace(/-/g, '');
    
      // Get the current timestamp.
      const eventDate = new Date();
    
      // Finding category.
      const category = 'MEDIUM_RISK_ONE';
    
      // Build the finding request object.
      const createFindingRequest = {
        parent: parent,
        findingId: findingId,
        finding: {
          resourceName,
          category,
          state: 'ACTIVE',
          // The time associated with discovering the issue.
          eventTime: {
            seconds: Math.floor(eventDate.getTime() / 1000),
            nanos: (eventDate.getTime() % 1000) * 1e6,
          },
        },
      };
    
      await client.createFinding(createFindingRequest);
      return sourceId;
    }
    
    const sourceId = await createSampleFinding();
    
    // Relative resource name of the source. Its format is
    // "organizations/[organization_id]/source/[source_id]".
    const name = `organizations/${organizationId}/sources/${sourceId}`;
    
    // Build the request.
    const getSourceRequest = {
      name,
    };
    
    async function getSource() {
      // Call the API.
      const [source] = await client.getSource(getSourceRequest);
      console.log('Source: %j', source);
    }
    
    await getSource();

### Python
    
    
    def get_source(source_name) -> Dict:
        """
        Gets the details of an existing source.
        Args:
            source_name: is the resource path for a source that has been created
        Returns:
             Dict: returns the details of existing source.
        """
        from google.cloud import securitycenter_v2
    
        client = securitycenter_v2.SecurityCenterClient()
    
        # 'source_name' is the resource path for a source that has been
        # created previously (you can use list_sources to find a specific one).
        # Its format is:
        # source_name = "organizations/{organization_id}/sources/{source_id}"
        # e.g.:
        # source_name = "organizations/111122222444/sources/1234"
        source = client.[get_source](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_get_source)(request={"name": source_name})
    
        print(f"Source: {source}")
        return source
    
    

## Listing sources

Security Command Center lets you list a specific source, or all sources available in an organization:

### REST

In the API, make a request to the [`organizations.sources.list`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources/list) method:
    
    
    GET https://securitycenter.googleapis.com/v2/organizations/ORGANIZATION_ID/sources
    

Replace the following:

  * `ORGANIZATION_ID`: your organization ID.



### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv2"
    	"cloud.google.com/go/securitycenter/apiv2/securitycenterpb"
    	"google.golang.org/api/iterator"
    )
    
    // listSources prints all sources in  orgID to w.  orgID is the numeric
    // identifier of the organization.
    func listSources(w io.Writer, orgID string) error {
    	// orgID := "12321311"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_Close)() // Closing the client safely cleans up background resources.
    
    	req := &securitycenterpb.ListSourcesRequest{
    		// Parent must be in one of the following formats:
    		//		"organizations/{orgId}"
    		//		"projects/{projectId}"
    		//		"folders/{folderId}"
    		Parent: fmt.Sprintf("organizations/%s", orgID),
    	}
    	it := client.ListSources(ctx, req)
    	for {
    		source, err := it.Next()
    		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_BulkMuteFindingsOperation_Done) {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("it.Next: %w", err)
    		}
    		fmt.Fprintf(w, "Source Name: %s, ", source.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_BulkMuteFindingsOperation_Name))
    		fmt.Fprintf(w, "Display name: %s, ", source.DisplayName)
    		fmt.Fprintf(w, "Description: %s\n", source.Description)
    	}
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.securitycenter.v2.[OrganizationLocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.OrganizationLocationName.html);
    import com.google.cloud.securitycenter.v2.[OrganizationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.OrganizationName.html);
    import com.google.cloud.securitycenter.v2.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html);
    import com.google.cloud.securitycenter.v2.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html).[ListSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListSourcesPagedResponse.html);
    import com.google.cloud.securitycenter.v2.[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    public class ListSources {
    
      public static void main(String[] args) throws IOException {
        // TODO: Replace the below variables.
        // organizationId: Google Cloud Organization id.
        String organizationId = "{google-cloud-organization-id}";
    
        listSources(organizationId);
      }
    
      // Demonstrates how to list all security sources in an organization.
      public static List<Source> listSources(String organizationId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html).create()) {
    
          // Start setting up a request to get a source.
          [OrganizationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.OrganizationName.html) parent = [OrganizationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.OrganizationName.html).of(organizationId);
    
          // Call the API.
          List<Source> sourcesList = new ArrayList<>();
          [ListSourcesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.ListSourcesPagedResponse.html) response = client.listSources(parent);
          response.iterateAll().forEach(sourcesList::add);
    
          for ([Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Source.html) source : sourcesList) {
            System.out.println("List sources: " + source);
          }
          return sourcesList;
        }
      }
    }

### Node.js
    
    
    // Imports the Google Cloud client library.
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)').v2;
    
    const client = new [SecurityCenterClient](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)();
    
    // TODO(developer): Update the following for your own environment.
    const organizationId = '1081635000895';
    
    // Required. Resource name of the parent of sources to list. Its format should
    // be "organizations/[organization_id]", "folders/[folder_id]", or
    // "projects/[project_id]".
    const parent = `organizations/${organizationId}`;
    
    // Build the request.
    const listSourcesRequest = {
      parent,
    };
    
    async function listAllSources() {
      // Call the API.
      const iterable = client.listSourcesAsync(listSourcesRequest);
      let count = 0;
      console.log('Sources:');
      for await (const response of iterable) {
        console.log(`${++count} ${response.name} ${response.description}`);
      }
    }
    
    await listAllSources();

### Python
    
    
    def list_source(organization_id) -> int:
        """
        lists the findings source
        Args:
            organization_id: organization_id is the numeric ID of the organization. e.g.:organization_id = "111122222444"
        Returns:
             Dict: returns the count of the findings source
        """
        count = -1
        from google.cloud import securitycenter_v2
    
        # Create a new client.
        client = securitycenter_v2.SecurityCenterClient()
        # 'parent' must be in one of the following formats:
        #   "organizations/{organization_id}"
        #   "projects/{project_id}"
        #   "folders/{folder_id}"
        parent = f"organizations/{organization_id}"
    
        # Call the API and print out each existing source.
        for count, source in enumerate(client.[list_sources](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_sources)(request={"parent": parent})):
            print(count, source)
        return count
    
    

## What's next

  * Learn more about [client libraries for Security Command Center](https://docs.cloud.google.com/security-command-center/docs/reference/libraries).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

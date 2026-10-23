---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-api-add-manage-security-marks/
title: Managing security marks using the Security Command Center API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:03.170786+00:00
---

# Managing security marks using the Security Command Center API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-api-add-manage-security-marks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Managing security marks using the Security Command Center API Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This guide describes how to use the Security Command Center Security Command Center API to manage security marks. Security marks, or "marks", are customizable annotations on assets or findings in Security Command Center that let you add your own business context to these objects.

You can add or update security marks only on assets that are supported by Security Command Center. For a list of the assets that Security Command Center supports, see [Supported asset types in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/supported-asset-types).

## Before you begin

Before you can work with security marks, you need to [Set up a service account and SDK](https://docs.cloud.google.com/security-command-center/docs/how-to-programmatic-access).

To add or change security marks, you must have an Identity and Access Management role that includes permissions for the kind of mark that you want to use:

  * Asset marks: **Asset Security Marks Writer** , `securitycenter.assetSecurityMarksWriter`
  * Finding marks: **Finding Security Marks Writer** , `securitycenter.findingSecurityMarksWriter`



For more information about IAM roles in Security Command Center, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). To learn how to use security marks effectively, see [Annotate findings with security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-findings) and [Annotate assets with security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-assets).

## Adding or updating security marks on assets

When using the Security Command Center API, adding and updating security marks are the same operation. The example shows how to add security marks for the key-value pairs `(key_a, value_a)` and `(key_b, value_b)`.

The following code uses field masks to ensure that only those values are updated. If field masks aren't provided, all security marks are cleared before adding the given keys and values.

### gcloud
    
    
    gcloud scc assets update-marks ASSET_ID \
        --PARENT=PARENT_ID \
        --location=LOCATION \
        --security-marks=SECURITY_MARKS \
        --update-mask=UPDATE_MASK

Replace the following:

  * `ASSET_ID`: the asset to update.
  * `PARENT`: the level of the resource hierarchy where the asset is located; use `organization`, `folder`, or `project`.
  * `PARENT_ID`: the numeric ID of the parent organization, folder, or project, or the alphanumeric ID of the parent project.
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to update a security mark on an asset; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`.
  * `SECURITY_MARKS`: comma-separated key-value pairs that represent security marks and their values; for example, `key_a=value_a,key_b=value_b`.
  * `UPDATE_MASK`: comma-separated list of security mark fields to update for the asset; for example, `marks.key_a,marks.key_b`.



### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv2"
    	"cloud.google.com/go/securitycenter/apiv2/securitycenterpb"
    	"google.golang.org/genproto/protobuf/field_mask"
    )
    
    // addSecurityMarks adds/updates the security marks for the assetName.
    // Specifically, it sets "key_a" and "key_b" to "value_a" and "value_b"
    // respectively.  assetName is the resource path for an asset.
    func addSecurityMarks(w io.Writer, assetName string) error {
    	// Specify the value of 'assetName' in one of the following formats:
    	// 		assetName := "organizations/{org_id}/locations/{location_id}/assets/{asset_id}"
    	//		assetName := "projects/{project_id}/locations/{location_id}/assets/{asset_id}"
    	//		assetName := "folders/{folder_id}/locations/{location_id}/assets/{asset_id}"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_Close)() // Closing the client safely cleans up background resources.
    
    	req := &securitycenterpb.UpdateSecurityMarksRequest{
    		// If not set or empty, all marks would be cleared before
    		// adding the new marks below.
    		UpdateMask: &field_mask.FieldMask{
    			Paths: []string{"marks.key_a", "marks.key_b"},
    		},
    		SecurityMarks: &securitycenterpb.SecurityMarks{
    			Name: fmt.Sprintf("%s/securityMarks", assetName),
    			// Note keys correspond to the last part of each path.
    			Marks: map[string]string{"key_a": "value_a", "key_b": "value_b"},
    		},
    	}
    	updatedMarks, err := client.UpdateSecurityMarks(ctx, req)
    	if err != nil {
    		return fmt.Errorf("UpdateSecurityMarks: %w", err)
    	}
    
    	fmt.Fprintf(w, "Updated marks: %s\n", updatedMarks.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_BulkMuteFindingsOperation_Name))
    	for k, v := range updatedMarks.Marks {
    		fmt.Fprintf(w, "%s = %s\n", k, v)
    	}
    	return nil
    
    }
    

### Python
    
    
    def add_to_finding(organization_id, source_name, location_id, finding_name):
        """
        Adds security marks to a finding.
        Args:
           organization_id: organization_id is the numeric ID of the organization. e.g.:organization_id = "111122222444"
           source_name: is the resource path for a source that has been created
           location_id: Gcp location id; example: 'global'
           finding_name: finding name to add security marks.
    
        Returns:
            Dict: returns the deleted security marks response.
        """
        from google.cloud import securitycenter_v2
        from google.protobuf import field_mask_pb2
    
        client = securitycenter_v2.SecurityCenterClient()
        finding_name = f"organizations/{organization_id}/sources/{source_name}/locations/{location_id}/findings/{finding_name}"
        finding_marks_name = f"{finding_name}/securityMarks"
    
        # Notice the suffix after "marks." in the field mask matches the keys
        # in marks.
        field_mask = field_mask_pb2.FieldMask(
            paths=["marks.finding_key_a", "marks.finding_key_b"]
        )
        marks = {"finding_key_a": "value_a", "finding_key_b": "value_b"}
    
        updated_marks = client.[update_security_marks](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_security_marks)(
            request={
                "security_marks": {"name": finding_marks_name, "marks": marks},
                "update_mask": field_mask,
            }
        )
        return updated_marks, marks
    
    

Read [Manage policies](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-assets#managing_policies) for information about dedicated asset marks for Security Health Analytics detectors.

## Deleting security marks on assets

Deleting specific security marks is accomplished in a similar fashion to adding or updating them, specifically calling update with a field mask but without any corresponding value. In the example, security marks with keys `key_a` and `key_b` are deleted.

### gcloud
    
    
    gcloud scc assets update-marks ASSET_ID \
      --PARENT=PARENT_ID \
      --location=LOCATION \
      --update-mask=UPDATE_MASK

  * `ASSET_ID`: the asset to update.
  * `PARENT`: the level of the resource hierarchy where the asset is located; use `organization`, `folder`, or `project`.
  * `PARENT_ID`: the numeric ID of the parent organization, folder, or project, or the alphanumeric ID of the parent project.
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to delete a security mark from an asset; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`.
  * `UPDATE_MASK`: comma-separated list of security mark fields to delete from the asset; for example, `marks.key_a,marks.key_b`.



### Node.js
    
    
    // Imports the Google Cloud client library.
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)').v2;
    
    // Creates a new client.
    const client = new [SecurityCenterClient](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)();
    
    // Build the full resource path for the finding to update.
    /*
     * TODO(developer): Update the following references for your own environment before running the sample.
     */
    // const organizationId = 'YOUR_ORGANIZATION_ID';
    // const sourceId = 'SOURCE_ID';
    // const location = 'LOCATION_ID';
    const findingName = `organizations/${organizationId}/sources/${sourceId}/locations/${location}/findings/${findingId}`;
    
    // Construct the request to be sent by the client.
    const updateSecurityMarksRequest = {
      securityMarks: {
        name: `${findingName}/securityMarks`,
        // Intentionally, not setting marks to delete them.
      },
      // Only delete marks for the following keys.
      updateMask: {paths: ['marks.key_a', 'marks.key_b']},
    };
    
    async function deleteSecurityMarks() {
      const [newMarks] = await client.updateSecurityMarks(
        updateSecurityMarksRequest
      );
    
      console.log('Updated marks: %j', newMarks);
    }
    deleteSecurityMarks();

### Python
    
    
    def delete_security_marks(organization_id, asset_name) -> Dict:
        """
        Removes security marks from an asset.
        Args:
           organization_id: organization_id is the numeric ID of the organization. e.g.:organization_id = "111122222444"
           asset_name: is the resource path for an asset that exists in SCC
    
        Returns:
            Dict: returns the deleted security marks response.
        """
        # Make sure they are there first
        add_to_asset(organization_id, asset_name)
        from google.cloud import securitycenter_v2
        from google.protobuf import field_mask_pb2
    
        # Create a new client.
        client = securitycenter_v2.SecurityCenterClient()
        asset_name = f"organizations/{organization_id}/assets/{asset_name}"
        marks_name = f"{asset_name}/securityMarks"
    
        field_mask = field_mask_pb2.FieldMask(paths=["marks.key_a", "marks.key_b"])
    
        updated_marks = client.[update_security_marks](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_security_marks)(
            request={
                "security_marks": {
                    "name": marks_name
                    # Note, no marks specified, so the specified values in
                    # the fields masks will be deleted.
                },
                "update_mask": field_mask,
            }
        )
        print(updated_marks)
        return updated_marks
    
    

## Adding and deleting security marks in the same request

The technique to add and update security marks and deleting security marks can be combined into the same request. In the example, `key_a` is updated, and `key_b` is deleted.

### gcloud
    
    
    gcloud scc assets update-marks ASSET_ID \
        --PARENT=PARENT_ID \
        --location=LOCATION \
        --update-mask=UPDATE_MASK

  * `ASSET_ID`: the asset to update.
  * `PARENT`: the level of the resource hierarchy where the asset is located; use `organization`, `folder`, or `project`.
  * `PARENT_ID`: the numeric ID of the parent organization, folder, or project, or the alphanumeric ID of the parent project.
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to update and delete security marks for an asset; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`.
  * `SECURITY_MARKS`: comma-separated key-value pairs that represent security marks that you want to update; for example, `key_a=value_a`; omit security marks that you want to delete
  * `UPDATE_MASK`: comma-separated list of security mark fields to update or delete; for example, `marks.key_a,marks.key_b`.



### Node.js
    
    
    // Imports the Google Cloud client library.
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)').v2;
    
    // Creates a new client.
    const client = new [SecurityCenterClient](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)();
    
    // Build the full resource path for the finding to update.
    /*
     * TODO(developer): Update the following references for your own environment before running the sample.
     */
    // const organizationId = 'YOUR_ORGANIZATION_ID';
    // const sourceId = 'SOURCE_ID';
    const findingName = `organizations/${organizationId}/sources/${sourceId}/locations/${location}/findings/${findingId}`;
    
    // Construct the request to be sent by the client.
    const updateSecurityMarksRequest = {
      securityMarks: {
        name: `${findingName}/securityMarks`,
        marks: {key_a: 'new_value_for_a'},
      },
      // Set the update mask to specify which properties should be updated.
      // If empty, all mutable fields will be updated.
      // For more info on constructing field mask path, see the proto or:
      // https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.
      // Since no marks have been added, including "marks.key_b" in the update mask
      // will cause it to be deleted.
      updateMask: {paths: ['marks.key_a', 'marks.key_b']},
    };
    
    async function UpdateAndDeleteSecurityMarks() {
      const [newMarks] = await client.updateSecurityMarks(
        updateSecurityMarksRequest
      );
    
      console.log('New marks: %j', newMarks);
    }
    UpdateAndDeleteSecurityMarks();

### Python
    
    
    def delete_and_update_marks(organization_id, asset_name) -> Dict:
        """
        Updates and deletes security marks from an asset in the same call.
        Args:
           organization_id: organization_id is the numeric ID of the organization. e.g.:organization_id = "111122222444"
           asset_name: is the resource path for an asset that exists in SCC
    
        Returns:
            Dict: returns the deleted security marks response.
    
        """
        # Make sure they are there first
        add_to_asset(organization_id, asset_name)
        from google.cloud import securitycenter_v2
        from google.protobuf import field_mask_pb2
    
        client = securitycenter_v2.SecurityCenterClient()
        asset_name = f"organizations/{organization_id}/assets/{asset_name}"
        marks_name = f"{asset_name}/securityMarks"
    
        field_mask = field_mask_pb2.FieldMask(paths=["marks.key_a", "marks.key_b"])
        marks = {"key_a": "new_value_for_a"}
    
        updated_marks = client.[update_security_marks](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_security_marks)(
            request={
                "security_marks": {"name": marks_name, "marks": marks},
                "update_mask": field_mask,
            }
        )
        print(updated_marks)
        return updated_marks
    
    

## Adding security marks to findings

Adding, updating, and deleting security marks on findings follows the same process as updating security marks on assets. The only change is the name of the resource used in the API call. Instead of an asset resource, you provide a finding resource name.

For example, to update security marks on a finding, use the following code:

### gcloud
    
    
    gcloud scc findings update-marks FINDING_NAME \
        --PARENT=PARENT_ID \
        --location=LOCATION \
        --source=SOURCE_ID \
        --security-marks=SECURITY_MARKS \
        --update-mask=UPDATE_MASK

Replace the following:

  * `FINDING_NAME`: the finding to update.
  * `PARENT`: the level of the resource hierarchy where the finding is located; use `organization`, `folder`, or `project`.
  * `PARENT_ID`: the numeric ID of the parent organization, folder, or project, or the alphanumeric ID of the parent project.
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to update a security mark on a finding; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`.
  * `SOURCE_ID`: the source ID.
  * `SECURITY_MARKS`: comma-separated key-value pairs that represent security marks and their values; for example, `key_a=value_a,key_b=value_b`.
  * `UPDATE_MASK`: comma-separated list of security mark fields to update for the asset; for example, `marks.key_a,marks.key_b`.



### Java
    
    
    import autovalue.shaded.com.google.common.collect.ImmutableMap;
    import com.google.cloud.securitycenter.v2.[FindingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.FindingName.html);
    import com.google.cloud.securitycenter.v2.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html);
    import com.google.cloud.securitycenter.v2.[SecurityMarks](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityMarks.html);
    import com.google.cloud.securitycenter.v2.[UpdateSecurityMarksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateSecurityMarksRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    
    public class AddMarkToFinding {
    
      public static void main(String[] args) throws IOException {
        // TODO: Replace the sample resource name
        // organizationId: Google Cloud Organization id.
        String organizationId = "{google-cloud-organization-id}";
    
        // Specify the source-id.
        String sourceId = "{source-id}";
    
        // Specify the finding-id.
        String findingId = "{finding-id}";
    
        // Specify the location.
        String location = "global";
    
        addMarksToFinding(organizationId, sourceId, location, findingId);
      }
    
      // Demonstrates adding security marks to findings.
      // To add or change security marks, you must have an IAM role that includes permission:
      // Finding marks: Finding Security Marks Writer, securitycenter.findingSecurityMarksWriter
      public static [SecurityMarks](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityMarks.html) addMarksToFinding(String organizationId, String sourceId,
          String location, String findingId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html).create();
    
        // Start setting up a request to add security marks for a finding.
        ImmutableMap markMap = ImmutableMap.of("key_a", "value_a", "key_b", "value_b");
    
        // Instead of using the FindingName, a plain String can also be used. E.g.:
        // String findingName = String.format("organizations/%s/sources/%s/locations/%s/findings/%s",
        // organizationId, sourceId, location, findingId);
        [FindingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.FindingName.html) findingName = [FindingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.FindingName.html)
            .[ofOrganizationSourceLocationFindingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.FindingName.html#com_google_cloud_securitycenter_v2_FindingName_ofOrganizationSourceLocationFindingName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(organizationId, sourceId, location, findingId);
    
        // Add security marks and field mask for security marks.
        [SecurityMarks](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityMarks.html) securityMarks = [SecurityMarks](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityMarks.html).newBuilder()
            .setName(findingName + "/securityMarks")
            .[putAllMarks](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityMarks.Builder.html#com_google_cloud_securitycenter_v2_SecurityMarks_Builder_putAllMarks_java_util_Map_java_lang_String_java_lang_String__)(markMap)
            .build();
    
        // Set the update mask to specify which properties should be updated.
        // If empty, all mutable fields will be updated.
        // For more info on constructing field mask path, see the proto or:
        // https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask
        [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) updateMask = [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder()
            .[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("marks.key_a")
            .[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("marks.key_b")
            .build();
    
        [UpdateSecurityMarksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateSecurityMarksRequest.html) request = [UpdateSecurityMarksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateSecurityMarksRequest.html).newBuilder()
            .setSecurityMarks(securityMarks)
            .setUpdateMask(updateMask)
            .build();
    
        // Call the API.
        [SecurityMarks](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityMarks.html) response = client.[updateSecurityMarks](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html#com_google_cloud_securitycenter_v2_SecurityCenterClient_updateSecurityMarks_com_google_cloud_securitycenter_v2_SecurityMarks_com_google_protobuf_FieldMask_)(request);
    
        System.out.println("Security Marks:" + response);
        return response;
      }
    }

### Node.js
    
    
    // Imports the Google Cloud client library.
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)').v2;
    
    // Creates a new client.
    const client = new [SecurityCenterClient](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)();
    
    // Build the full resource path for the finding to update.
    /*
     * TODO(developer): Update the following references for your own environment before running the sample.
     */
    // const organizationId = 'YOUR_ORGANIZATION_ID';
    // const sourceId = 'SOURCE_ID';
    const findingName = `organizations/${organizationId}/sources/${sourceId}/locations/${location}/findings/${findingId}`;
    
    // Construct the request to be sent by the client.
    const updateSecurityMarksRequest = {
      securityMarks: {
        name: `${findingName}/securityMarks`,
        marks: {key_a: 'value_a', key_b: 'value_b'},
      },
      // Only update the marks with these keys.
      updateMask: {paths: ['marks.key_a', 'marks.key_b']},
    };
    
    async function addFindingSecurityMarks() {
      const [newMarks] = await client.updateSecurityMarks(
        updateSecurityMarksRequest
      );
    
      console.log('New marks: %j', newMarks);
    }
    addFindingSecurityMarks();

### Python
    
    
    def add_to_finding(organization_id, source_name, location_id, finding_name):
        """
        Adds security marks to a finding.
        Args:
           organization_id: organization_id is the numeric ID of the organization. e.g.:organization_id = "111122222444"
           source_name: is the resource path for a source that has been created
           location_id: Gcp location id; example: 'global'
           finding_name: finding name to add security marks.
    
        Returns:
            Dict: returns the deleted security marks response.
        """
        from google.cloud import securitycenter_v2
        from google.protobuf import field_mask_pb2
    
        client = securitycenter_v2.SecurityCenterClient()
        finding_name = f"organizations/{organization_id}/sources/{source_name}/locations/{location_id}/findings/{finding_name}"
        finding_marks_name = f"{finding_name}/securityMarks"
    
        # Notice the suffix after "marks." in the field mask matches the keys
        # in marks.
        field_mask = field_mask_pb2.FieldMask(
            paths=["marks.finding_key_a", "marks.finding_key_b"]
        )
        marks = {"finding_key_a": "value_a", "finding_key_b": "value_b"}
    
        updated_marks = client.[update_security_marks](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_security_marks)(
            request={
                "security_marks": {"name": finding_marks_name, "marks": marks},
                "update_mask": field_mask,
            }
        )
        return updated_marks, marks
    
    

Security marks are processed during batch scans—which run twice daily for Security Command Center Premium and Enterprise and once every other day for Security Command Center Standard—and not in real time. There may be a delay of 12 to 24 hours before security marks are processed and enforcement policies that resolve or reopen findings are applied. 

**Note:** a mark added to a finding is only applied to that specific finding. The mark is not applied to subsequent findings of the same type.

## Listing assets with security mark filters

**Deprecated** : The ability to list assets by using the Security Command Center API or the `gcloud scc assets list` command is deprecated. Use Cloud Asset Inventory to list assets instead.

If you activated Security Command Center before June 20, 2023, you can still use these feature until they are removed on or after June 20, 2024.

To list assets with Cloud Asset Inventory, see [Listing assets](https://docs.cloud.google.com/asset-inventory/docs/listing-assets).

After security marks are set on an asset, they can be used in the filter argument to the `ListAssets` API call. For example, to query for all assets where `key_a = value_a`, use the following code:

### gcloud
    
    
      # ORGANIZATION=12344321
      FILTER="security_marks.marks.key_a = \"value_a\""
    
      gcloud scc assets list $ORGANIZATION \
          --filter="$FILTER"

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv1"
    	"cloud.google.com/go/securitycenter/apiv1/securitycenterpb"
    	"google.golang.org/api/iterator"
    )
    
    // listAssetsWithMarks prints assets that have a mark of key_a equal to value_a
    // to w for orgID.  orgID is the numeric Organization ID.
    func listAssetsWithMarks(w io.Writer, orgID string) error {
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
    		Filter: `security_marks.marks.key_a = "value_a"`,
    	}
    
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
    		fmt.Fprintf(w, "Asset Name: %s, ", asset.Name)
    		fmt.Fprintf(w, "Resource Name %s, ", properties.ResourceName)
    		fmt.Fprintf(w, "Resource Type %s\n", properties.ResourceType)
    	}
    	return nil
    }
    

### Java
    
    
    static ImmutableList<ListAssetsResult> listAssetsWithQueryMarks(
        OrganizationName organizationName) {
      try (SecurityCenterClient client = SecurityCenterClient.create()) {
        // Start setting up a request to list all assets filtered by a specific security mark.
        // Parent must be in one of the following formats:
        //    OrganizationName organizationName = OrganizationName.of("organization-id");
        //    ProjectName projectName = ProjectName.of("project-id");
        //    FolderName folderName = FolderName.of("folder-id");
        ListAssetsRequest request =
            ListAssetsRequest.newBuilder()
                .setParent(organizationName.toString())
                .setFilter("security_marks.marks.key_a = \"value_a\"")
                .build();
    
        // Call the API.
        ListAssetsPagedResponse response = client.listAssets(request);
    
        // This creates one list for all assets.  If your organization has a large number of assets
        // this can cause out of memory issues.  You can process them batches by returning
        // the Iterable returned response.iterateAll() directly.
        ImmutableList<ListAssetsResult> results = ImmutableList.copyOf(response.iterateAll());
        System.out.println("Assets with security mark - key_a=value_a:");
        System.out.println(results);
        return results;
      } catch (IOException e) {
        throw new RuntimeException("Couldn't create client.", e);
      }
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
    async function listAssetsWithSecurityMarks() {
      const [response] = await client.listAssets({
        parent: parent,
        filter: 'security_marks.marks.key_a="value_a"',
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
    
    listAssetsWithSecurityMarks();

### Python
    
    
    from google.cloud import securitycenter
    
    client = securitycenter.SecurityCenterClient()
    
    # 'parent' must be in one of the following formats:
    #   "organizations/{organization_id}"
    #   "projects/{project_id}"
    #   "folders/{folder_id}"
    parent = f"organizations/{organization_id}"
    
    marks_filter = 'security_marks.marks.key_a = "value_a"'
    # Call the API and print results.
    asset_iterator = client.[list_assets](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_assets)(
        request={"parent": parent, "filter": marks_filter}
    )
    for i, asset_result in enumerate(asset_iterator):
        print(i, asset_result)

## Listing findings with security mark filters

After security marks are set on a finding, they can be used in the filter argument to the `ListFindings` API call. For example, to query all assets where `key_a != value_a`, use the following code:

### gcloud
    
    
    gcloud scc findings list PARENT/PARENT_ID \
        --location=LOCATION \
        --source=SOURCE_ID \
        --filter=FILTER

  * `PARENT`: the level of the resource hierarchy where the finding is located; use `organizations`, `folders`, or `projects`.
  * `PARENT_ID`: the numeric ID of the parent organization, folder, or project, or the alphanumeric ID of the parent project.
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to list findings; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`.
  * `SOURCE_ID`: the source ID.
  * `FILTER`: the filter to apply to the findings; for example, to exclude findings with the security mark `key_a=value_a`, use `"NOT security_marks.marks.key_a=\"value_a\""`



### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv2"
    	"cloud.google.com/go/securitycenter/apiv2/securitycenterpb"
    	"google.golang.org/api/iterator"
    )
    
    // listFindingsWithMarks prints findings that don't have a security mark
    // key_a equal to value_a to w.  sourceName is the full resource name
    // of the source to search for findings under.
    func listFindingsWithMarks(w io.Writer, sourceName string) error {
    	// sourceName := "{parent}/sources/{sourceId}"
    	// where,
    	// Parent must be in one of the following formats:
    	//		"organizations/{orgId}"
    	//		"projects/{projectId}"
    	//		"folders/{folderId}"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_Close)() // Closing the client safely cleans up background resources.
    
    	req := &securitycenterpb.ListFindingsRequest{
    		Parent: sourceName,
    		Filter: `NOT security_marks.marks.key_a="value_a"`,
    	}
    	it := client.ListFindings(ctx, req)
    	for {
    		result, err := it.Next()
    		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_BulkMuteFindingsOperation_Done) {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("it.Next: %w", err)
    		}
    		finding := result.Finding
    		fmt.Fprintf(w, "Finding Name: %s, ", finding.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_BulkMuteFindingsOperation_Name))
    		fmt.Fprintf(w, "Resource Name %s, ", finding.ResourceName)
    		fmt.Fprintf(w, "Category: %s\n", finding.Category)
    	}
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.securitycenter.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html);
    import com.google.cloud.securitycenter.v2.[ListFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListFindingsRequest.html);
    import com.google.cloud.securitycenter.v2.[ListFindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListFindingsResponse.html).[ListFindingsResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListFindingsResponse.ListFindingsResult.html);
    import com.google.cloud.securitycenter.v2.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    public class ListFindingMarksWithFilter {
    
      public static void main(String[] args) throws IOException {
        // TODO: Replace the sample resource name
        // organizationId: Google Cloud Organization id.
        String organizationId = "{google-cloud-organization-id}";
    
        // Specify the source-id.
        String sourceId = "{source-id}";
    
        // Specify the location.
        String location = "global";
    
        listFindingsWithQueryMarks(organizationId, sourceId, location);
      }
    
      // Demonstrates how to filter and list findings by security mark.
      public static List<Finding> listFindingsWithQueryMarks(String organizationId,
          String sourceId, String location) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html).create();
    
        // Start setting up a request to list all findings filtered by a specific security mark.
        // Use any one of the following formats:
        //  * organizations/{organization_id}/sources/{source_id}/locations/{location}
        //  * folders/{folder_id}/sources/{source_id}/locations/{location}
        //  * projects/{project_id}/sources/{source_id}/locations/{location}
        String parent = String.format("organizations/%s/sources/%s/locations/%s",
            organizationId, sourceId, location);
    
        // Lists findings where the 'security_marks.marks.key_a' field does not equal 'value_a'.
        String filter = "NOT security_marks.marks.key_a=\"value_a\"";
    
        [ListFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListFindingsRequest.html) request = [ListFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListFindingsRequest.html).newBuilder()
            .setParent(parent)
            .setFilter(filter)
            .build();
    
        // Call the API.
        List<Finding> listFindings = new ArrayList<>();
        Iterable<ListFindingsResult> resultList = client.[listFindings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html#com_google_cloud_securitycenter_v2_SecurityCenterClient_listFindings__org_jspecify_annotations_Nullable_com_google_cloud_securitycenter_v2_SourceName_)(request).iterateAll();
        resultList.forEach(result -> listFindings.add(result.getFinding()));
    
        for ([Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html) finding : listFindings) {
          System.out.println("List findings: " + finding);
        }
        return listFindings;
      }
    }

### Node.js
    
    
    // Imports the Google Cloud client library.
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)').v2;
    
    // Creates a new client.
    const client = new [SecurityCenterClient](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)();
    //  Build the full resource path for the source to search for findings.
    
    // The source path supports mutliple formats:
    // - `${parent}/sources/${sourceId}` without a location
    // - `${parent}/sources/${sourceId}/locations/${location}` with a location
    // where parent must be in one of the following formats:
    // - `organizations/${organization_id}`
    // - `folders/${folder_id}`
    // - `projects/${project_id}`
    
    /*
     * TODO(developer): Update the following references for your own environment before running the sample.
     */
    // const organizationId = 'YOUR_ORGANIZATION_ID';
    // const sourceId = 'SOURCE_ID';
    
    const sourceName = `organizations/${organizationId}/sources/${sourceId}`;
    
    // Construct the request to be sent by the client.
    const listFindingsRequest = {
      // List findings across all sources.
      parent: sourceName,
      filter: 'NOT security_marks.marks.key_a="value_a"',
    };
    
    async function listFindingsWithSecurityMarks() {
      const [response] = await client.listFindings(listFindingsRequest);
      let count = 0;
      Array.from(response).forEach(result =>
        console.log(
          `${++count} ${result.finding.name} ${result.finding.resourceName}`
        )
      );
    }
    listFindingsWithSecurityMarks();

### Python
    
    
    def list_findings_with_security_marks(organization_id, source_name, location_id) -> int:
        """
        lists all filtered findings with security marks across an organization.
        Args:
            organization_id: organization_id is the numeric ID of the organization. e.g.:organization_id = "111122222444"
            source_name: is the resource path for a source that has been created
            location_id: GCP location id; example: 'global'
        Returns:
             int: returns the count of filtered findings with security marks across the organization.
        """
        count = 0
        from google.cloud import securitycenter_v2
    
        # Create a new client.
        client = securitycenter_v2.SecurityCenterClient()
        parent = f"organizations/{organization_id}"
        all_sources = f"{parent}/sources/{source_name}/locations/{location_id}"
        # below filter is used to list active and unmuted findings without security marks acknowledgement as true.
        finding_result_iterator = client.[list_findings](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_findings)(
            request={
                "parent": all_sources,
                "filter": 'NOT security_marks.marks.ACK="true" AND NOT mute="MUTED" AND state="ACTIVE"',
            }
        )
        # Iterate an print all finding names and the resource they are
        # in reference to.
        for count, finding_result in enumerate(finding_result_iterator):
            print(
                "{}: name: {} resource: {}".format(
                    count, finding_result.finding.name, finding_result.finding.resource_name
                )
            )
        return count
    
    

## What's next

  * Learn more about [listing findings](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings) and [listing assets](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-assets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

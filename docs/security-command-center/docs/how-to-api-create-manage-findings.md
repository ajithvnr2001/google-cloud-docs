---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-api-create-manage-findings/
title: Managing findings using the Security Command Center API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:10.196785+00:00
---

# Managing findings using the Security Command Center API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-api-create-manage-findings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Managing findings using the Security Command Center API Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This guide walks you through creating and updating findings using the Security Command Center API.

## Before you begin

Before you create and update findings, you need to complete the following:

  * [Authenticate with the Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/reference/authentication)
  * [Have a source for the finding](https://docs.cloud.google.com/security-command-center/docs/how-to-api-create-manage-security-sources)



To complete this guide, you must have the Identity and Access Management (IAM) **Security Center Findings Editor** (`securitycenter.findingsEditor`) role at the **organization** level. For more information on Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control).

If you want to create findings with security marks, you must also have an IAM role that includes permissions for the kind of mark that you want to use:

  * **Asset Security Marks Writer** (`securitycenter.assetSecurityMarksWriter`)
  * **Finding Security Marks Writer** (`securitycenter.findingSecurityMarksWriter`)



For more information about marks, see [Annotate findings with security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-findings).

## Creating a finding

Create an active finding for a source.

### gcloud
    
    
    gcloud scc findings create FINDING_NAME \
        --organization=PARENT_ID \
        --location=LOCATION \
        --source=SOURCE_ID \
        --state=STATE \
        --category=CATEGORY \
        --event-time=EVENT_TIME \
        --resource-name=RESOURCE_NAME

Replace the following:

  * `FINDING_NAME`: the name of the finding.
  * `PARENT_ID`: the numeric ID of the parent organization.
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to create a finding; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`.
  * `SOURCE_ID`: the numeric ID of the source for the finding.
  * `STATE`: the state of the finding; use `ACTIVE` if the finding needs attention or `INACTIVE` if the finding has been addressed.
  * `CATEGORY`: the taxonomy group that the finding belongs to; for example, `AUDIT_LOGGING_DISABLED`.
  * `EVENT_TIME`: the time when the event occurred, formatted as an [RFC 822 timestamp](https://datatracker.ietf.org/doc/html/rfc822#section-5.1) or another [timestamp format that the gcloud CLI supports](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes).
  * `RESOURCE_NAME`: the full resource name of the resource that the finding applies to.



### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv2"
    	"cloud.google.com/go/securitycenter/apiv2/securitycenterpb"
    	"github.com/golang/protobuf/ptypes"
    )
    
    // createFinding demonstrates how to create a new security finding in CSCC.
    // sourceName is the full resource name of the source the finding should
    // be associated with.
    func createFinding(w io.Writer, sourceName string) error {
    	// sourceName := "organizations/111122222444/sources/1234/locations/global"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_Close)() // Closing the client safely cleans up background resources.
    	// Use now as the eventTime for the security finding.
    	eventTime, err := ptypes.TimestampProto(time.Now())
    	if err != nil {
    		return fmt.Errorf("TimestampProto: %w", err)
    	}
    
    	req := &securitycenterpb.CreateFindingRequest{
    		Parent:    sourceName,
    		FindingId: "samplefindingid",
    		Finding: &securitycenterpb.Finding{
    			State: securitycenterpb.[Finding_ACTIVE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2/securitycenterpb.html#cloud_google_com_go_securitycenter_apiv2_securitycenterpb_Finding_STATE_UNSPECIFIED_Finding_ACTIVE_Finding_INACTIVE),
    			// Resource the finding is associated with. This is an
    			// example any resource identifier can be used.
    			ResourceName: "//cloudresourcemanager.googleapis.com/organizations/11232/sources/-/locations/global",
    			// A free-form category.
    			Category: "MEDIUM_RISK_ONE",
    			// The time associated with discovering the issue.
    			EventTime: eventTime,
    		},
    	}
    	finding, err := client.CreateFinding(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateFinding: %w", err)
    	}
    	fmt.Fprintf(w, "New finding created: %s\n", finding.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_BulkMuteFindingsOperation_Name))
    	fmt.Fprintf(w, "Event time (Epoch Seconds): %d\n", eventTime.Seconds)
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.securitycenter.v2.[CreateFindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.CreateFindingRequest.html);
    import com.google.cloud.securitycenter.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html);
    import com.google.cloud.securitycenter.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html).[FindingClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.FindingClass.html);
    import com.google.cloud.securitycenter.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html).[Mute](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.Mute.html);
    import com.google.cloud.securitycenter.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html).Severity;
    import com.google.cloud.securitycenter.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html).State;
    import com.google.cloud.securitycenter.v2.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html);
    import com.google.cloud.securitycenter.v2.[SourceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SourceName.html);
    import com.google.protobuf.[Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html);
    import java.io.IOException;
    import java.time.Instant;
    import java.util.Optional;
    import java.util.UUID;
    
    public class CreateFindings {
    
      public static void main(String[] args) throws IOException {
        // TODO: Replace the sample resource name
        // organizationId: Google Cloud Organization id.
        String organizationId = "{google-cloud-organization-id}";
    
        // Specify the location to list the findings.
        String location = "global";
    
        // The source id corresponding to the finding.
        String sourceId = "{source-id}";
    
        // The finding id.
        String findingId = "testfindingv2" + UUID.randomUUID().toString().split("-")[0];
    
        // Specify the category.
        Optional<String> category = Optional.of("MEDIUM_RISK_ONE");
    
        createFinding(organizationId, location, findingId, sourceId, category);
      }
    
      /**
       * Creates a security finding within a specific source in the Security Command Center.
       */
      public static [Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html) createFinding(String organizationId, String location, String findingId,
          String sourceId, Optional<String> category) throws IOException {
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html).create()) {
          // Optionally SourceName or String can be used.
          // String sourceName = String.format("organizations/%s/sources/%s", organizationId, sourceId);
          [SourceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SourceName.html) sourceName = [SourceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SourceName.html).of(organizationId, sourceId);
    
          Instant eventTime = Instant.now();
          // The resource this finding applies to. The Cloud Security Command Center UI can link the
          // findings for a resource to the corresponding asset of a resource if there are matches.
          String resourceName = String.format("//cloudresourcemanager.googleapis.com/organizations/%s",
              organizationId);
    
          // Set up a request to create a finding in a source.
          String parent = String.format("%s/locations/%s", sourceName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SourceName.html#com_google_cloud_securitycenter_v2_SourceName_toString__)(), location);
          [Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html) finding = [Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html).newBuilder()
              .setParent(parent)
              .setState(State.ACTIVE)
              .setSeverity(Severity.LOW)
              .setMute([Mute](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.Mute.html).UNMUTED)
              .[setFindingClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.Builder.html#com_google_cloud_securitycenter_v2_Finding_Builder_setFindingClass_com_google_cloud_securitycenter_v2_Finding_FindingClass_)([FindingClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.FindingClass.html).OBSERVATION)
              .[setResourceName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.Builder.html#com_google_cloud_securitycenter_v2_Finding_Builder_setResourceName_java_lang_String_)(resourceName)
              .setEventTime([Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html).newBuilder()
                  .setSeconds(eventTime.getEpochSecond())
                  .setNanos(eventTime.getNano()))
              .[setCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.Builder.html#com_google_cloud_securitycenter_v2_Finding_Builder_setCategory_java_lang_String_)(category.orElse("LOW_RISK_ONE"))
              .build();
    
          [CreateFindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.CreateFindingRequest.html) createFindingRequest = [CreateFindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.CreateFindingRequest.html).newBuilder()
              .setParent(parent)
              .[setFindingId](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.CreateFindingRequest.Builder.html#com_google_cloud_securitycenter_v2_CreateFindingRequest_Builder_setFindingId_java_lang_String_)(findingId)
              .setFinding(finding).build();
    
          // Call the API.
          [Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html) response = client.createFinding(createFindingRequest);
          return response;
        }
      }
    }

### Node.js
    
    
    // Imports the Google Cloud client library.
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)').v2;
    const uuid = require('uuid');
    
    // Create a Security Center client
    const client = new [SecurityCenterClient](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)();
    
    // TODO(developer): Update the following for your own environment.
    const organizationId = '1081635000895';
    const location = 'global';
    
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
    
    // The resource this finding applies to. The Cloud Security Command Center UI can link the
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
    
    // Call the API.
    const [finding] = await client.createFinding(createFindingRequest);
    console.log('New finding created: %j', finding);

### Python
    
    
    def create_finding(
        organization_id, location_id, finding_id, source_name, category
    ) -> Dict:
        """
        cretaes a new finding
        Args:
            organization_id: organization_id is the numeric ID of the organization. e.g.:organization_id = "111122222444"
            source_name: is the resource path for a source that has been created
            finding_id: unique identifier provided by the client.
            location_id: GCP location id; example: 'global'
            category: the additional category group with in findings.
        Returns:
             Dict: returns the created findings details.
        """
        import datetime
    
        from google.cloud import securitycenter_v2
        from google.cloud.securitycenter_v2 import Finding
    
        # Create a new client.
        client = securitycenter_v2.SecurityCenterClient()
    
        # Use the current time as the finding "event time".
        event_time = datetime.datetime.now(tz=datetime.timezone.utc)
    
        # 'source_name' is the resource path for a source that has been
        # created previously (you can use list_sources to find a specific one).
        # Its format is:
        # source_name = "organizations/{organization_id}/sources/{source_id}"
        # e.g.:
        # source_name = "organizations/111122222444/sources/1234"
        # source_name = f"organizations/{organization_id}/sources/{source_name}"
        # category= "MEDIUM_RISK_ONE"
        # The resource this finding applies to.  The CSCC UI can link
        # the findings for a resource to the corresponding Asset of a resource
        # if there are matches.
        resource_name = (
            f"//cloudresourcemanager.googleapis.com/organizations/{organization_id}"
        )
    
        finding = Finding(
            state=Finding.State.ACTIVE,
            resource_name=resource_name,
            category=category,
            event_time=event_time,
        )
        parent = source_name + "/locations/" + location_id
        # Call The API.
        created_finding = client.[create_finding](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_create_finding)(
            request={"parent": parent, "finding_id": finding_id, "finding": finding}
        )
        print(created_finding)
        return created_finding
    
    

For information on how long findings data is stored in Security Command Center, read [Findings retention](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings#findings-retention).

## Updating a finding's state

Security Command Center also provides an API to only update a finding's state. The following example shows how to change a finding's state to inactive.

### gcloud
    
    
    gcloud scc findings update \
        PARENT/PARENT_ID/sources/SOURCE_ID/locations/LOCATION/findings/FINDING_NAME \
        --state=STATE

Replace the following:

  * `PARENT`: the level of the resource hierarchy where the finding is located; use `organizations`, `folders`, or `projects`.
  * `PARENT_ID`: the numeric ID of the parent organization, folder, or project, or the alphanumeric ID of the parent project.
  * `SOURCE_ID`: the numeric ID of the source for the finding.
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to update a finding; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`.
  * `FINDING_NAME`: the finding to update.
  * `STATE`: the state of the finding; use `ACTIVE` if the finding needs attention or `INACTIVE` if the finding has been addressed.



### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv2"
    	"cloud.google.com/go/securitycenter/apiv2/securitycenterpb"
    )
    
    // updateFindingState demonstrates how to update a security finding's state
    // in CSCC.  findingName is the full resource name of the finding to update.
    func setFindingState(w io.Writer, findingName string) error {
    	// findingName := "organizations/111122222444/sources/1234/locations/global"
    	// Instantiate a context and a security service client to make API calls.
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_Close)() // Closing the client safely cleans up background resources.
    
    	req := &securitycenterpb.SetFindingStateRequest{
    		Name:  findingName,
    		State: securitycenterpb.[Finding_INACTIVE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2/securitycenterpb.html#cloud_google_com_go_securitycenter_apiv2_securitycenterpb_Finding_STATE_UNSPECIFIED_Finding_ACTIVE_Finding_INACTIVE),
    		// New state is effective immediately.
    	}
    
    	finding, err := client.SetFindingState(ctx, req)
    	if err != nil {
    		return fmt.Errorf("SetFindingState: %w", err)
    	}
    
    	fmt.Fprintf(w, "Finding updated: %s\n", finding.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_BulkMuteFindingsOperation_Name))
    	fmt.Fprintf(w, "Finding state: %v\n", finding.State)
    	fmt.Fprintf(w, "Event time (Epoch Seconds): %d\n", finding.EventTime.Seconds)
    
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.securitycenter.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html);
    import com.google.cloud.securitycenter.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html).State;
    import com.google.cloud.securitycenter.v2.[FindingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.FindingName.html);
    import com.google.cloud.securitycenter.v2.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html);
    import com.google.cloud.securitycenter.v2.[SetFindingStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SetFindingStateRequest.html);
    import java.io.IOException;
    
    public class SetFindingsByState {
    
      public static void main(String[] args) throws IOException {
        // organizationId: Google Cloud Organization id.
        String organizationId = "{google-cloud-organization-id}";
    
        // Specify the location to list the findings.
        String location = "global";
    
        // The source id corresponding to the finding.
        String sourceId = "{source-id}";
    
        // The finding id.
        String findingId = "{finding-id}";
    
        setFindingState(organizationId, location, sourceId, findingId);
      }
    
      // Demonstrates how to update a finding's state
      public static [Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html) setFindingState(String organizationId, String location, String sourceId,
          String findingId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html).create()) {
          // Optionally FindingName or String can be used.
          // String findingName = String.format("organizations/%s/sources/%s/locations/%s/findings/%s",
          // organizationId,sourceId,location,findingId);
          [FindingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.FindingName.html) findingName = [FindingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.FindingName.html)
              .[ofOrganizationSourceLocationFindingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.FindingName.html#com_google_cloud_securitycenter_v2_FindingName_ofOrganizationSourceLocationFindingName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(organizationId, sourceId, location, findingId);
    
          [SetFindingStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SetFindingStateRequest.html) request = [SetFindingStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SetFindingStateRequest.html).newBuilder()
              .setName(findingName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.FindingName.html#com_google_cloud_securitycenter_v2_FindingName_toString__)())
              .setState(State.INACTIVE)
              .build();
    
          // Call the API.
          [Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html) finding = client.setFindingState(request);
    
          System.out.println("Updated Finding: " + finding);
          return finding;
        }
      }
    }

### Node.js
    
    
    // Imports the Google Cloud client library.
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)').v2;
    
    // Creates a new client.
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
      return {sourceId, findingId};
    }
    
    const {sourceId, findingId} = await createSampleFinding();
    
    // The name is the full resource name of the source the finding should be associated with.
    const name = `organizations/${organizationId}/sources/${sourceId}/locations/${location}/findings/${findingId}`;
    
    // Build the request.
    const eventTime = new Date();
    
    const findingRequest = {
      name,
      state: 'INACTIVE',
      // use now as the time when the new state takes effect.
      startTime: {
        seconds: Math.floor(eventTime.getTime() / 1000),
        nanos: (eventTime.getTime() % 1000) * 1e6,
      },
    };
    
    async function setFindingState() {
      // Call the API.
      const [response] = await client.setFindingState(findingRequest);
      console.log('Set finding state: %j', response);
    }
    
    await setFindingState();

## What's next

Learn more about [accessing Security Command Center using client libraries](https://docs.cloud.google.com/security-command-center/docs/reference/libraries).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

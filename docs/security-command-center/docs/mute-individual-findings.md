---
url: https://docs.cloud.google.com/security-command-center/docs/mute-individual-findings/
title: Mute individual findings \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:49.864525+00:00
---

# Mute individual findings  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/mute-individual-findings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Mute individual findings Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document explains how to statically mute individual findings, unmute them, or mute findings in bulk in Security Command Center.

## Required roles

To get the permissions that you need to mute or unmute findings, ask your administrator to grant you the following IAM roles on the organization, folder, or project: 

  * Manually mute or unmute individual findings: 
    * [Security Center Findings Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsEditor) (`roles/securitycenter.findingsEditor`)
    * [Security Center Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)
  * Mute findings in bulk: 
    * [Security Center Findings Bulk Mute Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsBulkMuteEditor) (`roles/securitycenter.findingsBulkMuteEditor`)
    * [Security Center Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Mute an individual finding

You can _statically_ mute an individual finding by using the Google Cloud console, the gcloud CLI, or the Security Command Center API.

Statically muting a finding doesn't affect whether it is active or not. If an active finding is muted, the `state` attribute remains unchanged: `state="ACTIVE"`. The finding is hidden, but remains active until the underlying vulnerability, misconfiguration, or threat is resolved. In addition, by statically muting a finding, you are overriding any dynamic mute rules that apply to the finding.

Muting a toxic combination finding closes the corresponding toxic combination case.

To mute all future findings that match criteria that you specify, see [Manage mute rules](https://docs.cloud.google.com/security-command-center/docs/manage-mute-rules).

For sample code to mute a finding, see [Mute a finding](https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-set-mute).

To statically mute an individual finding, click the tab for the procedure that you want to use:

### Console

  1. In the Google Cloud console, go to the Security Command Center **Findings** page. 

[ Go to Findings](https://console.cloud.google.com/security/command-center/findings)

  2. If necessary, select your Google Cloud project or organization.
  3. If you don't see the finding that you need to mute in the **Findings query results** panel, select the category of the finding in the **Category** section of the **Quick filters** panel.
  4. Select the finding that you need to mute. You can select one or more findings.
  5. On the **Findings query results** action bar, click **Mute options** , and then select **Apply mute override**.

The `mute` attribute for the selected findings is set to `MUTED`, and the finding is removed from the **Findings query results** panel. Alternatively, you can mute a finding from its details panel:

  6. In the **Finding query results** panel of the **Findings** page, in the **Category** column, click the name of an individual finding. The details panel of the finding opens.

  7. Click **Take action**.

  8. From the **Take action** menu, select **Apply mute override**.

If you select **Mute findings like this** instead, the **Create mute rule** page opens where you can create a mute rule for findings of the same type or that include the same [`Indicator`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v1/organizations.sources.findings#indicator) attribute.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To set a finding's mute state to `MUTED`, use the [`set-mute`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/set-mute) command in the gcloud CLI:
         
         gcloud scc findings set-mute FINDING_ID \
           --PARENT=PARENT_ID \
           --location=LOCATION \
           --source=SOURCE_ID \
           --mute=MUTED

Replace the following:

     * `FINDING_ID`: the ID for the finding you want to mute

To retrieve finding IDs, use the Security Command Center API to [list findings](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings). The finding ID is the last part of the `canonicalName` attribute, for example, `projects/123456789012/sources/1234567890123456789/findings`/5ee30aa342e799e4e1700826de053aa9`.

     * `PARENT`: the parent resource (`project`, `folder`, or `organization`), case-sensitive

     * `PARENT_ID`: the ID of the parent organization, folder, or project

     * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to mute or unmute findings; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`

     * `SOURCE_ID`: the source ID

For instructions on retrieving a source ID, see [Getting the source ID](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications#get-source-id).




### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv2"
    	"cloud.google.com/go/securitycenter/apiv2/securitycenterpb"
    )
    
    // setMute mutes an individual finding.
    // If a finding is already muted, muting it again has no effect.
    // Various mute states are: MUTE_UNSPECIFIED/MUTE/UNMUTE.
    func setMute(w io.Writer, findingPath string) error {
    	// findingPath: The relative resource name of the finding. See:
    	// https://cloud.google.com/apis/design/resource_names#relative_resource_name
    	// Use any one of the following formats:
    	//  - organizations/{organization_id}/sources/{source_id}/finding/{finding_id}
    	//  - folders/{folder_id}/sources/{source_id}/finding/{finding_id}
    	//  - projects/{project_id}/sources/{source_id}/finding/{finding_id}
    	// findingPath := fmt.Sprintf("projects/%s/sources/%s/finding/%s", "your-google-cloud-project-id", "source", "finding-id")
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_Close)()
    
    	req := &securitycenterpb.SetMuteRequest{
    		Name: findingPath,
    		Mute: securitycenterpb.[Finding_MUTED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2/securitycenterpb.html#cloud_google_com_go_securitycenter_apiv2_securitycenterpb_Finding_MUTE_UNSPECIFIED_Finding_MUTED_Finding_UNMUTED_Finding_UNDEFINED)}
    
    	finding, err := client.SetMute(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to set the specified mute value: %w", err)
    	}
    	fmt.Fprintf(w, "Mute value for the finding: %s is %s", finding.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_BulkMuteFindingsOperation_Name), finding.Mute)
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.securitycenter.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html);
    import com.google.cloud.securitycenter.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html).[Mute](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.Mute.html);
    import com.google.cloud.securitycenter.v2.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html);
    import com.google.cloud.securitycenter.v2.[SetMuteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SetMuteRequest.html);
    import java.io.IOException;
    
    public class SetMuteFinding {
    
      public static void main(String[] args) throws IOException {
        // TODO: Replace the variables within {}
        // findingPath: The relative resource name of the finding. See:
        // https://cloud.google.com/apis/design/resource_names#relative_resource_name
        // Use any one of the following formats:
        //  - organizations/{org_id}/sources/{source_id}/locations/{location}/finding/{finding_id}
        //  - folders/{folder_id}/sources/{source_id}/locations/{location}/finding/{finding_id}
        //  - projects/{project_id}/sources/{source_id}/locations/{location}/finding/{finding_id}
        //
        String findingPath = "{path-to-the-finding}";
    
        setMute(findingPath);
      }
    
      // Mute an individual finding.
      // If a finding is already muted, muting it again has no effect.
      // Various mute states are: MUTE_UNSPECIFIED/MUTE/UNMUTE.
      public static [Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html) setMute(String findingPath) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html).create()) {
    
          [SetMuteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SetMuteRequest.html) setMuteRequest =
              [SetMuteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SetMuteRequest.html).newBuilder()
                  // Relative path for the finding.
                  .setName(findingPath)
                  .setMute([Mute](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.Mute.html).MUTED)
                  .build();
    
          [Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html) finding = client.setMute(setMuteRequest);
          System.out.println(
              "Mute value for the finding " + finding.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html#com_google_cloud_securitycenter_v2_Finding_getName__)() + " is: " + finding.[getMute](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html#com_google_cloud_securitycenter_v2_Finding_getMute__)());
          return finding;
        }
      }
    }

### Python
    
    
    def set_mute_finding(finding_path: str) -> None:
        """
          Mute an individual finding.
          If a finding is already muted, muting it again has no effect.
          Various mute states are: MUTE_UNSPECIFIED/MUTE/UNMUTE.
        Args:
            finding_path: The relative resource name of the finding. See:
            https://cloud.google.com/apis/design/resource_names#relative_resource_name
            Use any one of the following formats:
            - organizations/{organization_id}/sources/{source_id}/finding/{finding_id},
            - folders/{folder_id}/sources/{source_id}/finding/{finding_id},
            - projects/{project_id}/sources/{source_id}/finding/{finding_id}.
        """
        from google.cloud import securitycenter_v2
    
        client = securitycenter_v2.SecurityCenterClient()
    
        request = securitycenter_v2.SetMuteRequest()
        request.name = finding_path
        request.mute = securitycenter_v2.Finding.Mute.MUTED
    
        finding = client.[set_mute](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_set_mute)(request)
        print(f"Mute value for the finding: {finding.mute.name}")
        return finding
    
    

### REST

In the Security Command Center API, use the [`findings.setMute`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings/setMute) method to mute a finding. The request body is an enum that indicates the resulting mute state:
    
    
    POST https://securitycenter.googleapis.com/v2/PARENT/PARENT_ID/sources/SOURCE_ID/locations/LOCATION/findings/FINDING_ID:setMute
    
    {
      "mute": "MUTED"
    }
    

Replace the following:

  * `PARENT`: the parent resource (`organizations`, `folders`, or `projects`).
  * `PARENT_ID`: the ID of the parent organization, folder, or project.
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to mute or unmute findings; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`
  * `SOURCE_ID`: the numeric ID for the source.

For instructions on retrieving a source ID, see [Getting the source ID](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications#get-source-id).

  * `FINDING_ID`: the ID for the finding you want to mute.

To retrieve finding IDs, use the Security Command Center API to [list findings](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings). The finding ID is the last part of the `canonicalName` attribute, for example, `projects/123456789012/sources/1234567890123456789/findings/5ee30aa342e799e4e1700826de053aa9`.




After you mute a finding, its `mute` attribute is set to `MUTED`.

### Unmute individual findings

You can _statically_ unmute an individual finding by using the Google Cloud console, the gcloud CLI, or the Security Command Center API.

Unmuting a finding is useful when you need to prevent a finding from being hidden by an overly broad mute rule, or by a rule that might be too complex to modify to exclude findings you deem important.

Unmuted findings are muted again only if the findings are manually muted. Mute rules created with the gcloud CLI or Security Command Center API won't affect findings unmuted by users.

For sample code to unmute a finding, see [Unmute a finding](https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-set-unmute).

### Console

To unmute an individual finding using Google Cloud console, click the tab for your service tier:

  1. In the Google Cloud console, go to the Security Command Center **Findings** page. 

[ Go to Findings](https://console.cloud.google.com/security/command-center/findings)

  2. If necessary, select your Google Cloud project or organization. The **Findings** page opens with the default query displayed in the **Query preview** section. The default query filters out muted findings, so you need to edit the query before muted findings appear in the **Findings query results** panel.
  3. To the right of the **Query preview** section, click **Edit query** to open the **Query editor**.
  4. In the **Query editor** field, replace the existing mute statement with the following: 
         
         mute="MUTED"

  5. Click **Apply**. The findings in the **Findings query results** panel update to include only muted findings.
  6. If necessary, filter out other muted findings. For example, in the **Quick filters** panel under **Category** , select the name of the finding that you need to unmute to filter out all other categories of finding.
  7. Select the finding that you want to unmute. You can select one or more findings.
  8. On the **Findings query results** action bar, click **Mute Options** , and then select **Apply unmute override**. The `mute` attribute for the selected findings is set to `UNMUTED`, and the finding is removed from the **Findings query results** panel. Alternatively, you can unmute a finding from its details panel:
  9. In the **Finding query results** panel of the **Findings** page, in the **Category** column, click the name of an individual finding. The details panel of the finding opens.
  10. Click **Take action**.
  11. From the **Take action** menu, select **Apply unmute override**.



### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To set a finding's mute state to `UNMUTED`, use the [`set-mute`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/set-mute) command in the gcloud CLI:
         
         gcloud scc findings set-mute FINDING_ID \
           --PARENT=PARENT_ID \
           --location=LOCATION \
           --source=SOURCE_ID \
           --mute=UNMUTED

Replace the following:

     * `FINDING_ID`: the ID for the finding you want to mute

To retrieve finding IDs, use the Security Command Center API to [list findings](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings). The finding ID is the last part of the `canonicalName` attribute, for example, `projects/123456789012/sources/1234567890123456789/findings/5ee30aa342e799e4e1700826de053aa9`.

     * `PARENT`: the parent resource (`project`, `folder`, or `organization` ), case-sensitive

     * `PARENT_ID`: the ID of the parent organization, folder, or project

     * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to mute or unmute findings; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`

     * `SOURCE_ID`: the source ID

For instructions on retrieving a source ID, see [Getting the source ID](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications#get-source-id).




### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv2"
    	"cloud.google.com/go/securitycenter/apiv2/securitycenterpb"
    )
    
    // setUnmute unmutes an individual finding.
    // Unmuting a finding that isn't muted has no effect.
    // Various mute states are: MUTE_UNSPECIFIED/MUTE/UNMUTE.
    func setUnmute(w io.Writer, findingPath string) error {
    	// findingPath: The relative resource name of the finding. See:
    	// https://cloud.google.com/apis/design/resource_names#relative_resource_name
    	// Use any one of the following formats:
    	//  - organizations/{organization_id}/sources/{source_id}/finding/{finding_id}
    	//  - folders/{folder_id}/sources/{source_id}/finding/{finding_id}
    	//  - projects/{project_id}/sources/{source_id}/finding/{finding_id}
    	// findingPath := fmt.Sprintf("projects/%s/sources/%s/finding/%s", "your-google-cloud-project-id", "source", "finding-id")
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_Close)()
    
    	req := &securitycenterpb.SetMuteRequest{
    		Name: findingPath,
    		Mute: securitycenterpb.[Finding_UNMUTED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2/securitycenterpb.html#cloud_google_com_go_securitycenter_apiv2_securitycenterpb_Finding_MUTE_UNSPECIFIED_Finding_MUTED_Finding_UNMUTED_Finding_UNDEFINED)}
    
    	finding, err := client.SetMute(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to set the specified mute value: %w", err)
    	}
    	fmt.Fprintf(w, "Mute value for the finding: %s is %s", finding.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_BulkMuteFindingsOperation_Name), finding.Mute)
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.securitycenter.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html);
    import com.google.cloud.securitycenter.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html).[Mute](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.Mute.html);
    import com.google.cloud.securitycenter.v2.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html);
    import com.google.cloud.securitycenter.v2.[SetMuteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SetMuteRequest.html);
    import java.io.IOException;
    
    public class SetUnmuteFinding {
    
      public static void main(String[] args) throws IOException {
        // TODO: Replace the variables within {}
        // findingPath: The relative resource name of the finding. See:
        // https://cloud.google.com/apis/design/resource_names#relative_resource_name
        // Use any one of the following formats:
        //  - organizations/{org_id}/sources/{source_id}/locations/{location}/finding/{finding_id}
        //  - folders/{folder_id}/sources/{source_id}/locations/{location}/finding/{finding_id}
        //  - projects/{project_id}/sources/{source_id}/locations/{location}/finding/{finding_id}
        //
        String findingPath = "{path-to-the-finding}";
    
        setUnmute(findingPath);
      }
    
      // Unmute an individual finding.
      // Unmuting a finding that isn't muted has no effect.
      // Various mute states are: MUTE_UNSPECIFIED/MUTE/UNMUTE.
      public static [Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html) setUnmute(String findingPath) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html).create()) {
    
          [SetMuteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SetMuteRequest.html) setMuteRequest =
              [SetMuteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SetMuteRequest.html).newBuilder()
                  .setName(findingPath)
                  .setMute([Mute](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.Mute.html).UNMUTED)
                  .build();
    
          [Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html) finding = client.setMute(setMuteRequest);
          System.out.println(
              "Mute value for the finding " + finding.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html#com_google_cloud_securitycenter_v2_Finding_getName__)() + " is: " + finding.[getMute](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html#com_google_cloud_securitycenter_v2_Finding_getMute__)());
          return finding;
        }
      }
    }

### Python
    
    
    def set_unmute_finding(finding_path: str) -> None:
        """
          Unmute an individual finding.
          Unmuting a finding that isn't muted has no effect.
          Various mute states are: MUTE_UNSPECIFIED/MUTE/UNMUTE.
        Args:
            finding_path: The relative resource name of the finding. See:
            https://cloud.google.com/apis/design/resource_names#relative_resource_name
            Use any one of the following formats:
            - organizations/{organization_id}/sources/{source_id}/finding/{finding_id},
            - folders/{folder_id}/sources/{source_id}/finding/{finding_id},
            - projects/{project_id}/sources/{source_id}/finding/{finding_id}.
        """
        from google.cloud import securitycenter_v2
    
        client = securitycenter_v2.SecurityCenterClient()
    
        request = securitycenter_v2.SetMuteRequest()
        request.name = finding_path
        request.mute = securitycenter_v2.Finding.Mute.UNMUTED
    
        finding = client.[set_mute](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_set_mute)(request)
        print(f"Mute value for the finding: {finding.mute.name}")
        return finding
    
    

### REST

In the Security Command Center API, use the [`findings.setMute`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings/setMute) method to unmute a finding. The request body is an enum that indicates the resulting mute state:
    
    
    POST https://securitycenter.googleapis.com/v2/PARENT/PARENT_ID/sources/SOURCE_ID/locations/LOCATION/findings/FINDING_ID:setMute
    
    {
      "mute": "UNMUTED"
    }
    

Replace the following:

  * `PARENT`: the parent resource (`organizations`, `folders`, or `projects`)
  * `PARENT_ID`: the ID of the parent organization, folder, or project
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to mute or unmute findings; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`
  * `SOURCE_ID`: the numeric ID for the source

For instructions on retrieving a source ID, see [Getting the source ID](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications#get-source-id).

  * `FINDING_ID`: the ID for the finding you want to mute.

To retrieve finding IDs, use the Security Command Center API to [list findings](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings). The finding ID is the last part of the `canonicalName` attribute, for example, `projects/123456789012/sources/1234567890123456789/findings/5ee30aa342e799e4e1700826de053aa9`.




Selected findings are no longer hidden, and the `mute` attribute for the findings is set to `UNMUTED`.

### Remove a mute state override from individual findings

You apply a _mute state override_ when you intentionally modify a finding's mute state to statically mute or unmute the finding. For example, you might want to apply a mute state override to hide a low-severity finding that is not worth creating a dynamic mute rule for.

You can remove a mute state override from an individual finding by using the Google Cloud console, the gcloud CLI, or the Security Command Center API.

Before removing the mute state override from a finding, understand the following:

  * A finding has a mute state override if it is statically muted or unmuted. You can apply a mute state override to any finding manually or automatically with static mute rules.
  * A mute state override applies to a finding indefinitely and takes priority over any matching mute rules.
  * Removing the mute state override from a finding resets the finding's mute state so that it can be processed by static or dynamic mute rules.
  * Removing the mute state override from a finding is different than unmuting a finding. When you unmute a finding (apply an unmute override), mute rules can't mute that finding until you've manually removed the mute state override.



To remove the mute override from an individual finding, do the following:

### Console

  1. In the Google Cloud console, go to the Security Command Center **Findings** page. 

[ Go to Findings](https://console.cloud.google.com/security/command-center/findings)

  2. Select your Google Cloud project or organization.
  3. To the right of the **Query preview** section, click **Edit query** to open the **Query editor**.
  4. In the **Query editor** field, replace the existing mute statement with the following: 
         
         mute="MUTED" OR mute="UNMUTED"

  5. Click **Apply**. The findings in the **Findings query results** panel update to include statically muted and unmuted findings.
  6. If necessary, filter out other findings. For example, in the **Quick filters** panel under **Category** , select the name of the finding that you need to reset to filter out all other categories of finding.
  7. Select the finding that you want to reset. You can select one or more findings.
  8. On the **Findings query results** action bar, click **Mute Options** , and then select **Remove mute overrides**. The `mute` attribute for the selected findings is set to `UNDEFINED`, and the finding is removed from the **Findings query results** panel. Alternatively, you can unmute a finding from its details panel:
  9. In the **Finding query results** panel of the **Findings** page, in the **Category** column, click the name of an individual finding. The details panel of the finding opens.
  10. Click **Take action**.
  11. From the **Take action** menu, select **Remove mute overrides**.



### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To set a finding's mute state to `UNDEFINED`, use the [`set-mute`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/findings/set-mute) command in the gcloud CLI:
         
         gcloud scc findings set-mute FINDING_ID \
           --PARENT=PARENT_ID \
           --location=LOCATION \
           --source=SOURCE_ID \
           --mute=UNDEFINED

Replace the following:

     * `FINDING_ID`: the ID for the finding you want to reset

To retrieve finding IDs, use the Security Command Center API to [list findings](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings). The finding ID is the last part of the `canonicalName` attribute, for example, `projects/123456789012/sources/1234567890123456789/findings/5ee30aa342e799e4e1700826de053aa9`.

     * `PARENT`: the parent resource (`project`, `folder`, or `organization` ), case-sensitive

     * `PARENT_ID`: the ID of the parent organization, folder, or project

     * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to mute or unmute findings; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`

     * `SOURCE_ID`: the source ID

For instructions on retrieving a source ID, see [Getting the source ID](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications#get-source-id).




### REST

In the Security Command Center API, use the [`findings.setMute`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings/setMute) method to reset the mute state of a finding. The request body is an enum that indicates the resulting mute state:
    
    
    POST https://securitycenter.googleapis.com/v2/PARENT/PARENT_ID/sources/SOURCE_ID/locations/LOCATION/findings/FINDING_ID:setMute
    
    {
      "mute": "UNDEFINED"
    }
    

Replace the following:

  * `PARENT`: the parent resource (`organizations`, `folders`, or `projects`)
  * `PARENT_ID`: the ID of the parent organization, folder, or project
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to mute or unmute findings; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`
  * `SOURCE_ID`: the numeric ID for the source



### Java
    
    
    import com.google.cloud.securitycenter.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html);
    import com.google.cloud.securitycenter.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html).[Mute](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.Mute.html);
    import com.google.cloud.securitycenter.v2.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html);
    import com.google.cloud.securitycenter.v2.[SetMuteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SetMuteRequest.html);
    import java.io.IOException;
    
    public class SetMuteUndefinedFinding {
    
      public static void main(String[] args) throws IOException {
        // TODO: Replace the variables within {}
    
        // findingPath: The relative resource name of the finding. See:
        // https://cloud.google.com/apis/design/resource_names#relative_resource_name
        // Use any one of the following formats:
        // - organizations/{organization_id}/sources/{source_id}/finding/{finding_id}
        // - folders/{folder_id}/sources/{source_id}/finding/{finding_id}
        // - projects/{project_id}/sources/{source_id}/finding/{finding_id}
        String findingPath = "{path-to-the-finding}";
        setMuteUndefined(findingPath);
      }
    
      // Reset mute state of an individual finding.
      // If a finding is already reset, resetting it again has no effect.
      // Various mute states are: MUTE_UNSPECIFIED/MUTE/UNMUTE/UNDEFINED.
      public static [Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html) setMuteUndefined(String findingPath) throws IOException {
        // Initialize client that will be used to send requests. This client only needs
        // to be created once, and can be reused for multiple requests.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html).create()) {
    
          [SetMuteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SetMuteRequest.html) setMuteRequest =
              [SetMuteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SetMuteRequest.html).newBuilder()
                  .setName(findingPath)
                  .setMute([Mute](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.Mute.html).UNDEFINED)
                  .build();
    
          [Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html) finding = client.setMute(setMuteRequest);
          System.out.println(
              "Mute value for the finding " + finding.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html#com_google_cloud_securitycenter_v2_Finding_getName__)() + " is: " + finding.[getMute](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.Finding.html#com_google_cloud_securitycenter_v2_Finding_getMute__)());
          return finding;
        }
      }
    }

## Mute or reset multiple existing findings

You can perform the following bulk mute operations for multiple existing findings by using either the `gcloud scc findings bulk-mute` gcloud CLI command, or the `bulkMute` method of the Security Command Center API:

  * Mute multiple existing findings. Muting existing findings in bulk mutes them _statically_ and overrides any dynamic mute rules that apply to the finding. If you need to mute similar future findings, [create a mute rule](https://docs.cloud.google.com/security-command-center/docs/manage-mute-rules#create_a_mute_rule).

  * Remove the mute state override on multiple existing findings. By removing the mute state override on a finding, you are resetting the mute state from `MUTED` (statically muted) or `UNMUTED` (statically unmuted) to `UNDEFINED`. This capability can be useful if you are [migrating from static to dynamic mute rules](https://docs.cloud.google.com/security-command-center/docs/dynamic-mute-migrate).




Specify the set of findings that you need to mute by defining a _finding filter_. Bulk mute filters don't support all finding properties. For a list of unsupported properties, see [Unsupported finding properties for mute rules](https://docs.cloud.google.com/security-command-center/docs/manage-mute-rules#mute_rule_unsupported_properties).

If data residency is enabled for Security Command Center, bulk mute operations are limited in scope to the Security Command Center location in which they are executed.

**Caution:** Bulk mute operations can time out if you attempt to mute more than approximately 4,000,000 existing findings or the operation takes longer than 6 hours. If you need to mute millions of existing findings, consider breaking up the mute operation by using multiple finding queries that match smaller numbers of findings.**Note:** Findings belonging to the finding class `SCC errors` report issues that prevent Security Command Center from working as expected. For this reason, error findings can't be muted. For more information, see [Overview of Security Command Center errors](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors).

For sample code that mutes findings in bulk, see [Bulk mute findings](https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-bulk-mute).

To mute or reset findings in bulk, click the tab for the procedure that you want to use:

### Console

In the Google Cloud console, you can only bulk mute findings by [creating mute rules](https://docs.cloud.google.com/security-command-center/docs/manage-mute-rules#create_a_mute_rule). In the Google Cloud console, creating mute rules silences existing and future findings.

### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To mute or reset multiple findings in bulk, run the `gcloud scc findings bulk-mute` command:
         
         gcloud scc findings bulk-mute \
           --PARENT=PARENT_ID \
           --location=LOCATION \
           --filter="FILTER" \
           --mute-state=MUTE_STATE

Replace the following:

     * `PARENT`: the scope in the resource hierarchy to which the mute rule applies, `organization`, `folder`, or `project`.
     * `PARENT_ID`: the numeric ID of the parent organization, folder, or project, or the alphanumeric ID of the parent project.
     * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to mute or unmute findings; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`.
     * `FILTER`: the expression you define to filter findings.

For example, to mute all existing low-severity `OPEN_FIREWALL` and `PUBLIC_IP_ADDRESS` findings in the `internal-test` project, your filter can be `"category=\"OPEN_FIREWALL\" OR category=\"PUBLIC_IP_ADDRESS\" AND severity=\"LOW\" AND resource.projectDisplayName=\"internal-test\""`.

     * `MUTE_STATE`: the value that indicates whether the finding is statically muted or not. Valid values are `MUTED` and `UNDEFINED`. The value is set to `MUTED` by default. Only set this value to `UNDEFINED` if you are resetting the mute state of multiple existing findings.




### REST

In the Security Command Center API, use the [`findings.bulkMute`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.findings/bulkMute) method to mute or reset the mute state of multiple existing findings. The request body contains the expression used to filter findings:
    
    
    POST https://securitycenter.googleapis.com/v2/PARENT/PARENT_ID/locations/LOCATION/findings:bulkMute
    
    {
      "filter": "FILTER",
      "muteState": "MUTE_STATE"
    }
    

Replace the following:

  * `PARENT`: the parent resource (`organizations`, `folders`, or `projects`).
  * `PARENT_ID`: the ID of the parent organization, folder, or project.
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to mute or unmute findings; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`.
  * `FILTER`: the expression you define to filter findings.

For example, to mute all existing low-severity `OPEN_FIREWALL` and `PUBLIC_IP_ADDRESS` findings in the `internal-test` project, your filter can be `"category=\"OPEN_FIREWALL\" OR category=\"PUBLIC_IP_ADDRESS\" AND severity=\"LOW\" AND resource.projectDisplayName=\"internal-test\""`.

  * `MUTE_STATE`: the value that indicates whether the finding is muted or not. Valid values are `MUTED` or `UNDEFINED`. The value is set to `MUTED` by default. Only set this value to `UNDEFINED` if you are resetting the mute state of multiple existing findings.




All existing findings in the resource you select, and which exactly match the filter, are hidden. The `mute` attribute for the findings is set to `MUTED`.

Muting findings doesn't change their state. If active findings are muted, they are hidden but remain active until the underlying vulnerabilities, misconfigurations, or threats are resolved.

## View muted findings in the Google Cloud console

You can view muted findings in the Google Cloud console by editing the finding query to select findings that include the property value `mute="MUTED"`.

For example, the following findings query displays only active findings that are muted:
    
    
    state="ACTIVE"
    AND mute="MUTED"
    

To display all active findings, both muted and unmuted, omit the `mute` attribute from the query entirely:
    
    
    state="ACTIVE"
    

By default, the finding query in the Google Cloud console displays only findings that are not muted.

### View findings muted by mute rule type

The following sections describe how to query active findings by mute rule type.

For more information on listing specific findings, see [Filter findings](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings#filter_findings).

#### Query findings muted by static mute rules

To display active findings that were muted by a _static_ mute rule after a specified time, use the following query and inspect the `muteInitiator` attribute to determine if the finding was muted by a static mute rule.
    
    
    state="ACTIVE" AND
    muteInfo.staticMute.applyTime>=TIMESTAMP AND
    muteInfo.staticMute.state="MUTED"
    

Replace the `TIMESTAMP` with the date and time string that indicates the beginning of the time period you want to query. For information about time formats, see [`gcloud topic datetimes`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes).

#### Query findings muted by dynamic mute rules

To display active findings that were muted by a _dynamic_ mute rule after a specified time, use the following query:
    
    
    state="ACTIVE" AND
    muteUpdateTime>=TIMESTAMP AND
    contains(muteInfo.dynamicMuteRecords, muteConfig="PARENT_ID/muteConfigs/CONFIG_ID")
    

Replace the following:

  * `TIMESTAMP`: the date and time string that indicates the beginning of the time period you want to query. For information about time formats, see [`gcloud topic datetimes`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes).
  * `PARENT_ID`: the ID of the parent organization, folder, or project, specified in the format of `organizations/123`, `folders/456`, or `projects/789`.
  * `CONFIG_ID`: the name of the mute rule. The ID must use alphanumeric characters and hyphens and be between 1 and 63 characters.



For more information about editing finding queries, see [Create or edit a findings query in the dashboard](https://docs.cloud.google.com/security-command-center/docs/how-to-work-with-findings-in-the-dashboard#create_or_edit_a_findings_query_in_the_dashboard).

## Stop notifications and exports of muted findings

If you [enable finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications), new or updated muted findings that match your notification filters are still exported to Pub/Sub.

To stop exports and notifications for muted findings, use the `mute` attribute to exclude muted findings in your `NotificationConfig` filter. For example, the following filter only sends notifications for active findings that are not muted or where the mute attribute hasn't been set:
    
    
    FILTER="state=\"ACTIVE\" AND -mute=\"MUTED\""
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

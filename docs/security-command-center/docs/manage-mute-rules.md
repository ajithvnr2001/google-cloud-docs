---
url: https://docs.cloud.google.com/security-command-center/docs/manage-mute-rules/
title: Manage mute rules \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:50.171270+00:00
---

# Manage mute rules  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/manage-mute-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Manage mute rules Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document explains how to create and manage mute rules to automatically mute findings in Security Command Center.

## Required roles

To get the permissions that you need to manage mute rules, ask your administrator to grant you the following IAM roles on the organization, folder, or project: 

  * View mute rules: 
    * [Security Center Admin Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)
    * [Security Center Settings Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsViewer) (`roles/securitycenter.settingsViewer`)
    * [Security Center Mute Configurations Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.muteConfigsViewer) (`roles/securitycenter.muteConfigsViewer`)
  * View, create, update, and delete mute rules: 
    * [Security Center Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)
    * [Security Center Admin Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminEditor) (`roles/securitycenter.adminEditor`)
    * [Security Center Settings Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.settingsEditor) (`roles/securitycenter.settingsEditor`)
    * [Security Center Mute Configurations Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.muteConfigsEditor) (`roles/securitycenter.muteConfigsEditor`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a mute rule

Your organization can create a maximum of 1,000 mute rules.

We recommend using dynamic mute rules exclusively in your mute rule configurations, because they're more flexible than static mute rules. For a comparison of mute rule types, see [Types of mute rules](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings#mute-types).

To create a mute rule, click the tab for the procedure that you want to use:

### Console

#### Define the mute rule

  1. In the Google Cloud console, go to the **Findings** page.

[Go to Findings](https://console.cloud.google.com/projectselector2/security/command-center/findings?supportedpurview=organizationId,project)

  2. Select an organization or project.

  3. Click **Mute options** , and then select **Manage mute rules**.

  4. Click **Create mute rule**.

  5. Enter a **Mute rule ID**.

  6. Recommended: Enter a **Description** that provides context for why findings are muted.

  7. To confirm the scope of the mute rule, check the **Parent resource** value.




#### Optional: Add an expiration date

You can add an expiration date to dynamic mute rules.

  1. Select **Mute matching findings temporarily**.
  2. To configure the expiration date for the dynamic mute rule, select the calendar and choose a date and time at least 24 hours in the future.

After the expiration date, the mute rule has no effect.




#### Optional: Limit the mute rule with a query

If you add a query, then the mute rule applies only to findings that match the query.

To limit the mute rule with a query, in the **Findings query** section, click add_circle_outline **Add filter**. 

The **Add filter** menu lets you choose supported finding attributes and values.

  1. In the **Select filter** menu, select a finding attribute or type its name in the **Search finding attributes** box. A list of the available sub-attributes displays.
  2. Select a sub-attribute. A selection field displays where you can build the query statement using the sub-attribute you selected, a query operator, and one or more values for the sub-attribute. 
  3. Select the operator and one or more values for the sub-attribute from the panel. For more information about query operators and functions that they use, see [Query operators in the **Add filters** menu](https://docs.cloud.google.com/security-command-center/docs/how-to-build-findings-query-console#query_operators_in_the_add_filters_menu).

If you want to start over, click **Reset**.

  4. Click **Apply**.

The menu closes and your query is updated.

  5. Repeat until the findings query contains all the attributes you want.

To check the query results, click **Preview matching findings**. A table lists findings that match your query. 

If the query doesn't match the correct findings, then revise the query as needed and preview the findings again. Repeat this step until you're satisfied with the results.

#### Save the mute rule

Click **Save**. The Google Cloud console shows a list of your mute rules.

### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To create mute rules, run the `gcloud scc muteconfigs create` command:
         
         gcloud scc muteconfigs create CONFIG_ID \
           --PARENT=PARENT_ID \
           --location=LOCATION \
           --description="RULE_DESCRIPTION" \
           --filter="FILTER" \
           --type=MUTE_TYPE \
           --expiry-time=TIMESTAMP

Replace the following:

     * `CONFIG_ID`: the name of the mute rule. The ID must use alphanumeric characters and hyphens and be between 1 and 63 characters.
     * `PARENT`: the scope in the resource hierarchy to which the mute rule applies, `organization`, `folder`, or `project`.
     * `PARENT_ID`: the numeric ID of the parent organization, folder, or project, or the alphanumeric ID of the parent project.
     * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to manage mute rules; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`.
     * `RULE_DESCRIPTION`: a description of the mute rule of no more than 1,024 characters.
     * `FILTER`: the expression you define to filter findings. For example, to mute `OPEN_FIREWALL` findings, your filter can be `FILTER="category=\"OPEN_FIREWALL\""`.
     * `MUTE_TYPE`: the type of mute rule you want to create. Valid mute rule types are `DYNAMIC` and `STATIC`. The mute rule type is set to `STATIC` by default. You can't change the type of a mute rule after you've created it.
     * `TIMESTAMP`: only applies if you are creating a dynamic mute rule. The date and time string that indicates when the dynamic mute rule expires. The value must be set to at least one day in the future or the request will be rejected. For information about time formats, see [`gcloud topic datetimes`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). When a dynamic mute rule expires, it is removed from all matched findings. To have the dynamic mute rule act indefinitely on matching findings, omit this field.

The response includes the mute rule ID, which you can use to view, update, and delete mute rules, as described in Manage mute rules.




### Terraform

Create a mute rule for an organization:
    
    
    resource "google_scc_v2_organization_mute_config" "default" {
      mute_config_id    = "my-config"
      organization = "123456789"
      location     = "global"
      description  = "My custom Cloud Security Command Center Finding Organization mute Configuration"
      filter = "severity = \"HIGH\""
      type = "STATIC"
    }
    

Create a mute rule for a folder:
    
    
    resource "google_folder" "folder" {
      parent       = "organizations/123456789"
      display_name = "folder-name"
    }
    
    resource "google_scc_v2_folder_mute_config" "default" {
      mute_config_id    = "my-config"
      folder = google_folder.folder.folder_id
      location     = "global"
      description  = "My custom Cloud Security Command Center Finding Folder mute Configuration"
      filter = "severity = \"HIGH\""
      type = "STATIC"
    }
    

Create a mute rule for a project:
    
    
    resource "google_scc_v2_project_mute_config" "default" {
      mute_config_id    = "my-config"
      project = "my-project-name"
      location     = "global"
      description  = "My custom Cloud Security Command Center Finding Project mute Configuration"
      filter = "severity = \"HIGH\""
      type = "STATIC"
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv2"
    	"cloud.google.com/go/securitycenter/apiv2/securitycenterpb"
    )
    
    // createMuteRule: Creates a mute configuration under a given scope that will mute
    // all new findings that match a given filter.
    // Existing findings will not be muted.
    func createMuteRule(w io.Writer, parent string, muteConfigId string) error {
    	// parent: Use any one of the following options:
    	//             - organizations/{organization_id}
    	//             - folders/{folder_id}
    	//             - projects/{project_id}
    	// parent := fmt.Sprintf("projects/%s", "your-google-cloud-project-id")
    	// muteConfigId: Set a random id; max of 63 chars.
    	// muteConfigId := "random-mute-id-" + uuid.New().String()
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_Close)()
    
    	muteConfig := &securitycenterpb.MuteConfig{
    		Description: "Mute low-medium IAM grants excluding 'compute' ",
    		// Set mute rule(s).
    		// To construct mute rules and for supported properties, see:
    		// https://cloud.google.com/security-command-center/docs/how-to-mute-findings#create_mute_rules
    		Filter: "severity=\"LOW\" OR severity=\"MEDIUM\" AND " +
    			"category=\"Persistence: IAM Anomalous Grant\" AND " +
    			"-resource.type:\"compute\"",
    		Type: securitycenterpb.[MuteConfig_STATIC](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2/securitycenterpb.html#cloud_google_com_go_securitycenter_apiv2_securitycenterpb_MuteConfig_MUTE_CONFIG_TYPE_UNSPECIFIED_MuteConfig_STATIC_MuteConfig_DYNAMIC),
    	}
    
    	req := &securitycenterpb.CreateMuteConfigRequest{
    		Parent:       parent,
    		MuteConfigId: muteConfigId,
    		MuteConfig:   muteConfig,
    	}
    
    	response, err := client.CreateMuteConfig(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to create mute rule: %w", err)
    	}
    	fmt.Fprintf(w, "Mute rule created successfully: %s", response.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_BulkMuteFindingsOperation_Name))
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.securitycenter.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.LocationName.html);
    import com.google.cloud.securitycenter.v2.[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig.html);
    import com.google.cloud.securitycenter.v2.[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig.html).[MuteConfigType](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig.MuteConfigType.html);
    import com.google.cloud.securitycenter.v2.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html);
    import java.io.IOException;
    import java.util.UUID;
    
    public class CreateMuteRule {
    
      public static void main(String[] args) throws IOException {
        // TODO: Replace the following variables.
        // projectId: Google Cloud Project id.
        String projectId = "google-cloud-project-id";
    
        // Specify the location of the mute config.
        String location = "global";
    
        // muteConfigId: Set a random id; max of 63 chars.
        String muteConfigId = "random-mute-id-" + UUID.randomUUID();
    
        createMuteRule(projectId, location, muteConfigId);
      }
    
      // Creates a mute configuration in a project under a given location.
      public static void createMuteRule(String projectId, String location, String muteConfigId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html).create()) {
    
          [MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig.html) muteConfig =
              [MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig.html).newBuilder()
                  .setDescription("Mute low-medium IAM grants excluding 'compute' ")
                  // Set mute rule(s).
                  // To construct mute rules and for supported properties, see:
                  // https://cloud.google.com/security-command-center/docs/how-to-mute-findings#create_mute_rules
                  .setFilter(
                      "severity=\"LOW\" OR severity=\"MEDIUM\" AND "
                          + "category=\"Persistence: IAM Anomalous Grant\" AND "
                          + "-resource.type:\"compute\"")
                  .setType([MuteConfigType](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig.MuteConfigType.html).STATIC)
                  .build();
    
          // You can also create mute rules in an organization/ folder.
          // Construct the parameters according to the parent resource.
          //  * Organization -> client.createMuteConfig(OrganizationLocationName.of(...
          //  * Folder -> client.createMuteConfig(FolderLocationName.of(...
          [MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig.html) response = client.createMuteConfig(
              [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.LocationName.html).of(projectId, location), muteConfig, muteConfigId);
          System.out.println("Mute rule created successfully: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig.html#com_google_cloud_securitycenter_v2_MuteConfig_getName__)());
        }
      }
    }

### Python
    
    
    def create_mute_rule(parent_path: str, location_id: str, mute_config_id: str) -> Dict:
        """
        Creates a mute configuration under a given scope that will mute
        all new findings that match a given filter.
        Existing findings will NOT BE muted.
        Args:
            parent_path: use any one of the following options:
                         - organizations/{organization_id}
                         - folders/{folder_id}
                         - projects/{project_id}
            location_id: Gcp location id; example: 'global'
            mute_config_id: Set a unique id; max of 63 chars.
        Returns:
            Dict: returns the mute rule details
        """
    
        from google.cloud import securitycenter_v2
    
        client = securitycenter_v2.SecurityCenterClient()
    
        mute_config = securitycenter_v2.MuteConfig()
        mute_config.description = "Mute low-medium IAM grants excluding 'compute' "
        # Set mute rule(s).
        # To construct mute rules and for supported properties, see:
        # https://cloud.google.com/security-command-center/docs/how-to-mute-findings#create_mute_rules
        mute_config.filter = (
            'severity="LOW" OR severity="MEDIUM" AND '
            'category="Persistence: IAM Anomalous Grant" AND '
            '-resource.type:"compute"'
        )
        mute_config.type = "STATIC"
    
        request = securitycenter_v2.CreateMuteConfigRequest()
        request.parent = parent_path + "/locations/" + location_id
        request.mute_config_id = mute_config_id
        request.mute_config = mute_config
    
        mute_config = client.[create_mute_config](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_create_mute_config)(request=request)
        print(f"Mute rule created successfully: {mute_config.name}")
        return mute_config
    
    

### REST

In the Security Command Center API, use the [`muteConfigs.create`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.muteConfigs) method to create a mute rule. The request body is an instance of `MuteConfig`:
    
    
    POST https://securitycenter.googleapis.com/v2/PARENT/PARENT_ID/locations/LOCATION/muteConfigs?muteConfigId=MUTE_CONFIG_ID -d
    
      {
        "description": "RULE_DESCRIPTION",
        "filter": "FILTER",
        "type": "MUTE_TYPE",
        "expiryTime": "TIMESTAMP"
      }
    

Replace the following:

  * `PARENT`: the parent resource for your mute rule (`organizations`, `folders`, or `projects`)
  * `PARENT_ID`: the ID of the parent organization, folder, or project
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to manage mute rules; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`
  * `MUTE_CONFIG_ID`: the name of the mute rule (between 1 and 63 characters)
  * `RULE_DESCRIPTION`: a description of the mute rule (max: 1,024 characters)
  * `FILTER`: the expression you define to filter findings

For example, to mute `OPEN_FIREWALL` findings, your filter can be `"category=\"OPEN_FIREWALL\""`.

  * `MUTE_TYPE`: the type of mute rule you want to create. Valid mute rule types are `DYNAMIC` and `STATIC`. You can't change the type of a mute rule after you've created it.

  * `TIMESTAMP`: only applies if you are creating a dynamic mute rule. The date and time string that indicates when the dynamic mute rule expires. The value must be set to at least one day in the future or the request will be rejected. For information about time formats, see [`gcloud topic datetimes`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). When a dynamic mute rule expires, it is removed from all matched findings. If you want the dynamic mute rule to act indefinitely on matching findings, omit this field.




The response includes the mute config ID, which you can use to view, update, and delete mute rules, as described in Manage mute rules.

New findings that exactly match the filter are hidden, and the `mute` attribute for the findings is set to `MUTED`.

### Unsupported finding properties for mute rules

Mute rules don't support all finding properties in filters. Expand the following section to see the list of properties that aren't supported in mute rule filters.

#### Unsupported finding properties

  * `caiResource`
  * `canonicalName`
  * `createTime`
  * `description`
  * `eventTime`
  * `externalUri`
  * `gcpMetadata.folders`1
  * `libraryPaths`
  * `mute`
  * `muteAnnotation`
  * `muteInfo`
  * `muteInitiator`
  * `muteUpdateTime`
  * `name`
  * `nextSteps`
  * `originalProviderId`
  * `parent`
  * `processes.binaryPath`
  * `processes.libraryPaths`
  * `propertyDataTypes`
  * `resource.tags`
  * `resourceName`
  * `securityMarks`
  * `sourceProperties`
  * `state`
  * `workflowState`

1The `gcpMetadata.folders` property contains subfields that are supported in mute filters.




### List mute rules

You can list the mute rules in an organization, folder, or project by using the Google Cloud console, the gcloud CLI, or the Security Command Center API.

Your ability to list mute rules for a given scope depends on the permissions that are granted to your IAM roles.

If data residency is enabled for Security Command Center, the scope of the list command is also limited to the selected [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations).

For sample code that lists mute rules, see [List mute rules](https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-mute-configs).

To list the mute rules for an organization, folder, or project, click the tab for the procedure that you want to use:

### Console

  1. In the Google Cloud console, go to the **Mute rules** tab in the Security Command Center **Settings** page. 

[ Go to Mute rules](https://console.cloud.google.com/security/command-center/config/mute-rules)

  2. If necessary, select your Google Cloud project or organization.

  3. In the **Mute rules** section, you see details for active mute rules, including the following:

     * **Name** : mute rule ID
     * **Parent resource** : the resource where the mute rule lives
     * **Description** : the mute rule description, if available
     * **Last updated by** : the principal who last updated the rule
     * **Last updated** : the date and time the rule was last updated



### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To list mute rules, run the `gcloud scc muteconfigs list` command:
         
         gcloud scc muteconfigs list --PARENT=PARENT_ID \
           --location=LOCATION

Replace the following:

     * `PARENT`: the parent `organization`, `folder`, or `project` for which to list mute rules
     * `PARENT_ID`: the ID of the parent organization, folder, or project
     * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to manage mute rules; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`



### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv2"
    	"cloud.google.com/go/securitycenter/apiv2/securitycenterpb"
    	"google.golang.org/api/iterator"
    )
    
    // listMuteRules lists mute configs at the organization level will return all the configs
    // at the org, folder, and project levels.
    // Similarly, listing configs at folder level will list all the configs
    // at the folder and project levels.
    func listMuteRules(w io.Writer, parent string) error {
    	// Use any one of the following resource paths to list mute configurations:
    	//         - organizations/{organization_id}
    	//         - folders/{folder_id}
    	//         - projects/{project_id}
    	// parent := fmt.Sprintf("projects/%s", "your-google-cloud-project-id")
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_Close)()
    
    	req := &securitycenterpb.ListMuteConfigsRequest{Parent: parent}
    
    	// List all mute configs present in the resource.
    	it := client.ListMuteConfigs(ctx, req)
    	for {
    		muteconfig, err := it.Next()
    		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_BulkMuteFindingsOperation_Done) {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("it.Next: %w", err)
    		}
    		fmt.Fprintf(w, "Muteconfig Name: %s, ", muteconfig.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_BulkMuteFindingsOperation_Name))
    	}
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.securitycenter.v2.[ListMuteConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListMuteConfigsRequest.html);
    import com.google.cloud.securitycenter.v2.[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig.html);
    import com.google.cloud.securitycenter.v2.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html);
    import java.io.IOException;
    
    public class ListMuteRules {
    
      public static void main(String[] args) throws IOException {
        // TODO: Replace variables enclosed within {}
        // projectId: Google Cloud Project id.
        String projectId = "google-cloud-project-id";
    
        // Specify the location to list mute configs.
        String location = "global";
    
        listMuteRules(projectId, location);
      }
    
      // Lists all mute rules present under the resource type in the given location.
      public static void listMuteRules(String projectId, String location) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html).create()) {
    
          // Parent can also be one of:
          //  * "organizations/{org_id}/locations/{location}"
          //  * "folders/{folder_id}/locations/{location}"
          [ListMuteConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListMuteConfigsRequest.html) listMuteConfigsRequest = [ListMuteConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.ListMuteConfigsRequest.html).newBuilder()
              .setParent(String.format("projects/%s/locations/%s", projectId, location))
              .build();
    
          // List all mute configs present in the resource.
          for ([MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig.html) muteConfig : client.listMuteConfigs(listMuteConfigsRequest).iterateAll()) {
            System.out.println(muteConfig.getName());
          }
        }
      }
    }

### Python
    
    
    def list_mute_rules(parent: str, location_id: str) -> Dict:
        """
        Listing mute configs at organization level will return all the configs
        at the org, folder and project levels.
        Similarly, listing configs at folder level will list all the configs
        at the folder and project levels.
        Args:
            parent: Use any one of the following resource paths to list mute configurations:
                    - organizations/{organization_id}
                    - folders/{folder_id}
                    - projects/{project_id}
            location_id: Gcp location id; example: 'global'
        Returns:
             Dict: returns the mute rule details
        """
        from google.cloud import securitycenter_v2
    
        client = securitycenter_v2.SecurityCenterClient()
    
        request = securitycenter_v2.ListMuteConfigsRequest()
        request.parent = parent + "/locations/" + location_id
        response = client.[list_mute_configs](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_list_mute_configs)(request)
        # List all Mute Configs present in the resource.
        for mute_config in response:
            print(mute_config.name)
        return response
    
    

### REST

In the Security Command Center API, use the [`muteConfigs.list`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.muteConfigs/list) method to list mute rules:
    
    
    GET https://securitycenter.googleapis.com/v2/PARENT/PARENT_ID/locations/LOCATION/muteConfigs
    

Replace the following:

  * `PARENT`: the parent resource for your mute rule (`organizations`, `folders`, or `projects`)
  * `PARENT_ID`: the ID of the parent organization, folder, or project
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to manage mute rules; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`



The response includes the names, descriptions, and mute config IDs for your mute rules.

### View a mute rule configuration

You can view a mute rule configuration by using the Google Cloud console, the gcloud CLI, or the Security Command Center API.

For sample code that retrieves a mute rule configuration, see [View a mute rule](https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-get-mute-config).

To view a mute rule configuration, click the tab for the procedure that you want to use:

### Console

  1. In the Google Cloud console, go to the **Mute rules** tab in the Security Command Center **Settings** page.

[ Go to Mute rules](https://console.cloud.google.com/security/command-center/config/mute-rules)

  2. If necessary, select your Google Cloud project or organization.

  3. In the **Mute rules** section, you see a list of mute rules.

  4. Click the name of the rule you want to view.

A page opens with the mute rule's configuration.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To view the configuration of a mute rule, run the `gcloud scc muteconfigs get` command:
         
         gcloud scc muteconfigs get MUTE_CONFIG_ID \
           --PARENT=PARENT_ID --location=LOCATION

Replace the following:

     * `MUTE_CONFIG_ID`: the ID for the mute rule
     * `PARENT`: the parent resource for your mute rule (`organization`, `folder`, or `project`)
     * `PARENT_ID`: the ID of the organization, folder, or project
     * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to manage mute rules; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`



### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv2"
    	"cloud.google.com/go/securitycenter/apiv2/securitycenterpb"
    )
    
    // getMuteRule retrieves a mute configuration given its resource name.
    func getMuteRule(w io.Writer, parent string, muteConfigId string) error {
    	// Use any one of the following resource paths to get mute configuration:
    	//         - organizations/{organization_id}
    	//         - folders/{folder_id}
    	//         - projects/{project_id}
    	// parent := fmt.Sprintf("projects/%s", "your-google-cloud-project-id")
    	//
    	// Name of the mute config to retrieve.
    	// muteConfigId := "mute-config-id"
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_Close)()
    
    	req := &securitycenterpb.GetMuteConfigRequest{
    		Name: fmt.Sprintf("%s/muteConfigs/%s", parent, muteConfigId),
    	}
    
    	muteconfig, err := client.GetMuteConfig(ctx, req)
    	if err != nil {
    		return fmt.Errorf("Failed to retrieve Muteconfig: %w", err)
    	}
    	fmt.Fprintf(w, "Muteconfig Name: %s ", muteconfig.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_BulkMuteFindingsOperation_Name))
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.securitycenter.v2.[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig.html);
    import com.google.cloud.securitycenter.v2.[MuteConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfigName.html);
    import com.google.cloud.securitycenter.v2.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html);
    import java.io.IOException;
    
    public class GetMuteRule {
    
      public static void main(String[] args) throws IOException {
        // TODO(Developer): Replace the following variables
        // projectId: Google Cloud Project id.
        String projectId = "google-cloud-project-id";
    
        // Specify the location of the mute config. If the mute config was
        // created with v1 API, it can be accessed with "global".
        String location = "global";
    
        // muteConfigId: Name of the mute config to retrieve.
        String muteConfigId = "mute-config-id";
    
        getMuteRule(projectId, location, muteConfigId);
      }
    
      // Retrieves a mute configuration given its resource name.
      public static [MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig.html) getMuteRule(String projectId, String location, String muteConfigId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html).create()) {
          // Use appropriate `MuteConfigName` methods depending on the parent type.
          //  * organization -> MuteConfigName.ofOrganizationLocationMuteConfigName()
          //  * folder -> MuteConfigName.ofFolderLocationMuteConfigName()
    
          [MuteConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfigName.html) muteConfigName = [MuteConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfigName.html).[ofProjectLocationMuteConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfigName.html#com_google_cloud_securitycenter_v2_MuteConfigName_ofProjectLocationMuteConfigName_java_lang_String_java_lang_String_java_lang_String_)(projectId,
              location, muteConfigId);
          return client.getMuteConfig(muteConfigName);
        }
      }
    }

### Python
    
    
    def get_mute_rule(parent_path: str, location_id: str, mute_config_id: str) -> Dict:
        """
        Retrieves a mute configuration given its resource name.
        Args:
            parent_path: use any one of the following options:
                         - organizations/{organization_id}
                         - folders/{folder_id}
                         - projects/{project_id}
            location_id: Gcp location id; example: 'global'
            mute_config_id: Set a unique id; max of 63 chars.
        Returns:
             Dict: returns the mute rule details
        """
        from google.cloud import securitycenter_v2
    
        client = securitycenter_v2.SecurityCenterClient()
    
        request = securitycenter_v2.GetMuteConfigRequest()
        request.name = (
            parent_path + "/locations/" + location_id + "/muteConfigs/" + mute_config_id
        )
    
        mute_config = client.[get_mute_config](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_get_mute_config)(request)
        print(f"Retrieved the mute rule: {mute_config.name}")
        return mute_config
    
    

### REST

In the Security Command Center API, use the [`muteConfigs.get`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.muteConfigs/get) method to return the configuration of a mute rule:
    
    
    GET https://securitycenter.googleapis.com/v2/PARENT/PARENT_ID/locations/LOCATION/muteConfigs/CONFIG_ID
    

Replace the following:

  * `PARENT`: the parent resource for your mute rule (`organizations`, `folders`, or `projects`)
  * `PARENT_ID`: the ID for the organization, folder, or project
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to manage mute rules; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`
  * `CONFIG_ID`: the numeric ID of the mute rule



### Update mute rules

You can update the description or finding filter of a mute rule by using the Google Cloud console, the gcloud CLI, or the Security Command Center API.

You can't change the ID; the parent organization, folder, or project; or the location of a mute rule. To change any of these values, you must create a new mute rule.

If you previously unmuted findings, they're muted again if they matched through a mute rule that is updated in the Google Cloud console. For more information, see [Unmute individual findings](https://docs.cloud.google.com/security-command-center/docs/mute-individual-findings#unmute_findings).

**Note:** Findings belonging to the finding class `SCC errors` report issues that prevent Security Command Center from working as expected. For this reason, error findings can't be muted. For more information, see [Overview of Security Command Center errors](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors).

For sample code that updates a mute rule, see [Update a mute rule](https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-update-mute-config).

To update a mute rule, click the tab for the procedure that you want to use:

### Console

  1. In the Google Cloud console, go to the **Mute rules** tab in the Security Command Center **Settings** page. 

[ Go to Mute rules](https://console.cloud.google.com/security/command-center/config/mute-rules)

  2. Select the Google Cloud project or organization that is the parent resource for the mute rule you want to modify.

  3. Click the name of the mute rule you want to modify.

If you didn't select the appropriate project or organization, you might see a note informing you that you don't have permission to modify the mute rule.

  4. Make changes to the mute rule.

  5. Optional: After you update the filter, click **Preview Matching Findings** to view findings that match the updated filter. A table loads with findings that match the new query.

  6. Click **Save**.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To update mute rules, run the `gcloud scc muteconfigs update` command:
         
         gcloud scc muteconfigs update MUTE_CONFIG_ID \
             --PARENT=PARENT_ID \
             --location=LOCATION \
             --description=RULE_DESCRIPTION \
             --filter=FILTER \
             --type=MUTE_TYPE \
             --expiry-time=TIMESTAMP
         

Replace the following:

     * `MUTE_CONFIG_ID`: the ID for the mute rule.
     * `PARENT`: the parent resource for your mute rule (`organization`, `folder`, or `project`).
     * `PARENT_ID`: the ID for the organization, folder, or project.
     * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to manage mute rules; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`.
     * `RULE_DESCRIPTION`: a description of the mute rule (max: 1,024 characters).
     * `FILTER`: the expression you define to filter findings.

For example, to mute `OPEN_FIREWALL` findings, your filter could be `FILTER="category=\"OPEN_FIREWALL\""`.

     * `MUTE_TYPE`: the type of mute rule you are updating. Valid mute rule types are `DYNAMIC` and `STATIC`. You can't change the type of a mute rule once you've created it.

     * `TIMESTAMP`: only applies if you are updating a dynamic mute rule. The date and time string that indicates when the dynamic mute rule expires. The value must be set to at least one day in the future or the request will be rejected. For information about time formats, see [`gcloud topic datetimes`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). When a dynamic mute rule expires, it is removed from all matched findings. If you want the dynamic mute rule to act indefinitely on matching findings, omit this field.




### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv2"
    	"cloud.google.com/go/securitycenter/apiv2/securitycenterpb"
    	"google.golang.org/protobuf/types/known/fieldmaskpb"
    )
    
    // updateMuteRule Updates an existing mute configuration.
    // The following can be updated in a mute config: description and filter.
    func updateMuteRule(w io.Writer, muteConfigName string) error {
    	// Specify the name of the mute config to delete.
    	// muteConfigName: Use any one of the following formats:
    	//                 - organizations/{organization}/muteConfigs/{config_id}
    	//                 - folders/{folder}/muteConfigs/{config_id}
    	//                 - projects/{project}/muteConfigs/{config_id}
    	// muteConfigName := fmt.Sprintf("projects/%s/muteConfigs/%s", "project-id", "mute-config")
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_Close)()
    
    	updateMuteConfig := &securitycenterpb.MuteConfig{
    		Name:        muteConfigName,
    		Description: "Updated mute config description",
    	}
    
    	req := &securitycenterpb.UpdateMuteConfigRequest{
    		MuteConfig: updateMuteConfig,
    		// Set the update mask to specify which properties of the mute config should be
    		// updated.
    		// If empty, all mutable fields will be updated.
    		// Make sure that the mask fields match the properties changed in 'updateMuteConfig'.
    		// For more info on constructing update mask path, see the proto or:
    		// https://cloud.google.com/security-command-center/docs/reference/rest/v1/folders.muteConfigs/patch?hl=en#query-parameters
    		UpdateMask: &fieldmaskpb.FieldMask{
    			Paths: []string{
    				"description",
    			},
    		},
    	}
    
    	response, err := client.UpdateMuteConfig(ctx, req)
    	if err != nil {
    		return fmt.Errorf("mute rule update failed! %w", err)
    	}
    	fmt.Fprintf(w, "Mute rule updated %s", response.[Name](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_BulkMuteFindingsOperation_Name))
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.securitycenter.v2.[MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig.html);
    import com.google.cloud.securitycenter.v2.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html);
    import com.google.cloud.securitycenter.v2.[UpdateMuteConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateMuteConfigRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    
    public class UpdateMuteRule {
    
      public static void main(String[] args) throws IOException {
        // TODO: Replace the variables within {}
        // projectId: Google Cloud Project id.
        String projectId = "google-cloud-project-id";
    
        // Specify the location of the mute config to update. If the mute config was
        // created with v1 API, it can be accessed with "global".
        String location = "global";
    
        // muteConfigId: Name of the mute config to update.
        String muteConfigId = "mute-config-id";
    
        updateMuteRule(projectId, location, muteConfigId);
      }
    
      // Updates an existing mute configuration.
      // The following can be updated in a mute config: description and filter.
      public static void updateMuteRule(String projectId, String location, String muteConfigId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html) securityCenterClient = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html).create()) {
    
          [MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig.html) updateMuteConfig =
              [MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig.html).newBuilder()
                  // Construct the name according to the parent type of the mute rule.
                  // Parent can also be one of:
                  //  * "organizations/{org_id}/locations/{location}/muteConfigs/{muteConfig_id}"
                  //  * "folders/{folder_id}/locations/{location}/muteConfigs/{muteConfig_id}"
                  .setName(String.format("projects/%s/locations/%s/muteConfigs/%s", projectId, location,
                      muteConfigId))
                  .setDescription("Updated mute config description")
                  .build();
    
          [UpdateMuteConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateMuteConfigRequest.html) updateMuteConfigRequest =
              [UpdateMuteConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.UpdateMuteConfigRequest.html).newBuilder()
                  .setMuteConfig(updateMuteConfig)
                  // Make sure that the mask fields match the properties changed in
                  // 'updateMuteConfig' object.
                  // For more info on constructing update mask path, see the proto or:
                  // https://cloud.google.com/security-command-center/docs/reference/rest/v2/folders.muteConfigs/patch?hl=en#query-parameters
                  .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("description").build())
                  .build();
    
          [MuteConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfig.html) response = securityCenterClient.updateMuteConfig(updateMuteConfigRequest);
          System.out.println(response);
        }
      }
    }

### Python
    
    
    def update_mute_rule(parent_path: str, location_id: str, mute_config_id: str) -> Dict:
        """
        Updates an existing mute configuration.
        The following can be updated in a mute config: description, and filter/ mute rule.
        Args:
            parent: Use any one of the following resource paths to list mute configurations:
                    - organizations/{organization_id}
                    - folders/{folder_id}
                    - projects/{project_id}
            location_id: Gcp location id; example: 'global'
            mute_config_id: Set a unique id; max of 63 chars.
        Returns:
             Dict: returns the mute rule details
        """
        from google.cloud import securitycenter_v2
        from google.protobuf import field_mask_pb2
    
        client = securitycenter_v2.SecurityCenterClient()
    
        update_mute_config = securitycenter_v2.MuteConfig()
        update_mute_config.name = (
            parent_path + "/locations/" + location_id + "/muteConfigs/" + mute_config_id
        )
        update_mute_config.description = "Updated mute config description"
    
        field_mask = field_mask_pb2.FieldMask(paths=["description"])
    
        request = securitycenter_v2.UpdateMuteConfigRequest()
        request.mute_config = update_mute_config
        # Set the update mask to specify which properties of the Mute Config should be updated.
        # If empty, all mutable fields will be updated.
        # Make sure that the mask fields match the properties changed in 'update_mute_config'.
        # For more info on constructing update mask path, see the proto or:
        # https://cloud.google.com/security-command-center/docs/reference/rest/v1/folders.muteConfigs/patch?hl=en#query-parameters
        request.update_mask = field_mask
    
        mute_config = client.[update_mute_config](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_update_mute_config)(request)
        print(f"Updated mute rule : {mute_config}")
        return mute_config
    
    

### REST

In the Security Command Center API, use the [`muteConfigs.patch`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.muteConfigs/patch) method to update a mute rule. The request body is an instance of `MuteConfig`:
    
    
    PATCH https://securitycenter.googleapis.com/v2/PARENT/PARENT_ID/locations/LOCATION/muteConfigs/CONFIG_ID
    
      {
        "description": "RULE_DESCRIPTION",
        "filter": "FILTER",
        "type": "MUTE_TYPE",
        "expiryTime": "TIMESTAMP"
      }
    

Replace the following:

  * `PARENT`: the parent resource for your mute rule (`organizations`, `folders`, or `projects`)
  * `PARENT_ID`: the ID for the organization, folder, or project
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to manage mute rules; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`
  * `CONFIG_ID`: the numeric ID of the mute rule
  * `RULE_DESCRIPTION`: a description of the mute rule (max: 1,024 characters)
  * `FILTER`: the expression you define to filter findings
  * `MUTE_TYPE`: the type of mute rule you are updating. Valid mute rule types are `DYNAMIC` and `STATIC`. You can't change the type of a mute rule once you've created it.
  * `TIMESTAMP`: only applies if you are updating a dynamic mute rule. The date and time string that indicates when the dynamic mute rule expires. The value must be set to at least one day in the future or the request will be rejected. For information about time formats, see [`gcloud topic datetimes`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). When a dynamic mute rule expires, it is removed from all matched findings. If you want the dynamic mute rule to act indefinitely on matching findings, omit this field.



### Delete mute rules

You can delete a mute rule by using the Google Cloud console, the gcloud CLI, or the Security Command Center API.

Before deleting mute rules, understand the following:

  * You can't recover deleted mute rules.
  * Deleting _static_ mute rules doesn't automatically unmute any findings that are muted. You must manually or programmatically [unmute findings](https://docs.cloud.google.com/security-command-center/docs/mute-individual-findings#unmute_findings).
  * Deleting _dynamic_ mute rules automatically removes the rule from all previously matching findings and unmutes them if they don't match any additional rules.
  * Future findings that match filters in deleted mute rules aren't muted.



For sample code that deletes a mute rule, see [Delete a mute rule](https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-delete-mute-config).

To delete a mute rule, click the tab for the procedure that you want to use:

### Console

  1. In the Google Cloud console, go to the **Mute rules** tab in the Security Command Center **Settings** page. 

[ Go to Mute rules](https://console.cloud.google.com/security/command-center/config/mute-rules)

  2. If necessary, select your Google Cloud project or organization.

  3. Click the name of the mute rule you want to delete.

  4. Click _delete_ **Delete**.

  5. Read the dialog and, if satisfied, click **Delete**.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To delete mute rules, run the `gcloud scc muteconfigs delete` command:
         
         gcloud scc muteconfigs delete MUTE_CONFIG_ID \
           --PARENT=PARENT_ID --location=LOCATION

Replace the following:

     * `MUTE_CONFIG_ID`: the ID for the mute config
     * `PARENT`: the parent resource for your mute rule (`organization`, `folder`, or `project`)
     * `PARENT_ID`: the ID for the organization, folder, or project
     * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to manage mute rules; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`
  3. Confirm your request to delete the mute rule.




### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	securitycenter "cloud.google.com/go/securitycenter/apiv2"
    	"cloud.google.com/go/securitycenter/apiv2/securitycenterpb"
    )
    
    // deleteMuteRule deletes a mute configuration given its resource name.
    // Note: Previously muted findings are not affected when a mute config is deleted.
    func deleteMuteRule(w io.Writer, parent string, muteConfigId string) error {
    	// parent: Use any one of the following options:
    	//             - organizations/{organization_id}
    	//             - folders/{folder_id}
    	//             - projects/{project_id}
    	// parent := fmt.Sprintf("projects/%s", "your-google-cloud-project-id")
    	//
    	// muteConfigId: Specify the name of the mute config to delete.
    	// muteConfigId := "mute-config-id"
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv2.html#cloud_google_com_go_securitycenter_apiv2_Client_Close)()
    
    	req := &securitycenterpb.DeleteMuteConfigRequest{
    		Name: fmt.Sprintf("%s/muteConfigs/%s", parent, muteConfigId),
    	}
    
    	if err := client.DeleteMuteConfig(ctx, req); err != nil {
    		return fmt.Errorf("failed to delete Muteconfig: %w", err)
    	}
    	fmt.Fprintf(w, "Mute rule deleted successfully: %s", muteConfigId)
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.securitycenter.v2.[MuteConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfigName.html);
    import com.google.cloud.securitycenter.v2.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html);
    import java.io.IOException;
    
    public class DeleteMuteRule {
    
      public static void main(String[] args) throws IOException {
        // TODO(Developer): Replace the following variables
        // projectId: Google Cloud Project id.
        String projectId = "google-cloud-project-id";
    
        // Specify the location of the mute config. If the mute config was
        // created with v1 API, it can be accessed with "global".
        String location = "global";
    
        // muteConfigId: Specify the name of the mute config to delete.
        String muteConfigId = "mute-config-id";
    
        deleteMuteRule(projectId, location, muteConfigId);
      }
    
      // Deletes a mute configuration given its resource name.
      // Note: Previously muted findings are not affected when a mute config is deleted.
      public static void deleteMuteRule(String projectId, String location, String muteConfigId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.SecurityCenterClient.html).create()) {
          // Use appropriate `MuteConfigName` methods depending on the parent type.
          // folder -> MuteConfigName.ofFolderLocationMuteConfigName()
          // organization -> MuteConfigName.ofOrganizationLocationMuteConfigName()
          client.deleteMuteConfig(
              [MuteConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfigName.html).[ofProjectLocationMuteConfigName](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v2.MuteConfigName.html#com_google_cloud_securitycenter_v2_MuteConfigName_ofProjectLocationMuteConfigName_java_lang_String_java_lang_String_java_lang_String_)(projectId, location, muteConfigId));
    
          System.out.println("Mute rule deleted successfully: " + muteConfigId);
        }
      }
    }

### Python
    
    
    def delete_mute_rule(parent_path: str, location_id: str, mute_config_id: str) -> None:
        """
        Deletes a mute configuration given its resource name.
        Note: Previously muted findings are not affected when a mute config is deleted.
        Args:
             parent_path: use any one of the following options:
                         - organizations/{organization_id}
                         - folders/{folder_id}
                         - projects/{project_id}
            location_id: Gcp location id; example: 'global'
            mute_config_id: Set a unique id; max of 63 chars.
        Returns:
             None: returns none mute rule is deleted
        """
        from google.cloud import securitycenter_v2
    
        client = securitycenter_v2.SecurityCenterClient()
    
        request = securitycenter_v2.DeleteMuteConfigRequest()
        request.name = (
            parent_path + "/locations/" + location_id + "/muteConfigs/" + mute_config_id
        )
    
        client.[delete_mute_config](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1.services.security_center.SecurityCenterClient.html#google_cloud_securitycenter_v1_services_security_center_SecurityCenterClient_delete_mute_config)(request)
        print(f"Mute rule deleted successfully: {mute_config_id}")
    
    

### REST

In the Security Command Center API, use the [`muteConfigs.delete`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.muteConfigs/delete) method to delete a mute rule:
    
    
    DELETE https://securitycenter.googleapis.com/v2/PARENT/PARENT_ID/locations/LOCATION/muteConfigs/CONFIG_ID
    

Replace the following:

  * `PARENT`: the parent resource for your mute rule (`organizations`, `folders`, or `projects`)
  * `PARENT_ID`: the ID for the organization, folder, or project
  * `LOCATION`: the [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) in which to manage mute rules; if data residency is enabled, use `eu`, `sa`, or `us`; otherwise, use the value `global`
  * `CONFIG_ID`: the numeric ID of the mute rule



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-notification-configs/
title: List NotificationConfigs \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:15.990994+00:00
---

# List NotificationConfigs  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-list-notification-configs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  List NotificationConfigs Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to list NotificationConfigs

## Code sample

### C#

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Cloud.SecurityCenter.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.html);
    using System;
    
    /// <summary>Snippet for ListNotificationConfig</summary>
    public class ListNotificationConfigSnippets
    {
        public static PagedEnumerable<ListNotificationConfigsResponse, NotificationConfig> ListNotificationConfigs(string organizationId)
        {
            // You can also use 'projectId' or 'folderId' instead of the 'organizationId'.
            //      ProjectName projectName = new ProjectName(projectId);
            //      FolderName folderName = new FolderName(folderId);
            [OrganizationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.OrganizationName.html) orgName = new [OrganizationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.OrganizationName.html)(organizationId);
            [SecurityCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.SecurityCenterClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.SecurityCenterClient.html#Google_Cloud_SecurityCenter_V1_SecurityCenterClient_Create)();
            PagedEnumerable<ListNotificationConfigsResponse, NotificationConfig> notificationConfigs = client.[ListNotificationConfigs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.SecurityCenterClient.html#Google_Cloud_SecurityCenter_V1_SecurityCenterClient_ListNotificationConfigs_Google_Api_Gax_ResourceNames_FolderName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(orgName);
    
            // Print Notification Configuration names.
            foreach (var config in notificationConfigs)
            {
                Console.WriteLine(config.[NotificationConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.NotificationConfigName.html));
            }
            return notificationConfigs;
        }
    }

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
    
    func listNotificationConfigs(w io.Writer, orgID string) error {
    	// orgId := "your-org-id"
    
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)()
    
    	req := &securitycenterpb.ListNotificationConfigsRequest{
    		// Parent must be in one of the following formats:
    		//		"organizations/{orgId}"
    		//		"projects/{projectId}"
    		//		"folders/{folderId}"
    		Parent: fmt.Sprintf("organizations/%s", orgID),
    	}
    	it := client.ListNotificationConfigs(ctx, req)
    	for {
    		result, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    
    		if err != nil {
    			return fmt.Errorf("it.Next: %w", err)
    		}
    
    		fmt.Fprintln(w, "NotificationConfig: ", result)
    	}
    
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycenter.v1.[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.NotificationConfig.html);
    import com.google.cloud.securitycenter.v1.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html);
    import com.google.cloud.securitycenter.v1.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html).[ListNotificationConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.ListNotificationConfigsPagedResponse.html);
    import com.google.common.collect.ImmutableList;
    import java.io.IOException;
    
    public class ListNotificationConfigSnippets {
    
      public static void main(String[] args) throws IOException {
        // parentId: must be in one of the following formats:
        //    "organizations/{organization_id}"
        //    "projects/{project_id}"
        //    "folders/{folder_id}"
        String parentId = String.format("organizations/%s", "ORG_ID");
    
        listNotificationConfigs(parentId);
      }
    
      // List notification configs present in the given parent.
      public static ImmutableList<NotificationConfig> listNotificationConfigs(String parentId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html).create()) {
    
          [ListNotificationConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.ListNotificationConfigsPagedResponse.html) response = client.listNotificationConfigs(parentId);
    
          ImmutableList<NotificationConfig> notificationConfigs =
              ImmutableList.copyOf(response.iterateAll());
    
          System.out.printf("List notifications response: %s%n", response.getPage().getValues());
          return notificationConfigs;
        }
      }
    }

### Node.js

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // npm install @google-cloud/security-center/
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)');
    
    const client = new [SecurityCenterClient](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)();
    
    // parent: must be in one of the following formats:
    //    `organizations/${organization_id}`
    //    `projects/${project_id}`
    //    `folders/${folder_id}`
    const parent = `organizations/${organizationId}`;
    
    async function listNotificationConfigs() {
      const [resources] = await client.listNotificationConfigs({parent: parent});
      console.log('Received Notification configs: ');
      for (const resource of resources) {
        console.log(resource);
      }
    }
    
    listNotificationConfigs();

### PHP

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\SecurityCenter\V1\Client\SecurityCenterClient;
    use Google\Cloud\SecurityCenter\V1\ListNotificationConfigsRequest;
    
    /**
     * @param string $organizationId        Your org ID
     */
    function list_notification(string $organizationId): void
    {
        $securityCenterClient = new SecurityCenterClient();
        // 'parent' must be in one of the following formats:
        //		"organizations/{orgId}"
        //		"projects/{projectId}"
        //		"folders/{folderId}"
        $parent = $securityCenterClient::organizationName($organizationId);
        $listNotificationConfigsRequest = (new ListNotificationConfigsRequest())
            ->setParent($parent);
    
        foreach ($securityCenterClient->listNotificationConfigs($listNotificationConfigsRequest) as $element) {
            printf('Found notification config %s' . PHP_EOL, $element->getName());
        }
    
        print('Notification configs were listed' . PHP_EOL);
    }

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def list_notification_configs(parent_id):
        """
        Args:
            parent_id: must be in one of the following formats:
                "organizations/{organization_id}"
                "projects/{project_id}"
                "folders/{folder_id}"
        """
        from google.cloud import securitycenter as securitycenter
    
        client = securitycenter.SecurityCenterClient()
    
        notification_configs_iterator = client.list_notification_configs(
            request={"parent": parent_id}
        )
        for i, config in enumerate(notification_configs_iterator):
            print(f"{i}: notification_config: {config}")

### Ruby

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/security_center"
    
    # Your organization id. e.g. for "organizations/123", this would be "123".
    # org_id = "YOUR_ORGANZATION_ID"
    
    # Your location. e.g. "global" or "us".
    # location = "global"
    
    client = Google::Cloud::[SecurityCenter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center/latest/Google-Cloud-SecurityCenter.html).[security_center](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center/latest/Google-Cloud-SecurityCenter.html)
    
    # You can also use a project or folder as a parent.
    parent = client.organization_location_path organization: org_id, location: location
    
    client.list_notification_configs(parent: parent).each_page do |page|
      page.each do |element|
        puts element
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

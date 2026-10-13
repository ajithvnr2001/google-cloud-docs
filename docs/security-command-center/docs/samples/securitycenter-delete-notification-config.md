---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-delete-notification-config/
title: Delete a NotificationConfig \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:53:21.105583+00:00
---

# Delete a NotificationConfig  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-delete-notification-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Delete a NotificationConfig Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to delete a NotificationConfig

## Code sample

### C#

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.SecurityCenter.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.html);
    using System;
    
    /// <summary>Snippet for DeleteNotificationConfig</summary>
    public class DeleteNotificationConfigSnippets
    {
        public static bool DeleteNotificationConfig(string organizationId, string notificationConfigId)
        {
            // You can also use 'projectId' or 'folderId' instead of the 'organizationId'.
            [NotificationConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.NotificationConfigName.html) notificationConfigName = new [NotificationConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.NotificationConfigName.html)(organizationId, notificationConfigId);
            [SecurityCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.SecurityCenterClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.SecurityCenterClient.html#Google_Cloud_SecurityCenter_V1_SecurityCenterClient_Create)();
    
            client.[DeleteNotificationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.SecurityCenterClient.html#Google_Cloud_SecurityCenter_V1_SecurityCenterClient_DeleteNotificationConfig_Google_Cloud_SecurityCenter_V1_DeleteNotificationConfigRequest_Google_Api_Gax_Grpc_CallSettings_)(notificationConfigName);
            Console.WriteLine($"Deleted Notification config: {notificationConfigName}");
            return true;
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
    )
    
    func deleteNotificationConfig(w io.Writer, orgID string, notificationConfigID string) error {
    	// orgID := "your-org-id"
    	// notificationConfigID := "config-to-delete"
    
    	ctx := context.Background()
    	client, err := securitycenter.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_NewClient)(ctx)
    
    	if err != nil {
    		return fmt.Errorf("securitycenter.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/securitycenter/latest/apiv1.html#cloud_google_com_go_securitycenter_apiv1_Client_Close)()
    
    	// Parent must be in one of the following formats:
    	//		"organizations/{orgId}"
    	//		"projects/{projectId}"
    	//		"folders/{folderId}"
    	parent := fmt.Sprintf("organizations/%s", orgID)
    	name := fmt.Sprintf("%s/notificationConfigs/%s", parent, notificationConfigID)
    	req := &securitycenterpb.DeleteNotificationConfigRequest{
    		Name: name,
    	}
    
    	if err = client.DeleteNotificationConfig(ctx, req); err != nil {
    		return fmt.Errorf("Failed to retrieve notification config: %w", err)
    	}
    	fmt.Fprintln(w, "Deleted config: ", name)
    
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycenter.v1.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html);
    import java.io.IOException;
    
    public class DeleteNotificationConfigSnippets {
    
      public static void main(String[] args) throws IOException {
        // parentId: must be in one of the following formats:
        //    "organizations/{organization_id}"
        //    "projects/{project_id}"
        //    "folders/{folder_id}"
        String parentId = String.format("organizations/%s", "ORG_ID");
    
        String notificationConfigId = "{config-id}";
    
        deleteNotificationConfig(parentId, notificationConfigId);
      }
    
      // Delete a notification config.
      public static boolean deleteNotificationConfig(String parentId, String notificationConfigId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html).create()) {
    
          client.deleteNotificationConfig(String.format("%s/notificationConfigs/%s",
              parentId, notificationConfigId));
    
          System.out.printf("Deleted Notification config: %s%n", notificationConfigId);
        }
        return true;
      }
    }

### Node.js

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // npm install @google-cloud/security-center/
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)');
    
    const client = new [SecurityCenterClient](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)();
    
    const formattedConfigName = `organizations/${organizationId}/notificationConfigs/${configId}`;
    
    async function deleteNotificationConfg() {
      await client.deleteNotificationConfig({name: formattedConfigName});
      console.log('Notification config deleted: ', formattedConfigName);
    }
    
    deleteNotificationConfg();

### PHP

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\SecurityCenter\V1\Client\SecurityCenterClient;
    use Google\Cloud\SecurityCenter\V1\DeleteNotificationConfigRequest;
    
    /**
     * @param string $organizationId        Your org ID
     * @param string $notificationConfigId  A unique identifier
     */
    function delete_notification(string $organizationId, string $notificationConfigId): void
    {
        $securityCenterClient = new SecurityCenterClient();
        $notificationConfigName = $securityCenterClient::notificationConfigName(
            // You can also use 'projectId' or 'folderId' instead of the 'organizationId'.
            $organizationId,
            $notificationConfigId
        );
        $deleteNotificationConfigRequest = (new DeleteNotificationConfigRequest())
            ->setName($notificationConfigName);
    
        $securityCenterClient->deleteNotificationConfig($deleteNotificationConfigRequest);
        print('Notification config was deleted' . PHP_EOL);
    }

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def delete_notification_config(parent_id, notification_config_id):
        """
        Args:
            parent_id: must be in one of the following formats:
                "organizations/{organization_id}"
                "projects/{project_id}"
                "folders/{folder_id}"
            notification_config_id: "your-config-id"
        """
        from google.cloud import securitycenter as securitycenter
    
        client = securitycenter.SecurityCenterClient()
    
        notification_config_name = (
            f"{parent_id}/notificationConfigs/{notification_config_id}"
        )
    
        client.delete_notification_config(request={"name": notification_config_name})
        print(f"Deleted notification config: {notification_config_name}")

### Ruby

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/security_center"
    
    # Your organization id. e.g. for "organizations/123", this would be "123".
    # org_id = "YOUR_ORGANZATION_ID"
    
    # Your location. e.g. "global" or "us".
    # location = "global"
    
    # Your notification config id. e.g. for
    # "organizations/123/notificationConfigs/my-config" this would be "my-config".
    # config_id = "YOUR_CONFIG_ID"
    
    client = Google::Cloud::[SecurityCenter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v1p1beta1/latest/Google-Cloud-SecurityCenter.html).[security_center](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center/latest/Google-Cloud-SecurityCenter.html)
    
    # You can also use a project or folder as a parent.
    config_path = client.notification_config_path organization:        org_id,
                                                  location:            location,
                                                  notification_config: config_id
    
    response = client.delete_notification_config name: config_path
    puts "Deleted notification config #{config_id} with response: #{response}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

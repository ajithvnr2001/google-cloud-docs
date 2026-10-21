---
url: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-get-notification-config/
title: Get a NotificationConfig \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:57.169642+00:00
---

# Get a NotificationConfig  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/samples/securitycenter-get-notification-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Samples ](https://docs.cloud.google.com/security-command-center/docs/samples)



#  Get a NotificationConfig Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to retrieve NotificationConfigs

## Code sample

### C#

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.SecurityCenter.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.html);
    using System;
    
    /// <summary>Snippet for GetNotificationConfig</summary>
    public class GetNotificationConfigSnippets
    {
        public static NotificationConfig GetNotificationConfig(string organizationId, string configId)
        {
            [SecurityCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.SecurityCenterClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.SecurityCenterClient.html#Google_Cloud_SecurityCenter_V1_SecurityCenterClient_Create)();
            // You can also use 'projectId' or 'folderId' instead of the 'organizationId'.
            [NotificationConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.NotificationConfigName.html) notificationConfigName = new [NotificationConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.NotificationConfigName.html)(organizationId, configId);
    
            [NotificationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.NotificationConfig.html) response = client.[GetNotificationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1/latest/Google.Cloud.SecurityCenter.V1.SecurityCenterClient.html#Google_Cloud_SecurityCenter_V1_SecurityCenterClient_GetNotificationConfig_Google_Cloud_SecurityCenter_V1_GetNotificationConfigRequest_Google_Api_Gax_Grpc_CallSettings_)(notificationConfigName);
            Console.WriteLine($"Notification config: {response}");
            return response;
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
    
    func getNotificationConfig(w io.Writer, orgID string, notificationConfigID string) error {
    	// orgID := "your-org-id"
    	// notificationConfigID := "your-config-id"
    
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
    	req := &securitycenterpb.GetNotificationConfigRequest{
    		Name: fmt.Sprintf("%s/notificationConfigs/%s", parent, notificationConfigID),
    	}
    
    	notificationConfig, err := client.GetNotificationConfig(ctx, req)
    	if err != nil {
    		return fmt.Errorf("Failed to retrieve notification config: %w", err)
    	}
    	fmt.Fprintln(w, "Received config: ", notificationConfig)
    
    	return nil
    }
    

### Java

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.securitycenter.v1.[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.NotificationConfig.html);
    import com.google.cloud.securitycenter.v1.[SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html);
    import java.io.IOException;
    
    public class GetNotificationConfigSnippets {
    
      public static void main(String[] args) throws IOException {
        // parentId: must be in one of the following formats:
        //    "organizations/{organization_id}"
        //    "projects/{project_id}"
        //    "folders/{folder_id}"
        String parentId = String.format("organizations/%s", "ORG_ID");
    
        String notificationConfigId = "{config-id}";
    
        getNotificationConfig(parentId, notificationConfigId);
      }
    
      // Retrieve an existing notification config.
      public static [NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.NotificationConfig.html) getNotificationConfig(
          String parentId, String notificationConfigId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html) client = [SecurityCenterClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.SecurityCenterClient.html).create()) {
          [NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.NotificationConfig.html) response =
              client.getNotificationConfig(String.format("%s/notificationConfigs/%s",
                  parentId, notificationConfigId));
    
          System.out.printf("Notification config: %s%n", response);
          return response;
        }
      }
    }

### Node.js

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // npm install @google-cloud/security-center/
    const {SecurityCenterClient} = require('[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)');
    
    const client = new [SecurityCenterClient](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)();
    
    const formattedConfigName = `organizations/${organizationId}/notificationConfigs/${configId}`;
    
    async function getNotificationConfg() {
      const [response] = await client.getNotificationConfig({
        name: formattedConfigName,
      });
      console.log('Notification config: ', response);
    }
    
    getNotificationConfg();

### PHP

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\SecurityCenter\V1\Client\SecurityCenterClient;
    use Google\Cloud\SecurityCenter\V1\GetNotificationConfigRequest;
    
    /**
     * @param string $organizationId        Your org ID
     * @param string $notificationConfigId  A unique identifier
     */
    function get_notification(string $organizationId, string $notificationConfigId): void
    {
        $securityCenterClient = new SecurityCenterClient();
        $notificationConfigName = $securityCenterClient::notificationConfigName(
            // You can also use 'projectId' or 'folderId' instead of the 'organizationId'.
            $organizationId,
            $notificationConfigId
        );
        $getNotificationConfigRequest = (new GetNotificationConfigRequest())
            ->setName($notificationConfigName);
    
        $response = $securityCenterClient->getNotificationConfig($getNotificationConfigRequest);
        printf('Notification config was retrieved: %s' . PHP_EOL, $response->getName());
    }

### Python

To authenticate to Security Command Center, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def get_notification_config(parent_id, notification_config_id):
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
    
        notification_config = client.get_notification_config(
            request={"name": notification_config_name}
        )
        print(f"Got notification config: {notification_config}")

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
    
    client = Google::Cloud::[SecurityCenter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center-v2/latest/Google-Cloud-SecurityCenter.html).[security_center](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security_center/latest/Google-Cloud-SecurityCenter.html)
    
    # You can also use a project or folder as a parent.
    config_path = client.notification_config_path organization:        org_id,
                                                  location:            location,
                                                  notification_config: config_id
    
    response = client.get_notification_config name: config_path
    puts "Notification config fetched: #{response}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=securitycommandcenter). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

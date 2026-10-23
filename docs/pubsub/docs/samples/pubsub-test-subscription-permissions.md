---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-test-subscription-permissions/
title: Test permissions for subscription \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:27.684093+00:00
---

# Test permissions for subscription  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-test-subscription-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Test permissions for subscription Stay organized with collections  Save and categorize content based on your preferences. 

Tests IAM permissions for a subscription.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Access control with Identity and Access Management](https://docs.cloud.google.com/pubsub/docs/access-control)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace iam = google::cloud::iam_v1;
    namespace pubsub = google::cloud::pubsub;
    [](std::string project_id, std::string subscription_id) {
      auto const subscription =
          pubsub::Subscription(std::move(project_id), std::move(subscription_id));
      auto client = iam::IAMPolicyClient(
          iam::MakeIAMPolicyConnection(pubsub::IAMPolicyOptions()));
      google::iam::v1::TestIamPermissionsRequest request;
      request.set_resource(subscription.FullName());
      request.add_permissions("pubsub.subscriptions.consume");
      request.add_permissions("pubsub.subscriptions.update");
    
      auto response = client.TestIamPermissions(request);
      if (!response) throw std::move(response).status();
      std::cout << "Allowed permissions for subscription "
                << subscription.FullName() << ":";
      for (auto const& permission : response->permissions()) {
        std::cout << " " << permission;
      }
      std::cout << "\n";
    }

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Iam.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.html);
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    
    public class TestSubscriptionIamPermissionsSample
    {
        public TestIamPermissionsResponse TestSubscriptionIamPermissionsResponse(string projectId, string subscriptionId)
        {
            [TestIamPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html) request = new [TestIamPermissionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsRequest.html)
            {
                ResourceAsResourceName = [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html).[FromProjectSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html#Google_Cloud_PubSub_V1_SubscriptionName_FromProjectSubscription_System_String_System_String_)(projectId, subscriptionId),
                Permissions = { "pubsub.subscriptions.get", "pubsub.subscriptions.update" }
            };
            [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) publisher = [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_Create)();
            [TestIamPermissionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.TestIamPermissionsResponse.html) response = publisher.[IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_IAMPolicyClient).TestIamPermissions(request);
            return response;
        }
    }

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/iam/apiv1/iampb"
    	"cloud.google.com/go/pubsub/v2"
    )
    
    func testPermissions(w io.Writer, projectID, subID string) ([]string, error) {
    	// projectID := "my-project-id"
    	// subID := "my-sub"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return nil, fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    
    	req := &iampb.[TestIamPermissionsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_TestIamPermissionsRequest){
    		Resource: fmt.Sprintf("projects/%s/subscriptions/%s", projectID, subID),
    		Permissions: []string{
    			"pubsub.subscriptions.consume",
    			"pubsub.subscriptions.update",
    		},
    	}
    	resp, err := client.SubscriptionAdminClient.[TestIamPermissions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_UnimplementedIAMPolicyServer_TestIamPermissions)(ctx, req)
    	if err != nil {
    		return nil, fmt.Errorf("error calling TestIamPermissions: %w", err)
    	}
    	for _, perm := range resp.Permissions {
    		fmt.Fprintf(w, "Allowed: %v\n", perm)
    	}
    	return resp.Permissions, nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.pubsub.v1.[SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html);
    import com.google.iam.v1.[TestIamPermissionsRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.TestIamPermissionsRequest.html);
    import com.google.iam.v1.[TestIamPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.TestIamPermissionsResponse.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import java.io.IOException;
    import java.util.LinkedList;
    import java.util.List;
    
    public class TestSubscriptionPermissionsExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String subscriptionId = "your-subscription-id";
    
        testSubscriptionPermissionsExample(projectId, subscriptionId);
      }
    
      public static void testSubscriptionPermissionsExample(String projectId, String subscriptionId)
          throws IOException {
        try ([SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) subscriptionAdminClient = [SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html).create()) {
          [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName =
              [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subscriptionId);
    
          List<String> permissions = new LinkedList<>();
          permissions.add("pubsub.subscriptions.consume");
          permissions.add("pubsub.subscriptions.update");
    
          [TestIamPermissionsRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.TestIamPermissionsRequest.html) testIamPermissionsRequest =
              [TestIamPermissionsRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.TestIamPermissionsRequest.html).newBuilder()
                  .setResource(subscriptionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html#com_google_pubsub_v1_ProjectSubscriptionName_toString__)())
                  .addAllPermissions(permissions)
                  .build();
    
          [TestIamPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.TestIamPermissionsResponse.html) testedPermissionsResponse =
              subscriptionAdminClient.testIamPermissions(testIamPermissionsRequest);
    
          System.out.println("Tested:\n" + testedPermissionsResponse);
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Prints the permissions of a subscription.
     *
     * @param string $projectId  The Google project ID.
     * @param string $subscriptionName  The Pub/Sub subscription name.
     */
    function test_subscription_permissions($projectId, $subscriptionName)
    {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
        $subscription = $pubsub->subscription($subscriptionName);
        $permissions = $subscription->iam()->testPermissions([
            'pubsub.subscriptions.consume',
            'pubsub.subscriptions.update'
        ]);
        foreach ($permissions as $permission) {
            printf('Permission: %s' . PHP_EOL, $permission);
        }
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # subscription_id = "your-subscription-id"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    subscription_admin = pubsub.[subscription_admin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
    permissions = ["pubsub.subscriptions.consume", "pubsub.subscriptions.update"]
    
    response = pubsub.[iam](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html).test_iam_permissions \
      resource: pubsub.subscription_path(subscription_id),
      permissions: permissions
    
    puts "Permission to consume" \
     if response.permissions.include? "pubsub.subscriptions.consume"
    puts "Permission to update" \
     if response.permissions.include? "pubsub.subscriptions.update"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-set-subscription-policy/
title: Set subscription policy \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:14.650255+00:00
---

# Set subscription policy  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-set-subscription-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Set subscription policy Stay organized with collections  Save and categorize content based on your preferences. 

Sets a subscription IAM policy.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Access control with Identity and Access Management](https://docs.cloud.google.com/pubsub/docs/access-control)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace iam = google::cloud::iam_v1;
    namespace pubsub = google::cloud::pubsub;
    using google::cloud::StatusCode;
    [](std::string project_id, std::string subscription_id) {
      auto const subscription =
          pubsub::Subscription(std::move(project_id), std::move(subscription_id));
      auto client = iam::IAMPolicyClient(
          iam::MakeIAMPolicyConnection(pubsub::IAMPolicyOptions()));
    
      // In production code, consider an OCC loop to handle concurrent changes
      // to the policy.
      google::iam::v1::GetIamPolicyRequest get;
      get.set_resource(subscription.FullName());
      auto policy = client.GetIamPolicy(get);
      if (!policy) throw std::move(policy).status();
    
      google::iam::v1::SetIamPolicyRequest set;
      set.set_resource(subscription.FullName());
      *set.mutable_policy() = *std::move(policy);
      // Add all users as viewers.
      auto& b0 = *set.mutable_policy()->add_bindings();
      b0.set_role("roles/pubsub.viewer");
      b0.add_members("domain:google.com");
      // Add a group as an editor.
      auto& b1 = *set.mutable_policy()->add_bindings();
      b1.set_role("roles/editor");
      b1.add_members("group:cloud-logs@google.com");
    
      auto response = client.SetIamPolicy(set);
      if (!response) throw std::move(response).status();
      std::cout << "Policy for subscription " << subscription.FullName() << ": "
                << response->DebugString() << "\n";
    }

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Iam.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.html);
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    
    public class SetSubscriptionIamPolicySample
    {
        public Policy SetSubscriptionIamPolicy(string projectId, string subscriptionId, string role, string member)
        {
            [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) publisher = [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_Create)();
            string roleToBeAddedToPolicy = $"roles/{role}";
    
            [Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html) policy = new [Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)
            {
                Bindings = {
                    new [Binding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Binding.html)
                    {
                        Role = roleToBeAddedToPolicy,
                        Members = { member }
                    }
                }
            };
            [SetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html) request = new [SetIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.SetIamPolicyRequest.html)
            {
                ResourceAsResourceName = [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html).[FromProjectSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html#Google_Cloud_PubSub_V1_SubscriptionName_FromProjectSubscription_System_String_System_String_)(projectId, subscriptionId),
                Policy = policy
            };
            [Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html) response = publisher.[IAMPolicyClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_IAMPolicyClient).SetIamPolicy(request);
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
    
    func addUsersToSubscription(w io.Writer, projectID, subID string) error {
    	// projectID := "my-project-id"
    	// subID := "my-sub"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	subName := fmt.Sprintf("projects/%s/subscriptions/%s", projectID, subID)
    	req := &iampb.[GetIamPolicyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_GetIamPolicyRequest){
    		Resource: subName,
    	}
    	policy, err := client.SubscriptionAdminClient.[GetIamPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_UnimplementedIAMPolicyServer_GetIamPolicy)(ctx, req)
    	if err != nil {
    		return fmt.Errorf("error calling GetIamPolicy: %w", err)
    	}
    	b := &iampb.[Binding](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_Binding){
    		Role: "roles/editor",
    		// Other valid prefixes are "serviceAccount:", "user:"
    		// See the documentation for more values.
    		Members: []string{"group:cloud-logs@google.com"},
    	}
    	policy.Bindings = append(policy.Bindings, b)
    
    	setRequest := &iampb.[SetIamPolicyRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_SetIamPolicyRequest){
    		Resource: subName,
    		Policy:   policy,
    	}
    	_, err = client.SubscriptionAdminClient.[SetIamPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv1/iampb.html#cloud_google_com_go_iam_apiv1_iampb_UnimplementedIAMPolicyServer_SetIamPolicy)(ctx, setRequest)
    	if err != nil {
    		return fmt.Errorf("error calling SetIamPolicy: %w", err)
    	}
    	fmt.Fprintln(w, "Added roles to subscription.")
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.pubsub.v1.[SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html);
    import com.google.iam.v1.[Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html);
    import com.google.iam.v1.[GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import com.google.iam.v1.[SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import java.io.IOException;
    
    public class SetSubscriptionPolicyExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String subscriptionId = "your-subscription-id";
    
        setSubscriptionPolicyExample(projectId, subscriptionId);
      }
    
      public static void setSubscriptionPolicyExample(String projectId, String subscriptionId)
          throws IOException {
        try ([SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) subscriptionAdminClient = [SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html).create()) {
          [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName =
              [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subscriptionId);
          [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) getIamPolicyRequest =
              [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html).newBuilder().setResource(subscriptionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html#com_google_pubsub_v1_ProjectSubscriptionName_toString__)()).build();
          [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) oldPolicy = subscriptionAdminClient.getIamPolicy(getIamPolicyRequest);
    
          // Create new role -> members binding
          [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding =
              [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html).newBuilder()
                  .setRole("roles/pubsub.editor")
                  .[addMembers](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_addMembers_java_lang_String_)("domain:google.com")
                  .build();
    
          // Add new binding to updated policy
          [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) updatedPolicy = [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html).newBuilder(oldPolicy).[addBindings](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_addBindings_com_google_iam_v1_Binding_)(binding).build();
    
          [SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html) setIamPolicyRequest =
              [SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html).newBuilder()
                  .setResource(subscriptionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html#com_google_pubsub_v1_ProjectSubscriptionName_toString__)())
                  .[setPolicy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.Builder.html#com_google_iam_v1_SetIamPolicyRequest_Builder_setPolicy_com_google_iam_v1_Policy_)(updatedPolicy)
                  .build();
          [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) newPolicy = subscriptionAdminClient.setIamPolicy(setIamPolicyRequest);
          System.out.println("New subscription policy: " + newPolicy);
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Adds a user to the policy for a Pub/Sub subscription.
     *
     * @param string $projectId  The Google project ID.
     * @param string $subscriptionName  The Pub/Sub subscription name.
     * @param string $userEmail  The user email to add to the policy.
     */
    function set_subscription_policy($projectId, $subscriptionName, $userEmail)
    {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
        $subscription = $pubsub->subscription($subscriptionName);
        $policy = $subscription->iam()->policy();
        $policy['bindings'][] = [
            'role' => 'roles/pubsub.subscriber',
            'members' => ['user:' . $userEmail]
        ];
        $subscription->iam()->setPolicy($policy);
    
        printf(
            'User %s added to policy for %s' . PHP_EOL,
            $userEmail,
            $subscriptionName
        );
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # subscription_id       = "your-subscription-id"
    # role                  = "roles/pubsub.subscriber"
    # service_account_email =
    # "serviceAccount:account_name@project_name.iam.gserviceaccount.com"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    
    bindings = Google::Iam::[V1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1.html)::Binding.[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html) \
      role: role,
      members: [service_account_email]
    
    pubsub.[iam](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html).set_iam_policy resource: pubsub.subscription_path(subscription_id),
                              policy: {
                                bindings: [bindings]
                              }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

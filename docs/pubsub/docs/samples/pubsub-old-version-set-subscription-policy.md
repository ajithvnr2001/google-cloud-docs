---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-set-subscription-policy/
title: v1 Set subscription policy (DEPRECATED) \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:56.742971+00:00
---

# v1 Set subscription policy (DEPRECATED)  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-old-version-set-subscription-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  v1 Set subscription policy (DEPRECATED) Stay organized with collections  Save and categorize content based on your preferences. 

(DEPRECATED) Set subscription policy

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/iam"
    	"cloud.google.com/go/pubsub"
    )
    
    // addUsers adds all IAM users to a subscription.
    func addUsers(projectID, subID string) error {
    	// projectID := "my-project-id"
    	// subID := "my-sub"
    	ctx := context.Background()
    	client, err := pubsub.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsub/latest/index.html#cloud_google_com_go_pubsub_Client_NewClient)(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	sub := client.Subscription(subID)
    	policy, err := sub.IAM().Policy(ctx)
    	if err != nil {
    		return fmt.Errorf("err getting IAM Policy: %w", err)
    	}
    	// Other valid prefixes are "serviceAccount:", "user:"
    	// See the documentation for more values.
    	policy.[Add](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/index.html#cloud_google_com_go_iam_Policy_Add)(iam.[AllUsers](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/index.html#cloud_google_com_go_iam_AllUsers_AllAuthenticatedUsers), iam.[Viewer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/index.html#cloud_google_com_go_iam_Owner_Editor_Viewer))
    	policy.[Add](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/index.html#cloud_google_com_go_iam_Policy_Add)("group:cloud-logs@google.com", iam.[Editor](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/index.html#cloud_google_com_go_iam_Owner_Editor_Viewer))
    	if err := sub.IAM().SetPolicy(ctx, policy); err != nil {
    		return fmt.Errorf("SetPolicy: %w", err)
    	}
    	// NOTE: It may be necessary to retry this operation if IAM policies are
    	// being modified concurrently. SetPolicy will return an error if the policy
    	// was modified since it was retrieved.
    	return nil
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

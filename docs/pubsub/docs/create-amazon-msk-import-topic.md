---
url: https://docs.cloud.google.com/pubsub/docs/create-amazon-msk-import-topic/
title: Create an Amazon Managed Streaming for Apache Kafka import topic \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:20:58.307088+00:00
---

# Create an Amazon Managed Streaming for Apache Kafka import topic  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/create-amazon-msk-import-topic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Create an Amazon Managed Streaming for Apache Kafka import topic Stay organized with collections  Save and categorize content based on your preferences. 

An Amazon Managed Streaming for Apache Kafka (Amazon MSK) import topic lets you continuously ingest data from [Amazon MSK](https://aws.amazon.com/msk/) as an external source and into Pub/Sub. Then you can stream the data into any of the destinations that Pub/Sub supports.

**Note:** Only [Amazon MSK provisioned clusters](https://docs.aws.amazon.com/msk/latest/developerguide/msk-provisioned.html) can be imported into Pub/Sub. Your clusters also must be public. Clusters behind private VPCs aren't supported.

This document shows you how to create and manage Amazon MSK import topics. To create a standard topic, see [Create a standard topic](https://docs.cloud.google.com/pubsub/docs/create-topic).

For more information about import topics, see [About import topics](https://docs.cloud.google.com/pubsub/docs/publish-message-overview#import-topic-overview).

## Before you begin

  * Know more about the [Pub/Sub publish process](https://docs.cloud.google.com/pubsub/docs/publish-message-overview).

  * Configure the required roles and permissions to manage Amazon MSK import topics including the following:

    * Add the Pub/Sub publisher role to the Pub/Sub service account

    * Add the Pub/Sub service agent role to the Pub/Sub service account, if not already granted.

    * Add the service account user role to the service account

  * Set up workload identity federation so that Google Cloud can access the external streaming service.




### Required roles and permissions

To get the permissions that you need to create and manage Amazon MSK import topics, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on your topic or project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create and manage Amazon MSK import topics. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage Amazon MSK import topics:

  * Create an import topic: pubsub.topics.create 
  * Delete an import topic: pubsub.topics.delete 
  * Get an import topic: pubsub.topics.get 
  * List an import topic: pubsub.topics.list 
  * Publish to an import topic: pubsub.topics.publish and pubsub.serviceAgent 
  * Update an import topic: pubsub.topics.update 
  * Get the IAM policy for an import topic: pubsub.topics.getIamPolicy 
  * Configure the [IAM policy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy) for an import topic: `pubsub.topics.setIamPolicy`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You can configure access control at the project level and the individual resource level.

## Set up federated identity to access Amazon MSK

Workload Identity Federation lets Google Cloud services access workloads running outside of Google Cloud. With identity federation, you don't need to maintain or pass credentials to Google Cloud to access your resources in other clouds. Instead, you can use the identities of the workloads themselves to authenticate to Google Cloud and access resources.

### Create a service account in Google Cloud

This is an optional step. If you already have a service account, you can use it in this procedure instead of creating a new service account. If you are using an existing service account, go to Record the service account unique ID for the next step.

For Amazon MSK import topics, Pub/Sub uses the service account as the identity to access resources from AWS.

For more information about creating a service account, including prerequisites, required roles and permissions, and naming guidelines, see [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create). After you create a service account, you might need to wait for 60 seconds or more before you use the service account. This behavior occurs because read operations are eventually consistent; it can take time for the new service account to become visible.

### Record the service account unique ID

You need a service account unique ID to set up a role in the AWS console.

  1. In the Google Cloud console, go to the **Service account** details page.

[Go to service account](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click the service account that you just created or the one that you are planning to use.

  3. From the **Service account details** page, record the Unique ID number.

You need the ID as part of the workflow to set up a role in the AWS console.




### Add the service account token creator role to the Pub/Sub service account

**Note:** Pub/Sub creates and maintains a service account for each project. The service account has the following format: `service-{PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com`. Perform this procedure only if the Pub/Sub service account does not have the Pub/Sub Service Agent role (`roles/pubsub.serviceAgent`).

The **Service account token creator role** (`roles/iam.serviceAccountTokenCreator`) lets principals [create short-lived credentials](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct) for a service account. These tokens or credentials are used to impersonate the service account.

For more information about service account impersonation, see [Service account impersonation](https://docs.cloud.google.com/iam/docs/service-account-impersonation).

You can also add the **Pub/Sub publisher role** (`roles/pubsub.publisher`) during this procedure. For more information about the role and why you are adding it, see Add the Pub/Sub publisher role to the Pub/Sub service account.

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click the **Include Google-provided role grants** checkbox.

  3. Look for the service account that has the format `service-{PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com`.

  4. For this service account, click the **Edit Principal** button.

  5. If required, click **Add another role**.

  6. Search and click the **Service account token creator role** (`roles/iam.serviceAccountTokenCreator`).

  7. Click **Save**.




### Create a policy in AWS

You need a policy in AWS to let Pub/Sub authenticate to AWS so that Pub/Sub can ingest data from Amazon MSK.

  * For more methods and information about how to create a policy in AWS, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html).



To create a policy in AWS, perform the following steps:

  1. Sign in to the AWS Management Console and open the [IAM console](https://console.aws.amazon.com/iam/).

  2. In the navigation pane of the console for **IAM** , click **Access Management** > **Policies**.

  3. Click **Create policy**. 

  4. For **Click a service** , click **MSK**.

  5. For **Action allowed,** click **Read** > [**GetBootstrapBrokers**](https://docs.aws.amazon.com//msk/1.0/apireference/clusters-clusterarn-bootstrap-brokers.html).

This action grants permission to get the bootstrap brokers that Pub/Sub uses to connect to the MSK cluster.

  6. Click **Add more permissions**.

  7. For **Select a service** , click **Apache Kafka APIs for MSK**.

  8. For **Action allowed** , select the following:

     * **List** > [**DescribeTopic**](https://docs.aws.amazon.com/service-authorization/latest/reference/list_apachekafkaapisforamazonmskclusters.html)

This action grants permission to allow the Pub/Sub ingestion topic to get details about the Amazon MSK Kafka topic.

     * **Read** > [**ReadData**](https://docs.aws.amazon.com/service-authorization/latest/reference/list_apachekafkaapisforamazonmskclusters.html)

This action grants permission to read data from the Amazon MSK Kafka topic.

     * **Write** > [**Connect**](https://docs.aws.amazon.com/service-authorization/latest/reference/list_apachekafkaapisforamazonmskclusters.html)

This action grants permission to connect and authenticate to the Amazon MSK Kafka cluster.

  9. For **Resources** , specify the [cluster ARN](https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn.html) (if you want to restrict the policy to specific clusters, which is recommended). 

  10. Click **Add more permissions**.

  11. For **Select a service** , click **STS**.

  12. For **Action allowed** , click **Write** > **[AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html)**.

This action grants permission to obtain a set of temporary security credentials for Pub/Sub to authenticate to Amazon MSK by using identity federation.

  13. Click **Next**.

  14. Enter a policy name and description.

  15. Click **Create policy**.




### Create a role in AWS using a custom trust policy

You must create a role in AWS so that Pub/Sub can authenticate to AWS to ingest data from Amazon MSK.

  1. Sign in to the AWS Management Console and open the [IAM console](https://console.aws.amazon.com/iam/).

  2. In the navigation pane of the console for **IAM** , click **Roles**.

  3. Click **Create role**.

  4. For **Select trusted entity** , click **Custom trust policy**. 

  5. In the **Custom trust policy** section, enter or paste the following:
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
              "Effect": "Allow",
              "Principal": {
                 "Federated": "accounts.google.com"
              },
              "Action": "sts:AssumeRoleWithWebIdentity",
              "Condition": {
                  "StringEquals": {
                    "accounts.google.com:sub": "<SERVICE_ACCOUNT_UNIQUE_ID>"
                  }
               }
             }
           ]
         }
         

Replace `<SERVICE_ACCOUNT_UNIQUE_ID>` with the unique ID of the service account that you recorded in Record the service account unique ID. 

  6. Click **Next**.

  7. For **Add permissions** , search and click the custom policy that you just created.

  8. Click **Next**.

  9. Enter a role name and description.

  10. Click **Create role**.




## Add the Pub/Sub publisher role to the Pub/Sub principal

To enable publishing, you must assign a publisher role to the Pub/Sub service account so that Pub/Sub is able to publish to the Amazon MSK import topic.

## Add the Pub/Sub service agent role to the Pub/Sub service account

**Note:** The Pub/Sub service agent role is granted by default for all projects after April 9, 2021. If your project has been created after this date and the Pub/Sub service agent role has not been removed, your Pub/Sub service account will already have this role.

To allow Pub/Sub to use your import topic project's publish quota, the Pub/Sub service agent requires the [`serviceusage.services.use`](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.services.use) permission on your import topic's project.

To provide this permission, we recommend you add the Pub/Sub service agent role to the Pub/Sub service account.

If the Pub/Sub service account does not have the Pub/Sub service agent role, it can be granted as follows:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click the **Include Google-provided role grants** checkbox.

  3. Look for the service account that has the format `service-{PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com`.

  4. For this service account, click the **Edit principal** button.

  5. If required, click **Add another role**.

  6. Search and click the **Pub/Sub Service Agent role** (`roles/pubsub.serviceAgent`).

  7. Click **Save**.




### Enable publishing from all topics

Use this method if you have not created any Amazon MSK import topics.

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click the **Include Google-provided role grants** checkbox.

  3. Look for the service account that has the format `service-{PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com`.

  4. For this service account, click the **Edit principal** button.

  5. If required, click **Add another role**.

  6. Search and click the **Pub/Sub publisher role** (`roles/pubsub.publisher`).

  7. Click **Save**.




### Enable publishing from a single topic

Use this method only if the Amazon MSK import topic already exists.

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [`gcloud pubsub topics add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/add-iam-policy-binding) command:
         
         gcloud pubsub topics add-iam-policy-binding TOPIC_ID \
            --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com" \
            --role="roles/pubsub.publisher"

Replace the following:

     * `TOPIC_ID`: the topic ID of the Amazon MSK import topic.

     * `PROJECT_NUMBER`: the project number. To view the project number, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).




## Add the service account user role to the service account

The **Service Account User role** (`roles/iam.serviceAccountUser`) includes the permission `iam.serviceAccounts.actAs` that lets a principal attach a service account to the Amazon MSK import topic's ingestion settings and use that service account for federated identity.

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. For the principal that's issuing the create or update topic calls, click the **Edit principal** button.

  3. If required, click **Add another role**.

  4. Search and click the **Service account user role** (`roles/iam.serviceAccountUser`).

  5. Click **Save**.




## Use Amazon MSK import topics

You can create a new import topic or edit an existing topic.

### Considerations

**Caution:** If you already have data in Amazon MSK, first [create a standard topic and a default subscription](https://docs.cloud.google.com/pubsub/docs/create-topic#create_a_topic_2) without enabling the ingestion settings. Then, [convert the topic to an import topic](https://docs.cloud.google.com/pubsub/docs/change-topic-type#convert-standard-to-import). This method ensures that all messages are received by the subscription.

  * Creating the topic and subscription separately, even if done in rapid succession, can lead to data loss. There's a short window where the topic exists without a subscription. If any data is sent to the topic during this time, it is lost. By creating the topic first, creating the subscription, and then converting the topic to an import topic, you guarantee that no messages are missed during the import process.

  * If you need to re-create the Kafka topic of an existing import topic with the same name, you can't _just_ delete the Kafka topic and re-create it. This action can invalidate Pub/Sub's offset management, which can lead to data loss. To mitigate this, follow these steps:

    * Delete the Pub/Sub import topic.
    * Delete the Kafka topic.
    * Create the Kafka topic.
    * Create the Pub/Sub import topic.
  * Data from an Amazon MSK Kafka topic is always read from the [earliest offset](https://kafka.apache.org/documentation/#consumerconfigs_auto.offset.reset).




### Create Amazon MSK import topics

To know more about properties associated with a topic, see [Properties of a topic](https://docs.cloud.google.com/pubsub/docs/create-topic#properties_of_a_topic).

Ensure that you have completed the following procedures:

  * Set up federated identity to access Amazon MSK

  * Add the Pub/Sub publisher role to the Pub/Sub service account

  * Add the service account user role to the service account




To create an Amazon MSK import topic, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic/list)

  2. Click **Create topic**.

  3. In the **Topic ID** field, enter an ID for your Amazon MSK import topic. For more information about naming topics, see the [naming guidelines](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names).

  4. Select **Add a default subscription**.

  5. Select **Enable ingestion**.

  6. For ingestion source, select **Amazon MSK**.

  7. Enter the following details:

     * **Cluster ARN** : The ARN of the Amazon MSK that you are ingesting into Pub/Sub. The ARN format is as follows: `arn:aws:kafka:${Region}:${Account}:cluster/${ClusterName}/${ClusterId}`.
     * **Topic** : The name of the Amazon MSK Kafka topic that you are ingesting into Pub/Sub.
     * **AWS Role ARN** : The ARN of the AWS role. The ARN format of the role is as follows: `arn:aws:iam::${Account}:role/${RoleName}`.
     * **Service account** : The service account that you created in Create a service account in Google Cloud.
  8. Click **Create topic**.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [`gcloud pubsub topics create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/create) command:
         
         gcloud pubsub topics create TOPIC_ID \
               --aws-msk-ingestion-cluster-arn MSK_CLUSTER_ARN \
               --aws-msk-ingestion-topic MSK_TOPIC \
               --aws-msk-ingestion-aws-role-arn MSK_ROLE_ARN \
               --aws-msk-ingestion-service-account PUBSUB_SERVICE_ACCOUNT
         

Replace the following:

     * `TOPIC_ID`: the name or ID of your Pub/Sub topic.
     * `MSK_CLUSTER_ARN`: the ARN for the Amazon MSK cluster that you are ingesting into Pub/Sub. The ARN format is as follows: `arn:aws:kafka:${Region}:${Account}:cluster/${ClusterName}/${ClusterId}`.
     * `MSK_TOPIC`: the name of the Amazon MSK Kafka topic that you are ingesting into Pub/Sub.
     * `MSK_ROLE_ARN`: the ARN of the AWS role. The ARN format of the role is as follows: `arn:aws:iam::${Account}:role/${RoleName}`.
     * `PUBSUB_SERVICE_ACCOUNT`: the service account that you created in Create a service account in Google Cloud.



### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    [](pubsub_admin::TopicAdminClient client, std::string project_id,
       std::string topic_id, std::string const& cluster_arn,
       std::string const& msk_topic, std::string const& aws_role_arn,
       std::string const& gcp_service_account) {
      google::pubsub::v1::Topic request;
      request.set_name(
          pubsub::Topic(std::move(project_id), std::move(topic_id)).FullName());
      auto* aws_msk =
          request.mutable_ingestion_data_source_settings()->mutable_aws_msk();
      aws_msk->set_cluster_arn(cluster_arn);
      aws_msk->set_topic(msk_topic);
      aws_msk->set_aws_role_arn(aws_role_arn);
      aws_msk->set_gcp_service_account(gcp_service_account);
    
      auto topic = client.CreateTopic(request);
      // Note that kAlreadyExists is a possible error when the library retries.
      if (topic.status().code() == google::cloud::StatusCode::kAlreadyExists) {
        std::cout << "The topic already exists\n";
        return;
      }
      if (!topic) throw std::move(topic).status();
    
      std::cout << "The topic was successfully created: " << topic->DebugString()
                << "\n";
    }

### Go

The following sample uses the major version of the Go Pub/Sub client library (v2). If you are still using the v1 library, see [the migration guide to v2](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md). To see a list of v1 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=golang&text=deprecated).

Before trying this sample, follow the Go setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/pubsub/v2).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsub/v2"
    	"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb"
    )
    
    func createTopicWithAWSMSKIngestion(w io.Writer, projectID, topicID, clusterARN, mskTopic, awsRoleARN, gcpSA string) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    
    	// // AWS MSK ingestion settings.
    	// clusterARN := "cluster-arn"
    	// mskTopic := "msk-topic"
    	// awsRoleARN := "aws-role-arn"
    	// gcpSA := "gcp-service-account"
    
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	topicpb := &pubsubpb.Topic{
    		Name: fmt.Sprintf("projects/%s/topics/%s", projectID, topicID),
    		IngestionDataSourceSettings: &pubsubpb.IngestionDataSourceSettings{
    			Source: &pubsubpb.IngestionDataSourceSettings_AwsMsk_{
    				AwsMsk: &pubsubpb.IngestionDataSourceSettings_AwsMsk{
    					ClusterArn:        clusterARN,
    					Topic:             mskTopic,
    					AwsRoleArn:        awsRoleARN,
    					GcpServiceAccount: gcpSA,
    				},
    			},
    		},
    	}
    	topic, err := client.TopicAdminClient.CreateTopic(ctx, topicpb)
    	if err != nil {
    		return fmt.Errorf("CreateTopic: %w", err)
    	}
    	fmt.Fprintf(w, "Created topic with AWS MSK ingestion settings: %v\n", topic)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.cloud.pubsub.v1.[TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html);
    import com.google.pubsub.v1.[IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html);
    import com.google.pubsub.v1.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import java.io.IOException;
    
    public class CreateTopicWithAwsMskIngestionExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-topic-id";
        // AWS MSK ingestion settings.
        String clusterArn = "cluster-arn";
        String mskTopic = "msk-topic";
        String awsRoleArn = "aws-role-arn";
        String gcpServiceAccount = "gcp-service-account";
    
        createTopicWithAwsMskIngestionExample(
            projectId, topicId, clusterArn, mskTopic, awsRoleArn, gcpServiceAccount);
      }
    
      public static void createTopicWithAwsMskIngestionExample(
          String projectId,
          String topicId,
          String clusterArn,
          String mskTopic,
          String awsRoleArn,
          String gcpServiceAccount)
          throws IOException {
        try ([TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html).create()) {
          [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
    
          [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).[AwsMsk](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.AwsMsk.html) awsMsk =
              [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).AwsMsk.newBuilder()
                  .setClusterArn(clusterArn)
                  .setTopic(mskTopic)
                  .setAwsRoleArn(awsRoleArn)
                  .setGcpServiceAccount(gcpServiceAccount)
                  .build();
          [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html) ingestionDataSourceSettings =
              [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).newBuilder().[setAwsMsk](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.Builder.html#com_google_pubsub_v1_IngestionDataSourceSettings_Builder_setAwsMsk_com_google_pubsub_v1_IngestionDataSourceSettings_AwsMsk_)(awsMsk).build();
    
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html) topic =
              topicAdminClient.createTopic(
                  [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html).newBuilder()
                      .setName(topicName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html#com_google_pubsub_v1_TopicName_toString__)())
                      .[setIngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.Builder.html#com_google_pubsub_v1_Topic_Builder_setIngestionDataSourceSettings_com_google_pubsub_v1_IngestionDataSourceSettings_)(ingestionDataSourceSettings)
                      .build());
    
          System.out.println("Created topic with AWS MSK ingestion settings: " + topic.getAllFields());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    // const clusterArn = 'arn:aws:kafka:...';
    // const mskTopic = 'YOUR_MSK_TOPIC';
    // const roleArn = 'arn:aws:iam:...';
    // const gcpServiceAccount = 'ingestion-account@...';
    
    // Imports the Google Cloud client library
    const {PubSub} = require('@google-cloud/pubsub');
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function createTopicWithAwsMskIngestion(
      topicNameOrId,
      clusterArn,
      mskTopic,
      awsRoleArn,
      gcpServiceAccount,
    ) {
      // Creates a new topic with AWS MSK ingestion.
      await pubSubClient.createTopic({
        name: topicNameOrId,
        ingestionDataSourceSettings: {
          awsMsk: {
            clusterArn,
            topic: mskTopic,
            awsRoleArn,
            gcpServiceAccount,
          },
        },
      });
      console.log(`Topic ${topicNameOrId} created with AWS MSK ingestion.`);
    }

### Node.ts

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    // const clusterArn = 'arn:aws:kafka:...';
    // const mskTopic = 'YOUR_MSK_TOPIC';
    // const roleArn = 'arn:aws:iam:...';
    // const gcpServiceAccount = 'ingestion-account@...';
    
    // Imports the Google Cloud client library
    import {PubSub} from '@google-cloud/pubsub';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function createTopicWithAwsMskIngestion(
      topicNameOrId: string,
      clusterArn: string,
      mskTopic: string,
      awsRoleArn: string,
      gcpServiceAccount: string,
    ) {
      // Creates a new topic with AWS MSK ingestion.
      await pubSubClient.createTopic({
        name: topicNameOrId,
        ingestionDataSourceSettings: {
          awsMsk: {
            clusterArn,
            topic: mskTopic,
            awsRoleArn,
            gcpServiceAccount,
          },
        },
      });
      console.log(`Topic ${topicNameOrId} created with AWS MSK ingestion.`);
    }

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from google.cloud import pubsub_v1
    from google.pubsub_v1.types import [Topic](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.Topic.html)
    from google.pubsub_v1.types import [IngestionDataSourceSettings](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.IngestionDataSourceSettings.html)
    
    # TODO(developer)
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"
    # cluster_arn = "your-cluster-arn"
    # msk_topic = "your-msk-topic"
    # aws_role_arn = "your-aws-role-arn"
    # gcp_service_account = "your-gcp-service-account"
    
    publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
    topic_path = publisher.topic_path(project_id, topic_id)
    
    request = Topic(
        name=topic_path,
        ingestion_data_source_settings=IngestionDataSourceSettings(
            aws_msk=[IngestionDataSourceSettings](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.IngestionDataSourceSettings.html).[AwsMsk](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.IngestionDataSourceSettings.AwsMsk.html)(
                cluster_arn=cluster_arn,
                topic=msk_topic,
                aws_role_arn=aws_role_arn,
                gcp_service_account=gcp_service_account,
            )
        ),
    )
    
    topic = publisher.create_topic(request=request)
    
    print(f"Created topic: {topic.name} with AWS MSK Ingestion Settings")

For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html#arn-syntax-kinesis-streams) and [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html).

If you run into issues, see [Troubleshooting an Amazon MSK import topic](https://docs.cloud.google.com/pubsub/docs/amazon-msk-import-topic-troubleshooting).

### Edit Amazon MSK import topics

To edit the ingestion data source settings of an Amazon MSK import topic, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic/list)

  2. Click the Amazon MSK import topic.

  3. In the topic details page, click **Edit**.

  4. Update the fields that you want to change.

  5. Click **Update**.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the [`gcloud pubsub topics update`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/update) command with all the flags mentioned in the following sample:
         
         gcloud pubsub topics update TOPIC_ID \
             --aws-msk-ingestion-cluster-arn MSK_CLUSTER_ARN \
             --aws-msk-ingestion-topic MSK_TOPIC \
             --aws-msk-ingestion-aws-role-arn MSK_ROLE_ARN \
             --aws-msk-ingestion-service-account PUBSUB_SERVICE_ACCOUNT

Replace the following:

     * TOPIC_ID: the name or ID of your Pub/Sub topic.
     * MSK_CLUSTER_ARN: the ARN for the Amazon MSK cluster that you are ingesting into Pub/Sub. The ARN format is as follows: `arn:aws:kafka:${Region}:${Account}:cluster/${ClusterName}/${ClusterId}`.
     * MSK_TOPIC: the name of the Amazon MSK Kafka topic that you are ingesting into Pub/Sub.
     * MSK_ROLE_ARN: the ARN of the AWS role. The ARN format of the role is as follows: `arn:aws:iam::${Account}:role/${RoleName}`.
     * PUBSUB_SERVICE_ACCOUNT: the service account that you created in Create a service account in Google Cloud.




## Quotas and limits

The publisher throughput for import topics is bound by the publish quota of the topic. For more information, see [Pub/Sub quotas and limits](https://docs.cloud.google.com/pubsub/quotas).

## What's next

  * [Monitor an import topic](https://docs.cloud.google.com/pubsub/docs/monitor-topic#metrics-monitor-topic).

  * Choose the [type of subscription](https://docs.cloud.google.com/pubsub/docs/subscriber) for your topic.

  * Learn how to [publish a message to a topic](https://docs.cloud.google.com/pubsub/docs/publisher).

  * Create or modify a topic with [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics), [REST APIs](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics), or [Client libraries](https://docs.cloud.google.com/pubsub/docs/reference/libraries).

  * [Troubleshoot an Amazon MSK import topic](https://docs.cloud.google.com/pubsub/docs/amazon-msk-import-topic-troubleshooting)




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

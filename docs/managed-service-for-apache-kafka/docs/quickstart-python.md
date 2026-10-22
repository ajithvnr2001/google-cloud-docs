---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart-python/
title: Develop a Python producer \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:36.751551+00:00
---

# Develop a Python producer  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart-python/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Develop a Python producer application

Learn how to develop a Python producer application that authenticates with a Managed Service for Apache Kafka cluster by using [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) (ADC). ADC lets applications running on Google Cloud automatically find and use the right credentials for authenticating to Google Cloud services.

## Before you begin

Before you start this tutorial, create a new Managed Service for Apache Kafka cluster. If you already have a cluster, you can skip this step.

### How to create a cluster

### Console

  1. Go to the **Managed Service for Apache Kafka** > **Clusters** page. 

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

  2. Click add_box **Create**.
  3. In the **Cluster name** box, enter a name for the cluster.
  4. In the **Region** list, select a location for the cluster.
  5. For **Network configuration** , configure the subnet where the cluster is accessible: 
     1. For **Project** , select your project.
     2. For **Network** , select the VPC network.
     3. For **Subnet** , select the subnet.
     4. Click **Done**.
  6. Click **Create**.



After you click **Create** , the cluster state is `Creating`. When the cluster is ready, the state is `Active`. 

### gcloud

To create a Kafka cluster, run the [`managed-kafka clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/create) command. 
    
    
    gcloud managed-kafka clusters create KAFKA_CLUSTER \
    --location=REGION \
    --cpu=3 \
    --memory=3GiB \
    --subnets=projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME \
    --async

Replace the following:

  * `KAFKA_CLUSTER`: a name for the Kafka cluster
  * `REGION`: the location of the cluster
  * `PROJECT_ID`: your project ID
  * `SUBNET_NAME`: the subnet where you want to create the cluster, for example `default`



For information about supported locations, see [ Managed Service for Apache Kafka locations](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/locations). 

The command runs asynchronously and returns an operation ID:
    
    
    Check operation [projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID] for status.

To track the progress of the create operation, use the [`gcloud managed-kafka operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/operations/describe) command: 
    
    
    gcloud managed-kafka operations describe OPERATION_ID \
      --location=REGION

When the cluster is ready, the output from this command includes the entry `state: ACTIVE`. For more information, see [ Monitor the cluster creation operation](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster#monitor_cluster). 

### Required roles

To get the permissions that you need to create and configure a client VM, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Role Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.roleViewer) (`roles/iam.roleViewer`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up a client VM

Create a Linux virtual machine (VM) instance in Compute Engine that can access the Kafka cluster. When you configure the VM, set the following options:

  * **Region**. Create the VM in the same region as your Kafka cluster.

  * **Subnet**. Create the VM in the same VPC network as the subnet that you used in your Kafka cluster configuration. For more information, see [View a cluster's subnets](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-subnets).

  * **Access scopes**. Assign the `https://www.googleapis.com/auth/cloud-platform` [access scope](https://docs.cloud.google.com/compute/docs/access/service-accounts#accesscopesiam) to the VM. This scope authorizes the VM to send requests to the Managed Kafka API.




The following steps show how to set these options.

### Console

  1. In the Google Cloud console, go to the **Create an instance** page.

[Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Machine configuration** pane, do the following:

     1. In the **Name** field, specify a name for your instance. For more information, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).

     2. In the **Region** list, select the same region as your Kafka cluster.

     3. In the **Zone** list, select a zone.

  3. In the navigation menu, click **Networking**. In the **Networking** pane that appears, do the following:

     1. Go to the **Network interfaces** section.

     2. To expand the default network interface, click the expand_more arrow.

     3. In the **Network** field, choose the VPC network.

     4. In the **Subnetwork** list, select the subnet.

     5. Click **Done**.

  4. In the navigation menu, click **Security**. In the **Security** pane that appears, do the following:

     1. For **Access scopes** , select **Set access for each API**.

     2. In the list of access scopes, find the **Cloud Platform** drop-down list and select **Enabled.**

  5. Click **Create** to create the VM.




###  gcloud 

To create the VM instance, use the [`gcloud compute instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) command.
    
    
    gcloud compute instances create VM_NAME \
      --scopes=https://www.googleapis.com/auth/cloud-platform \
      --subnet=projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET \
      --zone=ZONE
    

Replace the following:

  * VM_NAME: the name of the VM
  * PROJECT_ID: your project ID
  * REGION: the region where you created the Kafka cluster, for example `us-central1`
  * SUBNET: a subnet in the same VPC network as the subnet that you used in the cluster configuration
  * ZONE: a zone in the region where you created the cluster, for example `us-central1-c`



For more information about creating a VM, see [Create a VM instance in a specific subnet](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#create_a_VM_instance_in_a_specific_subnet).

### Grant IAM roles

Grant the following Identity and Access Management (IAM) roles to the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account):

  * **Managed Kafka Client** (`roles/managedkafka.client`)
  * **Service Account Token Creator** (`roles/iam.serviceAccountTokenCreator`)
  * **Service Account OpenID Token Creator** (`roles/iam.serviceAccountOpenIdTokenCreator`)




### Console

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Find the row for **Compute Engine default service account** and click mode_edit  **Edit principal**.

  3. Click **Add another role** and select the role **Managed Kafka Client**. Repeat this step for the **Service Account Token Creator** and **Service Account OpenID Token Creator** roles.

  4. Click **Save**.




###  gcloud 

To grant IAM roles, use the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command.
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
      --role=roles/managedkafka.client
    
    gcloud projects add-iam-policy-binding PROJECT_ID\
      --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
      --role=roles/iam.serviceAccountTokenCreator
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
      --role=roles/iam.serviceAccountOpenIdTokenCreator
    

Replace the following:

  * PROJECT_ID: your project ID

  * PROJECT_NUMBER: your project number




To get the project number, run the [`gcloud projects describe`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe) command:
    
    
    gcloud projects describe PROJECT_ID
    

For more information, see [Find the project name, number, and ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

### Connect to the VM

Use SSH to connect to the VM instance.

###  Console 

  1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the list of VM instances, find the VM name and click **SSH**.




###  gcloud 

To connect to the VM, use the [`gcloud compute ssh`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh) command.
    
    
    gcloud compute ssh VM_NAME \
      --project=PROJECT_ID \
      --zone=ZONE
    

Replace the following:

  * VM_NAME: the name of the VM
  * PROJECT_ID: your project ID
  * ZONE: the zone where you created the VM



Additional configuration might be required for first time SSH usage. For more information, see [About SSH connections](https://docs.cloud.google.com/compute/docs/instances/ssh).

## Create a Python producer application

From your SSH session, run the following commands to create a producer application.

  1. Install pip, a Python package manager and the virtual environment manager:
         
         sudo apt install python3-pip -y
         sudo apt install python3-venv -y
         

  2. Create a new virtual environment (venv) and activate it:
         
         python3 -m venv kafka
         source kafka/bin/activate
         

  3. Install the `confluent-kafka` client and other dependencies:
         
         pip install confluent-kafka google-auth urllib3 packaging requests
         

  4. Copy the following producer client code into a file called `producer.py`
         
         import confluent_kafka
         import argparse
         from tokenprovider import TokenProvider
         
         parser = argparse.ArgumentParser()
         parser.add_argument('-b', '--bootstrap-servers', dest='bootstrap', type=str, required=True)
         parser.add_argument('-t', '--topic-name', dest='topic_name', type=str, default='example-topic', required=False)
         parser.add_argument('-n', '--num_messages', dest='num_messages', type=int, default=1, required=False)
         args = parser.parse_args()
         
         token_provider = TokenProvider()
         
         config = {
             'bootstrap.servers': args.bootstrap,
             'security.protocol': 'SASL_SSL',
             'sasl.mechanisms': 'OAUTHBEARER',
             'oauth_cb': token_provider.get_token,
         }
         
         producer = confluent_kafka.Producer(config)
         
         def callback(error, message):
             if error is not None:
                 print(error)
                 return
             print("Delivered a message to {}[{}]".format(message.topic(), message.partition()))
         
         for i in range(args.num_messages):
         
           message = f"{i} hello world!".encode('utf-8')
           producer.produce(args.topic_name, message, callback=callback)
         
         producer.flush()
         

  5. You now need an implementation of the OAuth token provider. Save the following code in a file called `tokenprovider.py`:
         
         import base64
         import datetime
         import http.server
         import json
         import google.auth
         from google.auth.transport.urllib3 import Request
         import urllib3
         import time
         
         def encode(source):
           """Safe base64 encoding."""
           return base64.urlsafe_b64encode(source.encode('utf-8')).decode('utf-8').rstrip('=')
         
         class TokenProvider(object):
           """
           Provides OAuth tokens from Google Cloud Application Default credentials.
           """
           HEADER = json.dumps({'typ':'JWT', 'alg':'GOOG_OAUTH2_TOKEN'})
         
           def __init__(self, **config):
             self.credentials, _project = google.auth.default()
             self.http_client = urllib3.PoolManager()
         
           def get_credentials(self):
             if not self.credentials.valid:
               self.credentials.refresh(Request(self.http_client))
             return self.credentials
         
           def get_jwt(self, creds):
             token_data = dict(
               exp=creds.expiry.replace(tzinfo=datetime.timezone.utc).timestamp(),
               iat=datetime.datetime.now(datetime.timezone.utc).timestamp(),
               iss='Google',
               sub=creds.service_account_email
             )
             return json.dumps(token_data)
         
           def get_token(self, args):
             creds = self.get_credentials()
             token = '.'.join([
               encode(self.HEADER),
               encode(self.get_jwt(creds)),
               encode(creds.token)
             ])
         
             # compute expiry time
             expiry_utc = creds.expiry.replace(tzinfo=datetime.timezone.utc)
             now_utc = datetime.datetime.now(datetime.timezone.utc)
             expiry_seconds = (expiry_utc - now_utc).total_seconds()
         
             return token, time.time() + expiry_seconds
         

  6. Look up the bootstrap address of your Kafka cluster following [View a cluster's bootstrap address](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-bootstrap-address)

  7. You are now ready to run the application:
         
         python producer.py -b BOOTSTRAP
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Console

  1. Delete the VM instance.

     1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. Select the VM and click **Delete**.

  2. Delete the Kafka cluster.

     1. Go to the **Managed Service for Apache Kafka** > **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

     2. Select the Kafka cluster and click **Delete**.




###  gcloud 

  1. To delete the VM, use the [`gcloud compute instances delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/delete) command.
         
         gcloud compute instances delete VM_NAME --zone=ZONE
         

  2. To delete the Kafka cluster, use the [`gcloud managed-kafka clusters delete`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/delete) command.
         
         gcloud managed-kafka clusters delete CLUSTER_ID \
           --location=REGION --async
         




## What's next

  * [Overview of Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview).

  * [Authenticate Kafka clients with Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication-kafka).

  * [Authentication tools and documentation Managed Service for Apache Kafka](https://github.com/googleapis/managedkafka/blob/main/README.md)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

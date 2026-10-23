---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart-avro/
title: Quickstart: Produce Avro messages with the schema registry \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:09.287795+00:00
---

# Quickstart: Produce Avro messages with the schema registry  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/quickstart-avro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Produce Avro messages with the schema registry

Learn how to develop a Java producer application that uses the [schema registry](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/schema-registry-overview) ([Preview](https://cloud.google.com/products#product-launch-stages)) to produce Apache Avro messages. The application writes the messages to a Managed Service for Apache Kafka cluster.

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
  * **Schema Registry Admin** (`roles/managedkafka.schemaRegistryAdmin`)
  * **Service Account Token Creator** (`roles/iam.serviceAccountTokenCreator`)
  * **Service Account OpenID Token Creator** (`roles/iam.serviceAccountOpenIdTokenCreator`)




### Console

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Find the row for **Compute Engine default service account** and click mode_edit  **Edit principal**.

  3. Click **Add another role** and select the role **Managed Kafka Client**. Repeat this step for the **Schema Registry Admin** , **Service Account Token Creator** , and **Service Account OpenID Token Creator** roles.

  4. Click **Save**.




###  gcloud 

To grant IAM roles, use the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command.
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
      --role=roles/managedkafka.client
    
    gcloud projects add-iam-policy-binding PROJECT_ID\
      --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
      --role=roles/managedkafka.schemaRegistryAdmin
    
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

## Set up an Apache Maven project

From your SSH session, run the following commands to set up a Maven project.

  1. Install Java and Maven with the command:
         
         sudo apt-get install maven openjdk-17-jdk
         

**Note:** The installation of OpenJDK might take more than 5 minutes, and might appear to get stuck. You can try interrupting the installation with `Ctrl`+`C`. In most cases, the necessary packages are installed even if the process is interrupted. To confirm the successful installation, proceed to the next step.
  2. Set up an Apache Maven project.

Use the following command to create a package `com.google.example` in a directory called `demo`.
         
         mvn archetype:generate -DartifactId=demo -DgroupId=com.google.example\
            -DarchetypeArtifactId=maven-archetype-quickstart\
            -DarchetypeVersion=1.5 -DinteractiveMode=false
         




## Define the schema and its Java implementation

In this example, a message represents a "user" that has a name and an optional ID. The corresponds to an Avro schema with two fields: a required field `name` of type `string` and an optional integer `id.` To use this schema in a Java program, you will also need to generate an Java implementation of an object corresponding to this schema.

  1. Change into the project directory with `cd demo`.

  2. Create the folders for storing schema files in your code:
         
         mkdir -p src/main/avro
         

  3. Create the Avro schema definition by pasting the following code into a file called `src/main/avro/User.avsc`:
         
         {
           "namespace": "com.google.example",
           "type": "record",
           "name": "User",
           "fields": [
             {"name": "name", "type": "string"},
             {"name": "id",  "type": ["int", "null"]}
           ]
         }
         

  4. Configure your Maven project to use an Avro Java code generation plugin by adding the following to the `build` node of your `pom.xml.` Note that the `pom.xml` may have other `plugins` nodes inside the `pluginManagement` node. Don't change the `pluginManagement` node in this step. The `plugins` node needs to be at the same level level as `pluginManagement`.
         
         <plugins>
         <plugin>
           <groupId>org.apache.avro</groupId>
           <artifactId>avro-maven-plugin</artifactId>
           <version>1.11.1</version>
           <executions>
             <execution>
               <phase>generate-sources</phase>
               <goals>
                 <goal>schema</goal>
               </goals>
               <configuration>
                 <sourceDirectory>${project.basedir}/src/main/avro/</sourceDirectory>
                 <outputDirectory>${project.basedir}/src/main/java/</outputDirectory>
               </configuration>
             </execution>
           </executions>
         </plugin>
         </plugins>
         

  5. Add Avro as a dependency by adding the following to the end of the `project/dependencies` node of `pom.xml`. Note that the `pom.xml` already has a `dependencies` node inside `dependencyManagement` tag. Don't change the `dependencyManagement` node in this step.
         
         <dependency>
           <groupId>org.apache.avro</groupId>
           <artifactId>avro</artifactId>
           <version>1.11.1</version>
         </dependency>
         

  6. Generate Java sources
         
         mvn generate-sources
         

  7. Run the following command to check that the implementation source file was created. The source is a Java class file that implements constructors, accessors, serializers and de-serializers for `User` objects. You will use this class in the producer code.
         
         cat src/main/java/com/google/example/User.java
         




For more information about Apache Avro, see [Apache Avro getting started guide](https://avro.apache.org/docs/1.11.1/getting-started-java/).

## Create a producer client

This section walks through the steps of writing, building, and running a producer client.

### Implement the producer

The producer uses [KafkaAvroSerializer.java](https://github.com/confluentinc/schema-registry/blob/master/avro-serializer/src/main/java/io/confluent/kafka/serializers/KafkaAvroSerializer.java) to encode messages and manage their schemas. The serializer automatically connects to the schema registry, registers the schema under a subject, retrieves its ID, and then serializes the message using Avro. You still need to configure the producer and serializer.

  1. Create the producer client class by pasting the following code into a new file called `src/main/java/com/google/example/UserProducer.java`
         
         package com.google.example;
         import java.util.Properties;
         import org.apache.kafka.clients.producer.KafkaProducer;
         import org.apache.kafka.clients.producer.ProducerRecord;
         import org.apache.kafka.clients.producer.RecordMetadata;
         import org.apache.kafka.clients.producer.ProducerConfig;
         import org.apache.kafka.common.serialization.StringSerializer;
         import io.confluent.kafka.serializers.KafkaAvroSerializer;
         
           public class UserProducer {
         
             private static Properties configure() throws Exception {
                 Properties p = new Properties();
                 p.load(new java.io.FileReader("client.properties"));
                 p.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
                 p.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, KafkaAvroSerializer.class);
                 return p;
             }
         
             public static void main(String[] args) throws Exception {
                 Properties p = configure();
         
                 KafkaProducer<String, User> producer = new KafkaProducer<String, User>(p);
                 final User u = new User("SchemaEnthusiast", 42);
                 final String topicName = "newUsers";
                 ProducerRecord<String, User>  message =
                   new ProducerRecord<String, User>(topicName, "", u);
                 producer.send(message, new SendCallback());
                 producer.close();
             }
           }
         

  2. Define the callback class in `src/main/java/com/google/example/SendCallback.java`:
         
         package com.google.example;
         
         import org.apache.kafka.clients.producer.Callback;
         import org.apache.kafka.clients.producer.RecordMetadata;
         
         class SendCallback implements Callback {
               public void onCompletion(RecordMetadata m, Exception e){
                   if (e == null){
                     System.out.println("Produced a message successfully.");
                   } else {
                     System.out.println(e.getMessage());
                   }
               }
         }
         

  3. To compile this code, you need the `org.apache.kafka.clients` package and the serializer code. The serializer Maven artifact is distributed through a custom repository. Add the following node to the `project` node of your `pom.xml` to configure this repository:
         
         <repositories>
             <repository>
               <id>confluent</id>
               <name>Confluent</name>
               <url>https://packages.confluent.io/maven/</url>
             </repository>
           </repositories>
         

  4. Add the following to the `dependencies` node in your `pom.xml` file:
         
         <dependency>
               <groupId>org.slf4j</groupId>
               <artifactId>slf4j-simple</artifactId>
               <version>1.7.32</version>
             </dependency>
             <dependency>
               <groupId>io.confluent</groupId>
               <artifactId>kafka-avro-serializer</artifactId>
               <version>7.8.1</version>
             </dependency>
             <dependency>
               <groupId>org.apache.kafka</groupId>
               <artifactId>kafka-clients</artifactId>
               <version>3.7.2</version>
             </dependency>
         

  5. To make sure all the dependencies are properly resolved, compile the client:
         
         mvn compile
         




### Create a schema registry

To create a schema registry, run the following command:
    
    
    gcloud beta managed-kafka schema-registries create REGISTRY_ID \
        --location=REGION
    

Replace the following:

  * REGISTRY_ID: a unique identifier for your new schema registry. This forms part of the registry's resource name. The name must start with a letter, contain only letters `(a-z, A-Z)`, numbers `(0-9)`, and underscores `(_)`, and be 63 characters or less.

  * REGION: Google Cloud region where the schema registry is going to be created. This location must match the region of the Kafka cluster or clusters using this registry.




The schema definition that you have created is not yet uploaded to the registry. The producer client does this the first time it runs in the following steps.

### Configure and run the producer

At this point the producer won't run since it is not fully configured. To configure the producer, provide both the Kafka and schema registry configuration.

  1. Look up the bootstrap address of your Kafka cluster following [View a cluster's bootstrap address](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-bootstrap-address)

  2. Create a file called `client.properties` in the same directory as your `pom.xml` and add the following content to it:
         
         bootstrap.servers=BOOTSTRAP
         security.protocol=SASL_SSL
         sasl.mechanism=OAUTHBEARER
         sasl.login.callback.handler.class=com.google.cloud.hosted.kafka.auth.GcpLoginCallbackHandler
         sasl.jaas.config=org.apache.kafka.common.security.oauthbearer.OAuthBearerLoginModule required;
         
         schema.registry.url=https://managedkafka.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/schemaRegistries/REGISTRY_ID
         bearer.auth.credentials.source=CUSTOM
         bearer.auth.custom.provider.class=com.google.cloud.hosted.kafka.auth.GcpBearerAuthCredentialProvider
         

Add the Kafka and schema registry authentication handler dependencies to your Maven project by inserting the following to the `dependencies` node of `pom.xml` _above_ the `kafka-avro-serializer` dependency:
         
         <dependency>
               <groupId>com.google.cloud.hosted.kafka</groupId>
               <artifactId>managed-kafka-auth-login-handler</artifactId>
               <version>1.0.6</version>
               <exclusions>
                 <exclusion>
                   <groupId>io.confluent</groupId>
                   <artifactId>kafka-schema-registry-client</artifactId>
                 </exclusion>
             </exclusions>
           </dependency>
         

If you would like to see the implementation of the custom schema registry authentcation handler authentication handler, look at the [GcpBearerAuthCredentialProvider](https://github.com/googleapis/managedkafka/blob/main/kafka-java-auth/src/main/java/com/google/cloud/hosted/kafka/auth/GcpBearerAuthCredentialProvider.java) class.

  3. Compile and run the producer client:
         
         mvn compile -q exec:java -Dexec.mainClass=com.google.example.UserProducer
         

If all goes well, you see the output `Produced a message successfully` generated by the `SendCallback` class.




## Examine the output

  1. Check that the `User` schema has been registered under a subject name derived from the topic and schema names:
         
         SR_DOMAIN=https://managedkafka.googleapis.com
         SR_PATH=/v1/projects/PROJECT_ID/locations/REGION
         SR_HOST=$SR_DOMAIN/$SR_PATH/schemaRegistries/REGISTRY_ID/subjects
         
         curl -X GET \
           -H "Content-Type: application/vnd.schemaregistry.v1+json" \
           -H "Authorization: Bearer $(gcloud auth print-access-token)"\
           $SR_HOST
         

The output of this command should look like this:
         
         ["newUsers-value"]
         

  2. Check that the schema registered in the repository is the same as `User`:
         
         curl -X GET \
           -H "Content-Type: application/vnd.schemaregistry.v1+json" \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           $SR_HOST/newUsers-value/versions/1
         

The output of the command should look like this:
         
         {
           "subject": "newUsers-value",
           "version": 1,
           "id": 2,
           "schemaType": "AVRO",
           "schema": "{\"type\":\"record\",\"name\":\"User\",\"namespace\":\"com.google.example\",\"fields\":[{\"name\":\"name\",\"type\":\"string\"},{\"name\":\"id\",\"type\":[\"int\",\"null\"]}]}",
           "references": []
         }
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Console

  1. Delete the VM instance.

     1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. Select the VM and click **Delete**.

  2. Delete the schema registry.

     1. Go to the **Schema registries** page.

[Go to Schema registries](https://console.cloud.google.com/managedkafka/schemaRegistries)

     2. Click the name of the schema registry.

     3. Click **Delete**.

  3. Delete the Kafka cluster.

     1. Go to the **Managed Service for Apache Kafka** > **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/managedkafka/clusters)

     2. Select the Kafka cluster and click **Delete**.




###  gcloud 

  1. To delete the VM, use the [`gcloud compute instances delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/delete) command.
         
         gcloud compute instances delete VM_NAME --zone=ZONE
         

  2. To delete the schema registry, use the [`/sdk/gcloud/reference/managed-kafka/schema-registries/delete`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/schema-registries/delete) command.
         
         gcloud beta managed-kafka schema-registries delete REGISTRY_ID \
           --location=REGION
         

  3. To delete the Kafka cluster, use the [`gcloud managed-kafka clusters delete`](https://docs.cloud.google.com/sdk/gcloud/reference/managed-kafka/clusters/delete) command.
         
         gcloud managed-kafka clusters delete CLUSTER_ID \
           --location=REGION --async
         




## What's next

  * [Schema registry overview](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/schema-registry/schema-registry-overview).
  * [Overview of Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview).
  * [Authenticate to Managed Kafka API](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/authentication).
  * [Write Avro messages to BigQuery by using Kafka Connect](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/kafka-connect-schema-registry)



_Confluent is a registered trademark of Confluent, Inc._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

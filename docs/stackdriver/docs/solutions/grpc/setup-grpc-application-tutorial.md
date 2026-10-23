---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/setup-grpc-application-tutorial/
title: Set up a gRPC application on Google Cloud with Microservices observability \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:33.388861+00:00
---

# Set up a gRPC application on Google Cloud with Microservices observability  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/setup-grpc-application-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Reference ](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview)



Send feedback 

#  Set up a gRPC application on Google Cloud with Microservices observability Stay organized with collections  Save and categorize content based on your preferences. 

Microservices observability tools provide you with the ability to instrument your applications to collect and present telemetry data in Cloud Monitoring, Cloud Logging, and Cloud Trace from gRPC workloads deployed on Google Cloud and elsewhere. Microservices observability works with any deployment that has been granted permission to access Monitoring, Logging, and Trace by enabling the Microservices API.

In this tutorial you learn how to use Microservices observability features by building a simple gRPC application on Google Cloud using Compute Engine and instrument your application with Microservices observability, and view them come up live on Monitoring and Logging.

## Objectives

At a high level, you do the following.

  * As a service developer, you can:

    * Create a gRPC application with the language of your choice (C++, Go, or Java).
    * Opt in your application and control the Microservices observability plugin.
    * Deploy the application on a Compute Engine VM.
  * As a service operator, you consume the collected data in various ways:

    * View traces on Trace.
    * View metrics on the monitoring dashboard called Microservices (gRPC) Monitoring.
    * View metrics on Metrics Explorer.
    * Inspect log entries on Logs Explorer.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Compute Engine](https://cloud.google.com/compute/all-pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

###  Console 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Compute Engine, and Microservices API APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,microservices.googleapis.com)

  5. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the following roles to the service account: **Logging > Logs Viewer > Logs Writer, Monitoring > Monitoring Editor > Metrics Writer, Trace > Trace Admin > Trace Agent**. 

To grant a role, find the **Select a role** list, then select the role. 

To grant additional roles, click add **Add another role** and add each additional role. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. In the **Service account users role** field, enter the identifier for the principal that will attach the service account to other resources, such as Compute Engine instances. 

This is typically the email address for a Google Account.

     9. Click **Done** to finish creating the service account. 

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Compute Engine, and Microservices API APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,microservices.googleapis.com)

  9. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the following roles to the service account: **Logging > Logs Viewer > Logs Writer, Monitoring > Monitoring Editor > Metrics Writer, Trace > Trace Admin > Trace Agent**. 

To grant a role, find the **Select a role** list, then select the role. 

To grant additional roles, click add **Add another role** and add each additional role. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. In the **Service account users role** field, enter the identifier for the principal that will attach the service account to other resources, such as Compute Engine instances. 

This is typically the email address for a Google Account.

     9. Click **Done** to finish creating the service account. 

  10. Read the [Microservices observability overview](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc). 
  11. Read about the [two supported environment variables](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/set-up-observability#config-options), decide which to use, and determine the values required by the environment variable. 



###  cli 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Compute Engine, and Microservices API APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com microservices.googleapis.com

  8. Set up authentication:

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. Create the service account: 
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account. 

     3. Grant roles to the service account. Run the following command once for each of the following IAM roles: `roles/logging.logWriter, roles/monitoring.metricWriter, roles/cloudtrace.agent`: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" --role=ROLE

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
        * `ROLE`: the role to grant
**Note** : The `--role` flag affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     4. Grant the required role to the principal that will attach the service account to other resources. 
            
            gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com --member="user:USER_EMAIL" --role=roles/iam.serviceAccountUser

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
        * `USER_EMAIL`: the email address for a Google Account

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  13. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  14. Enable the Compute Engine, and Microservices API APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com microservices.googleapis.com

  15. Set up authentication:

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. Create the service account: 
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account. 

     3. Grant roles to the service account. Run the following command once for each of the following IAM roles: `roles/logging.logWriter, roles/monitoring.metricWriter, roles/cloudtrace.agent`: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" --role=ROLE

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
        * `ROLE`: the role to grant
**Note** : The `--role` flag affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     4. Grant the required role to the principal that will attach the service account to other resources. 
            
            gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com --member="user:USER_EMAIL" --role=roles/iam.serviceAccountUser

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
        * `USER_EMAIL`: the email address for a Google Account

  16. Read the [Microservices observability overview](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc). 
  17. Read about the [two supported environment variables](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/set-up-observability#config-options), decide which to use, and determine the values required by the environment variable. 



## Create and connect to a Compute Engine VM

Use these instructions to create and connect to a Compute Engine VM instance. On the VM you deploy your application and then instrument the application with Microservices observability.

  1. Create a VM instance:
         
         gcloud compute instances create grpc-observability-vm \
           --image-family=debian-11 \
           --image-project=debian-cloud \
           --service-account=SERVICE_ACCOUNT_NAME@$PROJECT_ID.iam.gserviceaccount.com
         

  2. Connect to the VM instance:
         
         gcloud compute ssh --project=$PROJECT_ID grpc-observability-vm
         




## Deploy your application to the Compute Engine VM

You can either deploy an application of your choice to the Compute Engine VM that you created in the previous step, then skip this step, or you can use an example to continue with instructions in your preferred language.

###  C++ 

  1. After you connect to the VM instance, run the following command.
         
         sudo apt-get update -y
         sudo apt-get install -y git build-essential clang
         git clone -b v1.54.0 https://github.com/grpc/grpc.git --depth=1
         




###  Go 

  1. Make sure that you have Go installed.
         
         sudo apt-get install -y git
         sudo apt install wget
         wget https://go.dev/dl/go1.20.2.linux-amd64.tar.gz
         sudo rm -rf /usr/local/go && sudo tar -C /usr/local -xzf \
         go1.20.2.linux-amd64.tar.gz
         export PATH=$PATH:/usr/local/go/bin
         

  2. Clone the `gRPC-Go` examples.
         
         git clone https://github.com/grpc/grpc-go.git
         cd grpc-go/
         git checkout -b run-observability-example
         875c97a94dca8093bf01ff2fef490fbdd576373d
         




###  Java 

  1. After you connect to the VM instance, make sure that you have Java 8 or later installed.
         
         sudo apt update
         sudo apt upgrade
         sudo apt install git
         sudo apt-get install -y openjdk-11-jdk-headless
         

  2. Clone the `grpc-java` repository.
         
         export EXAMPLES_VERSION=v1.54.1
         git clone -b $EXAMPLES_VERSION --single-branch --depth=1 \
         https://github.com/grpc/grpc-java.git
         




## Create gRPC Google Cloud Observability config file

You need separate gRPC Google Cloud Observability config file to enable Microservices observability for both server and client. The location of this file is exported as `GRPC_GCP_OBSERVABILITY_CONFIG_FILE` in the future steps. Use the following instruction on how to set up the different parameters in the config file. 

### Example `GRPC_GCP_OBSERVABILITY_CONFIG_FILE`
    
    
    {
      "project_id": "your-project-here",
      "cloud_logging": {
        "client_rpc_events": [
        {
          "methods": ["google.pubsub.v1.Subscriber/Acknowledge", "google.pubsub.v1.Publisher/CreateTopic"],
          "exclude": true,
        },
        {
          "methods": ["google.pubsub.v1.Subscriber/*", "google.pubsub.v1.Publisher/*"],
          "max_metadata_bytes": 4096,
          "max_message_bytes": 4096,
        }],
        "server_rpc_events": [{
          "methods": ["*"],
          "max_metadata_bytes": 4096,
          "max_message_bytes": 4096
        }],
      },
      "cloud_monitoring": {},
      "cloud_trace": {
        "sampling_rate": 0.5,
      }
      "labels": {
        "SOURCE_VERSION": "J2e1Cf",
        "SERVICE_NAME": "payment-service-1Cf",
        "DATA_CENTER": "us-west1-a"
      }
    }
    

The following sections contain instructions for enabling data collection in your configuration for the individual components. If you used the gRPC example in this tutorial, you can use this config as is (after updating `your-project-here`) or use this as a template for your application.and an example showing the configuration information in an environment variable.

### Enable metrics

To enable metrics, add the `cloud_monitoring` object to the configuration and set its value to `{}`.

For more information about metrics, see [Metrics definitions](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/observability-reference#metrics-def).

### Enable tracing

To enable tracing, do the following:

  1. Add the `cloud_trace` object to the configuration.
  2. Set the `cloud_trace.sampling_rate` to `0.5` which to randomly traces 50% of RPCs.



If you plan to enable tracing across services, ensure that the services support the propagation of trace context received from upstream (or started by itself) to downstream.

For more information about tracing, see [Trace definitions](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/observability-reference#trace-def).

### Enable logging

To enable logging, do the following:

  1. Add the `cloud_logging` object to the configuration.
  2. Add a pattern to either or both of `client_rpc_events` and `server_rpc_events` specifying the set of services or methods for which you want to generate transport-level event logging and the number of bytes to log for headers and messages.



For more information about logging, see [Log record definitions](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/observability-reference#log-record-defs).

## Instrument your applications for the observability plugin

To instrument your applications so that they can use the Microservices observability plugin, use the following instructions for your preferred language.

### C++

You can use C++ with Microservices observability as of gRPC C++ v1.54. The [example repository](https://github.com/grpc/grpc/tree/v1.54.0/examples/cpp/gcp_observability/helloworld) is in GitHub.

  1. Observability support is only available through the Bazel build system. Add the target `grpcpp_gcp_observability` as a dependency.

  2. Opting in Microservices observability requires an additional dependency (an observability modul) and the following code changes to existing gRPC clients, servers, or both:
         
         #include <grpcpp/ext/gcp_observability.h>
         
         int main(int argc, char** argv) {
           auto observability = grpc::GcpObservability::Init();
           assert(observability.ok());
           …
           // Observability data flushed when object goes out of scope
         }
         

Before any gRPC operations, including creating a channel, server, or credentials, invoke the following:
         
         grpc::GcpObservability::Init();
         

This returns `absl::StatusOr<GcpObservability>` which should be saved. The status helps determine whether observability was successfully initialized. The accompanying `GcpObservability` object controls the lifetime of observability, and automatically closes and flushes observability data when it goes out of scope.




### Go

  1. Microservices observability plugins are supported for gRPC Go versions `v1.54.0` and later. The [example repository](https://github.com/grpc/grpc-go/tree/master/examples/features/observability) is in GitHub.



With the Go module, opting in Microservices observability requires an observability module and the following code:
    
    
    import "google.golang.org/grpc/gcp/observability"
    
    func main() {
      ctx, cancel := context.WithTimeout(context.Background(), time.Second)
      defer cancel()
      if err := observability.Start(ctx); err != nil {
        log.Warning("Unable to start gRPC observability:", err)
      }
      defer observability.End()
      …
    }
    

The `observability.Start` call parses the configuration from environment variables, creates exporters accordingly, and injects collection logic to client connections and servers created after the call. The deferred`observability.End` call cleans up resources and ensures that buffered data is flushed before the application closes.

After the application code is updated, run the following command to update the `go.mod` file.
    
    
    go mod tidy
    

### Java

To use Microservices observability with Java applications, modify your build to include the `grpc-gcp-observability` artifact. Use gRPC version 1.54.1 or later.

In the build snippets in the Gradle and Maven build tool sections, `grpcVersion` is set to the value 1.54.1.

The [example repository](https://github.com/grpc/grpc-java/tree/v1.54.1/examples/example-gcp-observability) is in GitHub.

  1. To successfully instrument your Java applications for Microservices observability, add the following code to `main()`.


    
    
    ...
    import io.grpc.gcp.observability.GcpObservability;
    ...
    
    // Main application class
    ...
    
    public static void main(String[] args) {
    ...
      // call GcpObservability.grpcInit() to initialize & get observability
      GcpObservability observability = GcpObservability.grpcInit();
    
    ...
      // call close() on the observability instance to shutdown observability
      observability.close();
    ...
    }
    

Note that you must call `GcpObservability.grpcInit()` before any gRPC channels or servers are created. The `GcpObservability.grpcInit()` function reads the Microservices observability configuration and uses that to set up the global interceptors and tracers that are required for the logging, metrics, and trace features in each channel and server created. `GcpObservability.grpcInit()` is thread safe and must be called exactly once. It returns an instance of `GcpObservability` that you must save in order to call `close()` later.

`GcpObservability.close()` de-allocates resources. Any channel or servers created afterwards don't perform any logging.

`GcpObservability` implements `java.lang.AutoCloseable`, which is closed automatically if you use `try-with-resource`s as follows:
    
    
    ...
    import io.grpc.gcp.observability.GcpObservability;
    ...
    
    // Main application class
    ...
    
    public static void main(String[] args) {
    ...
      // call GcpObservability.grpcInit() to initialize & get observability
      try (GcpObservability observability = GcpObservability.grpcInit()) {
    
    ...
      } // observability.close() called implicitly
    ...
    }
    

#### Use the Gradle build tool

If you are using the Gradle build tool, include the following:
    
    
    def grpcVersion = '1.54.1'
    
    ...
    
    dependencies {
    ...
    implementation "io.grpc:grpc-gcp-observability:${grpcVersion}"
    ...
    }
    

#### Use the Maven build tool (pom.xml)

If you are using the Maven build tool, include the following:
    
    
    <properties>
    ...
    <grpc.version>1.54.1</grpc.version>
    ...
    </properties>
    
    ...
    
    <dependencies>
    ...
    <dependency>
    <groupId>io.grpc</groupId>
    <artifactId>grpc-gcp-observability</artifactId>
    <version>${grpc.version}</version>
    </dependency>
    ...
    </dependencies>
    

## Run your application

Follow the instructions in this section only if you used the gRPC example for the tutorial. You can modify the `run` command to target your application binary.

### Run Server

### C++

  1. Create a SSH session into the VM.
  2. Export environmental variables. Use steps defined above to create `server_config.json`.
         
         export GOOGLE_CLOUD_PROJECT=$PROJECT_ID
           export GRPC_GCP_OBSERVABILITY_CONFIG_FILE="$(pwd)/examples/cpp/gcp_observability/helloworld/server_config.json"
         

  3. Run the server application `shell cd grpc tools/bazel run examples/cpp/gcp_observability/helloworld:greeter_server`




###  Go 

  1. Create a SSH session into the VM.
  2. Export environmental variables. Use steps defined above to create `server_config.json`.
         
         export GRPC_GCP_OBSERVABILITY_CONFIG_FILE=./server/serverConfig.json
         

  3. Run the server application `shell go run ./server/main.go`




###  Java 

  1. In the examples directory, open the README file and follow the instructions in the file.
  2. When the instructions tell you to open another terminal window, issue this command: `shell gcloud compute ssh --project=$PROJECT_ID grpc-observability-vm`



### Run Client

### C++

  1. Create another SSH session into the VM.
  2. Export environmental variables. Use steps defined above to create `client_config.json` file.
         
         export GOOGLE_CLOUD_PROJECT=$PROJECT_ID
           export GRPC_GCP_OBSERVABILITY_CONFIG_FILE="$(pwd)/examples/cpp/gcp_observability/helloworld/client_config.json"
         

  3. Run the client application
         
         cd grpc
         tools/bazel run examples/cpp/gcp_observability/helloworld:greeter_client
         




###  Go 

  1. Create another SSH session into the VM.
  2. Export environmental variables. Use steps defined above to create `client_config.json` file. `shell export GRPC_GCP_OBSERVABILITY_CONFIG_FILE=./client/clientConfig.json`
  3. Run the client application
         
         cd grpc-go/examples/features/observability
         go run ./client/main.go
         




###  Java 

  1. In the examples directory, open the README file and follow the instructions in the file.
  2. When the instructions tell you to open another terminal window, issue this command: `shell gcloud compute ssh --project=$PROJECT_ID grpc-observability-vm`



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete individual resources

  1. Delete the instance: 
         
         gcloud compute instances delete INSTANCE_NAME




## What's next

  * For detailed information about configuration data, trace definitions, metrics definitions, and log definitions see [Microservices observability reference](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/observability-reference).
  * For information about viewing logs, traces, and metrics, see [View traces, metrics, and log entries](https://docs.cloud.google.com/stackdriver/docs/solutions/grpc/set-up-observability#view-all)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

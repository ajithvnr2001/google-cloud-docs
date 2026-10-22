---
url: https://docs.cloud.google.com/cpp/docs/quickstart-open-telemetry/
title: Quickstart: Trace a C++ Application \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:26.852328+00:00
---

# Quickstart: Trace a C++ Application  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/quickstart-open-telemetry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Guides ](https://docs.cloud.google.com/cpp/docs/setup)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Trace a C++ Application

Learn how to compile and run the C++ example with [OpenTelemetry](https://opentelemetry.io/) and export the traces to [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview) This example uses the Google Cloud Pub/Sub C++ client to publish 5 messages and exports the traces to Cloud Trace.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Pub/Sub and Trace APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=pubsub,cloudtrace&redirect=https%3A//console.cloud.google.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Pub/Sub and Trace APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=pubsub,cloudtrace&redirect=https%3A//console.cloud.google.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 




## Set up

  1. Create a topic with the ID `my-topic`:
         
         gcloud pubsub topics create my-topic
         

  2. Checkout the C++ sample source code:
         
         git clone --depth 1 https://github.com/GoogleCloudPlatforms/cpp-samples
         




## Publish messages
    
    
    // Create a few namespace aliases to make the code easier to read.
    namespace gc = ::google::cloud;
    namespace otel = gc::otel;
    namespace pubsub = gc::pubsub;
    
    // This example uses a simple wrapper to export (upload) OTel tracing data
    // to Google Cloud Trace. More complex applications may use different
    // authentication, or configure their own OTel exporter.
    auto project = gc::Project(project_id);
    auto configuration = otel::ConfigureBasicTracing(project);
    
    auto publisher = pubsub::Publisher(pubsub::MakePublisherConnection(
        pubsub::Topic(project_id, topic_id),
        // Configure this publisher to enable OTel tracing. Some applications may
        // chose to disable tracing in some publishers or to dynamically enable
        // this option based on their own configuration.
        gc::Options{}.set<gc::OpenTelemetryTracingOption>(true)));
    
    // After this point, use the Cloud Pub/Sub C++ client library as usual.
    // In this example, we will send a few messages and configure a callback
    // action for each one.
    std::vector<gc::future<void>> ids;
    for (int i = 0; i < 5; i++) {
      auto id = publisher.Publish(pubsub::MessageBuilder().SetData("Hi!").Build())
                    .then([](gc::future<gc::StatusOr<std::string>> f) {
                      auto id = f.get();
                      if (!id) {
                        std::cout << "Error in publish: " << id.status() << "\n";
                        return;
                      }
                      std::cout << "Sent message with id: (" << *id << ")\n";
                    });
      ids.push_back(std::move(id));
    }
    // Block until the messages are actually sent.
    for (auto& id : ids) id.get();

  1. Compile and run the example:
         
         cd cpp-samples/pubsub-open-telemetry
         bazel run //:quickstart -- $(gcloud config get project) my-topic
         

  2. After running this example, you'll see the following lines printed to console.
         
         Sent message with id: (9095112996778043)
         Sent message with id: (9095112996778044)
         Sent message with id: (9095112996778045)
         Sent message with id: (9095112996778046)
         Sent message with id: (9095112996778047)
         




## View traces

In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/stackdriver/images/trace-explorer-icon.png)**Trace explorer** page: 

[Go to **Trace explorer**](https://console.cloud.google.com/traces/explorer)

You can also find this page by using the search bar.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. Delete the topic created by the example:
         
         gcloud pubsub topics delete my-topic
         




## What's next

  * Learn more about [C++ and OpenTelemetry](https://docs.cloud.google.com/trace/docs/setup/cpp-ot).
  * Find more [C++ examples](https://docs.cloud.google.com/docs/samples/?language=cpp).
  * Learn more about [Pub/Sub APIs](https://docs.cloud.google.com/pubsub/docs/reference/service_apis_overview).
  * Try more [C++ Pub/Sub OpenTelemetry Examples](https://github.com/GoogleCloudPlatform/cpp-samples/tree/main/pubsub-open-telemetry).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

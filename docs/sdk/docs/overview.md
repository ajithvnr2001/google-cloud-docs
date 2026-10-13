---
url: https://docs.cloud.google.com/sdk/docs/overview/
title: Google Cloud SDK overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:26.869746+00:00
---

# Google Cloud SDK overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Google Cloud SDK overview Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud SDK is a suite of libraries and tools for interacting with Google Cloud services. It includes command-line tools, language-specific client libraries, IDE extensions, and emulators that help you manage resources and automate tasks on Google Cloud.

With Google Cloud SDK, you can:

  * **Manage Google Cloud resources:** Use the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) to control virtual machines, applications, databases, and other services from the command line.
  * **Integrate with Google Cloud APIs:** Build applications using [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) available in languages like [Java](https://docs.cloud.google.com/java/docs), [C++](https://docs.cloud.google.com/cpp/docs), [Python](https://docs.cloud.google.com/python/docs), [Node.js](https://docs.cloud.google.com/nodejs/docs), [Ruby](https://docs.cloud.google.com/ruby/docs), [Go](https://docs.cloud.google.com/go/docs), [.NET](https://docs.cloud.google.com/dotnet/docs), [PHP](https://docs.cloud.google.com/php/docs), and [Rust](https://docs.cloud.google.com/rust).
  * **Develop and test locally:** Accelerate development cycles with local emulators for services including [Pub/Sub](https://docs.cloud.google.com/pubsub), [Spanner](https://docs.cloud.google.com/spanner), [Bigtable](https://docs.cloud.google.com/bigtable), and [Firestore in Datastore mode (Datastore)](https://docs.cloud.google.com/datastore).
  * **Work within your IDE:** Use [Cloud Code extensions](https://docs.cloud.google.com/code) to interact with Google Cloud services directly from Visual Studio Code and IntelliJ.



## Core components

### The gcloud CLI

The gcloud CLI is the primary command-line tool for Google Cloud. Use it to perform administrative tasks from your terminal.

For more information, see the [gcloud CLI overview](https://docs.cloud.google.com/sdk/gcloud).

### Cloud Client Libraries for API access

To programmatically interact with Google Cloud services from your applications, use the [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries). These libraries provide idiomatic access to Google Cloud APIs, simplifying integration and reducing boilerplate code.

Cloud Client Libraries are available for the following languages:

  * [C++](https://docs.cloud.google.com/cpp/docs)
  * [.NET](https://docs.cloud.google.com/dotnet/docs)
  * [Go](https://docs.cloud.google.com/go/docs)
  * [Java](https://docs.cloud.google.com/java/docs)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs)
  * [PHP](https://docs.cloud.google.com/php/docs)
  * [Python](https://docs.cloud.google.com/python/docs)
  * [Ruby](https://docs.cloud.google.com/ruby/docs)
  * [Rust](https://docs.cloud.google.com/rust)



SAP developers can also use the [ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/overview), which provides a comprehensive set of client libraries for ABAP environments.

For a complete list and overview of available APIs, see [Google Cloud APIs](https://docs.cloud.google.com/apis/docs/overview).

## Development and testing tools

### IDE integration

Google Cloud SDK provides IDE extensions that bring Google Cloud services directly into your development workflow. With these extensions, you can build, deploy, and debug applications without leaving your favorite editor.

Cloud Code extensions are available for:

  * [Visual Studio Code](https://docs.cloud.google.com/code/docs/vscode/overview)
  * [IntelliJ](https://docs.cloud.google.com/code/docs/intellij/overview)



For more information, see the [Cloud Code documentation](https://docs.cloud.google.com/code).

### Emulators

Emulators let you develop and test your applications by simulating the behavior of Google Cloud services. Use emulators to help you save costs, avoid impacting production services, and iterate faster during development.

The Google Cloud SDK provides emulators for several services, including:

  * **[Bigtable](https://docs.cloud.google.com/bigtable/docs/emulator-overview)** : Test applications using a local NoSQL wide-column database.
  * **[Datastore](https://docs.cloud.google.com/datastore/docs/tools/datastore-emulator)** : Develop against a local NoSQL document database.
  * **[Firestore](https://docs.cloud.google.com/firestore/docs/emulator)** : Build and test mobile, web, and server applications with a local document database.
  * **[Pub/Sub](https://docs.cloud.google.com/pubsub/docs/emulator)** : Validate asynchronous messaging workflows locally.
  * **[Spanner](https://docs.cloud.google.com/spanner/docs/emulator)** : Test applications requiring a globally-distributed relational database locally.



These emulators provide a high-fidelity environment for debugging issues and verifying your application's behavior before deployment.

For more details on using these tools, see [Using Google Cloud SDK emulators](https://docs.cloud.google.com/sdk/docs/emulators).

## Work with other frameworks and tools

The Google Cloud SDK is designed to work with a wide range of popular frameworks and tools, helping you streamline application development and deployment on Google Cloud. While not part of the core SDK components, these tools often use the gcloud CLI or Cloud Client Libraries for seamless interaction with Google Cloud services.

Examples include:

  * **[Spring Framework](https://docs.cloud.google.com/java/docs/spring):** Utilize Google Cloud integrations for Spring Boot applications.
  * **[Kubernetes](https://docs.cloud.google.com/kubernetes-engine/docs):** Manage deployments on Google Kubernetes Engine (GKE) using `kubectl`, often installed alongside the gcloud CLI.
  * **[Google Cloud's daptic to Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus):** Collect and analyze metrics from your applications.
  * **[Terraform](https://docs.cloud.google.com/docs/terraform):** Provision and manage your Google Cloud infrastructure as code using the Google Cloud provider.



## What's next

  * Install the [gcloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk) and learn useful commands with the [gcloud CLI cheat sheet](https://docs.cloud.google.com/sdk/docs/cheatsheet). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/swift/quickstart/
title: Quickstart: Get started with Swift \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:53.354040+00:00
---

# Quickstart: Get started with Swift  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/swift/quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Swift ](https://docs.cloud.google.com/swift)
  * [ Guides ](https://docs.cloud.google.com/swift/overview)



Send feedback 

#  Quickstart: Get started with Swift Stay organized with collections  Save and categorize content based on your preferences. 

This quickstart shows you how to set up your development environment, initialize a new Swift project using Swift Package Manager (SPM), add the Google Cloud Secret Manager client library as a dependency, and make an API call to list secrets in your Google Cloud project.

## Before you begin

  1. In the Google Cloud console, on the project selector page, [select or create a Google Cloud project](https://console.cloud.google.com/projectselector2).

  2. Confirm that billing is [enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-project).

  3. Install and initialize the Google Cloud CLI. For instructions, see [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).

  4. Install the Swift toolchain:

     * **macOS** : Install Xcode 16 or later from the Mac App Store, or install the Command Line Tools by running `xcode-select --install`.
     * **Linux** : Install Swift using [swiftly](https://www.swift.org/swiftly/) or by downloading a toolchain for your distribution from [Swift.org](https://www.swift.org/download/).

Verify that Swift 6.2 or later is installed by running:
    
    swift --version
    

  5. Enable the Secret Manager API:
         
         gcloud services enable secretmanager.googleapis.com
         

  6. Set up local authentication using Application Default Credentials (ADC):
         
         gcloud auth application-default login
         

The Google Cloud client libraries for Swift automatically discover and use these credentials when running in your local development environment.

  7. (Optional) Create a secret to list during this tutorial:
         
         printf "my-super-secret-data" | gcloud secrets create my-quickstart-secret \
             --data-file=- \
             --replication-policy="automatic"
         




## Create a Swift package

Create a new directory for your application and initialize a Swift executable package:
    
    
    mkdir Quickstart
    cd Quickstart
    swift package init --name Quickstart --type executable
    

This creates a standard Swift package structure:

  * `Package.swift`: Manifest defining your package, dependencies, and build targets.
  * `Sources/Quickstart/Quickstart.swift`: The entry point for your application.



When building on macOS, the client libraries require macOS 15 or later. Because `swift package init` defaults to older macOS deployment targets, edit `Package.swift` to add `platforms: [ .macOS(.v15) ]` if you are developing on macOS:
    
    
    let package = Package(
        name: "Quickstart",
        platforms: [
            .macOS(.v15)
        ],
        // ...
    )
    

## Add the Secret Manager client library

Add the `swift-google-cloud-secretmanager-v1` package dependency and link `GoogleCloudSecretManagerV1` to your executable target:
    
    
    swift package add-dependency \
        https://github.com/googleapis/swift-google-cloud-secretmanager-v1.git --from 0.4.0
    swift package add-target-dependency \
        GoogleCloudSecretManagerV1 Quickstart --package swift-google-cloud-secretmanager-v1
    

## Write the application code

Open `Sources/Quickstart/Quickstart.swift` (or `Sources/main.swift` depending on your Swift toolchain version) and replace its contents with the following code:
    
    
    import Foundation
    import GoogleCloudSecretManagerV1
    
    @main
    struct Quickstart {
      static func main() async throws {
        let args = CommandLine.arguments.dropFirst()
        guard let projectId = args.first else {
          print("Usage: GoogleCloudCLI <projectId>")
          exit(1)
        }
        let client = try SecretManagerServiceClient()
        let secrets = client.listSecretsByItems(
          request: ListSecretsRequest().with { $0.parent = "projects/\(projectId)" })
        for try await item in secrets {
          print("  \(item)")
        }
      }
    }

### Key concepts in the code

  * **Asynchronous main entry point (`@main`)**: Swift's built-in structured concurrency allows `static func main()` to be declared `async throws`, eliminating the need for custom runloops or blocking threads.
  * **Automatic credential resolution** : `SecretManagerServiceClient()` automatically detects your Application Default Credentials configured using `gcloud auth application-default login` without manual credential passing.
  * **Fluent request builder** : The `.with { ... }` pattern provides type-safe, closure-based chaining to configure request parameters cleanly.
  * **Streaming pagination (`AsyncSequence`)**: The `listSecretsByItems(request:)` method returns an `AsyncSequence`. Iterating with `for try await` automatically fetches subsequent pages behind the scenes, allowing you to stream large datasets without managing page tokens manually.



## Run the application

Run the application using `swift run`, passing your Google Cloud project ID as an argument:
    
    
    swift run Quickstart PROJECT_ID
    

Replace `PROJECT_ID` with your Google Cloud project ID.

If you created the `my-quickstart-secret` secret earlier, the output lists the secret resource in your project:
    
    
      GoogleCloudSecretManagerV1.Secret:
      name: "projects/1234567890/secrets/my-quickstart-secret"
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this quickstart, delete the resources you created:

  1. Delete the test secret:
         
         gcloud secrets delete my-quickstart-secret
         

  2. (Optional) If you created a project specifically for this quickstart, you can delete the project in the Google Cloud console:

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)




## What's next

  * Read the [Swift on Google Cloud overview](https://docs.cloud.google.com/swift/overview) for details on supported environments, Swift concurrency, and memory safety.
  * Explore the [Google Cloud Swift client libraries on GitHub](https://github.com/googleapis/google-cloud-swift).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

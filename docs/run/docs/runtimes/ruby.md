---
url: https://docs.cloud.google.com/run/docs/runtimes/ruby/
title: The Ruby runtime \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:24.648043+00:00
---

# The Ruby runtime  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/runtimes/ruby/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  The Ruby runtime Stay organized with collections  Save and categorize content based on your preferences. 

Your Cloud Run function runs in an environment consisting of an operating system version with add-on packages, language support, and the [Ruby Functions Framework](https://github.com/GoogleCloudPlatform/functions-framework-ruby) library that supports and invokes your function. This environment is identified by the language version, and is known as the runtime ID.

## Function preparation

You can prepare a function directly from the Google Cloud console or write it on your local machine and upload it. To prepare your local machine for Ruby development, see [Set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup).

## Supported Ruby runtimes and base images

Runtime | Runtime ID | Stacks | Runtime base image | Deprecation | Decommission  
---|---|---|---|---|---  
Ruby 4.0 | ruby40 |  google-24-full (default)  |  [google-24-full/ruby40](http://us-central1-docker.pkg.dev/serverless-runtimes/google-24-full/runtimes/ruby40) | 2029-03-31 | 2029-09-30  
Ruby 3.4 | ruby34 | 
* google-22 (default)
* google-22-full
| 
* [google-22/ruby34](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/ruby34)
* [google-22-full/ruby34](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/ruby34)
| 2028-03-31 | 2028-09-30  
Ruby 3.3 | ruby33 | 
* google-22 (default)
* google-22-full
| 
* [google-22/ruby33](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/ruby33)
* [google-22-full/ruby33](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/ruby33)
| 2027-03-31 | 2027-09-30  
Ruby 3.2 | ruby32 | 
* google-22 (default)
* google-22-full
| 
* [google-22/ruby32](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22/runtimes/ruby32)
* [google-22-full/ruby32](http://us-central1-docker.pkg.dev/serverless-runtimes/google-22-full/runtimes/ruby32)
| 2026-03-31 | 2026-09-30  
Ruby 3.0 | ruby30 |  google-18-full  |  [google-18-full/ruby30](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/ruby30) | 2024-03-31 | 2025-03-31  
Ruby 2.7 | ruby27 |  google-18-full  |  [google-18-full/ruby27](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/ruby27) | 2024-01-30 | 2025-01-30  
Ruby 2.6 | ruby26 |  google-18-full  |  [google-18-full/ruby26](http://us-central1-docker.pkg.dev/serverless-runtimes/google-18-full/runtimes/ruby26) | 2024-01-30 | 2025-01-30  
  
## Select your runtime

You can select one of the supported Ruby runtimes for your function during deployment. 

You can select a runtime version using the Google Cloud console, or the gcloud CLI. Click the tab for instructions on using the tool of your choice:

###  gcloud 

Specify the [Ruby base image](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images) for your function using the `--base-image` flag, while deploying your function. For example:
    
    
    gcloud run deploy FUNCTION \
        --source . \
        --function FUNCTION_ENTRYPOINT \
        --base-image ruby40
    

Replace:

  * FUNCTION with the name of the function you are deploying. You can omit this parameter entirely, but you will be prompted for the name if you omit it.

  * FUNCTION_ENTRYPOINT with the entry point to your function in your source code. This is the code Cloud Run executes when your function runs. The value of this flag must be a function name or fully-qualified class name that exists in your source code.




For detailed instructions on deploying a function using the gcloud CLI, see [Deploy functions in Cloud Run](https://docs.cloud.google.com/run/docs/deploy-functions#gcloud).

###  Console 

You can select a runtime version when you create or update a Cloud Run function in the Google Cloud console. For detailed instructions on deploying a function, see [Deploy functions in Cloud Run](https://docs.cloud.google.com/run/docs/deploy-functions#deploy-functions).

To select a runtime in the Google Cloud console when you create a function, follow these steps:

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Click **Write a function**.

  3. In the **Runtime** list, select a Ruby runtime version.

  4. Click **Create** , and wait for Cloud Run to create the service using a placeholder revision.

  5. The console will redirect you to the **Source** tab where you can see the source code of your function. Click **Save and redeploy**.




For detailed instructions on updating the runtime version after your function is deployed, see [Re-deploy new source code](https://docs.cloud.google.com/run/docs/deploy-functions#update-code-functions).

## Source code structure

For Cloud Run functions to find your function's definition, your source code must follow a specific structure. See [Write Cloud Run functions](https://docs.cloud.google.com/run/docs/write-functions#ruby) for more information.

## Specify dependencies

Cloud Run functions written in Ruby use [bundler](https://bundler.io) to access dependencies.

The [Functions Framework](https://github.com/GoogleCloudPlatform/functions-framework-ruby) is a required dependency for all functions. Although Cloud Run functions installs it on your behalf when the function is created, we recommend that you include it as an explicit dependency for clarity.

If your function relies on private dependencies, we recommend that you mirror `functions-framework` to your private registry. Include the mirrored `functions-framework` as a dependency to your function to avoid installing the package from the public internet.

Each function must provide a `Gemfile` that specifies the `functions_framework` gem, along with any additional gems needed by the function. `Gemfile` must be in the same directory as the `app.rb` file that contains your function code. In addition, your function must provide a lockfile that specifies all the transitive dependencies and their exact versions. This file, `Gemfile.lock`, is also located in the same directory alongside the `Gemfile`.

When you deploy your function, Cloud Run downloads and installs the dependencies declared in the `Gemfile` and `Gemfile.lock` using `bundler`.

The `Gemfile` lists the packages required by your function, along with any optional version constraints. For more details, see the [Gemfile reference](https://bundler.io/gemfile.html).

The following is an example `Gemfile`:
    
    
    source "https://rubygems.org"
    
    gem "functions_framework", "~> 0.7"
    gem "google-cloud-storage", "~> 1.29"
    

### Packaging local dependencies

You can also package and deploy dependencies alongside alongside your function. This approach is useful if your dependency is not available using the [rubygems package manager](https://rubygems.org/pages/download).

To package a gem locally, include it in a directory in your function's directory structure, and provide the path in the dependency's `Gemfile` entry. The gem directory must include a valid `gemspec` file, and it must be located within the function's directory hierarchy so that its code is deployed along with your function. For example, you might use a directory structure such as the following:
    
    
    myfunction/
    ├── Gemfile
    ├── Gemfile.lock
    ├── app.rb
    └── my_private_gem/
        ├── lib/
        |   └── my_private_gem.rb
        └── my_private_gem.gemspec
    

The `Gemfile` entry might look like this:
    
    
    source "https://rubygems.org"
    
    gem "functions_framework", "~> 0.7"
    gem "my_private_gem", path: "./my_private_gem"
    

See the [Gemfile reference](https://bundler.io/gemfile.html) for more discussion about referencing local gem paths.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

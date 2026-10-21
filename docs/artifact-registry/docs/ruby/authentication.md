---
url: https://docs.cloud.google.com/artifact-registry/docs/ruby/authentication/
title: Configure authentication to Artifact Registry for Ruby gem repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:24.478922+00:00
---

# Configure authentication to Artifact Registry for Ruby gem repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/ruby/authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Configure authentication to Artifact Registry for Ruby gem repositories Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure authentication with an Artifact Registry Ruby gem repository.

You must authenticate to Artifact Registry when you use a third-party application to connect to a repository.

You don't need to configure authentication for Cloud Build or Google Cloud runtime environments such as Google Kubernetes Engine and Cloud Run.

## Before you begin

  1. If the target repository doesn't exist, [create a Ruby gem repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).
  2. Verify that Ruby is installed. For installation instructions, see the Google Cloud [tutorial for setting up Ruby](https://docs.cloud.google.com/ruby/docs/setup).
  3. Verify that the user account or service account you are using has the required [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) to access the repository.
  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  5. (Optional) [Configure defaults for gcloud CLI commands](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults).



## Overview

Ruby supports two methods for authenticating requests to your Artifact Registry repository:

  * RubyGems CLI: Supports push and pull requests. This CLI is available with Ruby by default. When you authenticate with RubyGems, you must authenticate each time you make a push or pull request to your repository.
  * [Bundler](https://bundler.io/) CLI: Supports pull requests. Bundler stores packages and upstreams in a gemfile, which allows users to standardize setups across multiple machines without needing to authenticate each individual pull request. However, you must still reauthenticate your credentials to Bundler occasionally.

To install the Bundler CLI, enter `gem install bundler`.




## Generate tokens for authentication

To authenticate your package in Artifact Registry, you must first generate an authentication token. You can then use this token when you make requests from your package to Artifact Registry.

You can generate an `oauth2` access token using Google Cloud or an `oauth2l` token outside of Google Cloud.

Access tokens are valid for 60 minutes. Generate an access token shortly before running commands that interact with repositories. If your access token has expired, you must generate a new access token.

### Generate a token using gcloud

To generate an `oauth2` access token using Google Cloud, run the following command:
    
    
    export ACCESS_TOKEN="oauth2accesstoken:$(gcloud auth print-access-token)"
    

You can now reference `ACCESS_TOKEN` when you make requests from your Ruby package to Artifact Registry.

### Generate a token without using gcloud

To generate an access token using only the `oauth2l` CLI, do the following:

  1. Install the latest version of `oauth2l` by running the following command:
         
         go install github.com/google/oauth2l@latest
         

  2. Run the following command:
         
         export ACCESS_TOKEN="oauth2l fetch --scope cloud-platform"
         

Google Cloud generates an SHA256 hash token and stores it in the `ACCESS_TOKEN` variable. You can now reference `ACCESS_TOKEN` when you make requests from your Ruby package to Artifact Registry.




## Authenticate with the RubyGems CLI

The RubyGems CLI uses OAuth2 tokens to authenticate a request. To pass OAuth2 tokens to calls to your Artifact Registry repositories, you must pass your Oauth2 token with the address of your repository when you make a request. Tokens have a one-hour lifespan and must be refreshed hourly.

### Authenticate pull requests

You can authenticate a pull request in the Google Cloud CLI command line or by updating your `.gemrc` file.

#### Authenticate pull requests in the command line

To authenticate for the latest version of the gem in your pull request, run the following command:
    
    
    gem install GEM_NAME --source https://$ACCESS_TOKEN@LOCATION-ruby.pkg.dev/PROJECT/REPOSITORY
    

To authenticate for a specific gem version, add `-v GEM_VERSION` to the `gem install` command.

Where:

  * GEM_NAME is the name of the gem for which the request is made.
  * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for the repository.
  * PROJECT is the ID of the project containing the repository.
  * REPOSITORY is the ID of the repository.



#### Authenticate in a `.gemrc` file

You can configure your global or project-specific `/.gemrc` file to authenticate to your sources on pull requests by adding the following:
    
    
    # File: ~/.gemrc
    
    # Use the ACCESS_TOKEN retrieved from export ACCESS_TOKEN="oauth2accesstoken:$(gcloud auth print-access-token)"
    
    <...>
    :sources:
        - https://ACCESS_TOKEN@LOCATION-ruby.pkg.dev/PROJECT/REPOSITORY/
    <...>
    

Where:

  * ACCESS_TOKEN is your OAuth2 access token.
  * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for the repository.
  * PROJECT is the ID of the project containing the repository.
  * REPOSITORY is the ID of the repository.



To install a gem using the source or sources defined in your `/.gemrc` file, run:
    
    
    gem install GEM_NAME
    

### Authenticate push requests

You can authenticate a push request in the Google Cloud CLI command line or by updating your credentials file.

#### Authenticate push requests in the command line

To authenticate your push request, run the following command:
    
    
    export GEM_HOST_API_KEY="Bearer $(gcloud auth print-access-token)"
    gem push GEM_NAME --host https://LOCATION-ruby.pkg.dev/PROJECT/REPOSITORY
    

**Note:** After `GEM_HOST_API_KEY` has been defined, push requests don't need to pass the OAuth2 token in the URL.

Where:

  * GEM_NAME is the name of the gem for which the request is made.
  * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for the repository.
  * PROJECT is the ID of the project containing the repository.
  * REPOSITORY is the ID of the repository.



#### Authenticate push requests in a credentials file

The `gem` command line tool uses the `~/.gem/credentials` file to store API keys for pushing and pulling gems. To configure your credentials file to authenticate to your sources on push requests, do the following:

  1. Update your credentials file:

     1. Open `~/.gem/credentials` and add a line for your repository. The key is your repository URL, and the value is `Bearer`, followed by your token:
            
            :rubygems_api_key: RUBYGEMS_ORG_KEY
            https://LOCATION-ruby.pkg.dev/PROJECT/REPOSITORY: Bearer ACCESS_TOKEN
            

Where:

        * RUBYGEMS_ORG_KEY is the API key for `RubyGems.org`.
        * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for the repository.
        * PROJECT is the ID of the project containing the repository.
        * REPOSITORY is the ID of the repository.
        * ACCESS_TOKEN is your OAuth2 access token.
     2. Push your gem. Note that you don't need to set the `GEM_HOST_API_KEY`, as you have already defined the key in your credentials file.
            
            gem push GEM_NAME --host https://LOCATION-ruby.pkg.dev/PROJECT/REPOSITORY
            




## Authenticate with Bundler

The Ruby [Bundler](https://bundler.io/) manages application dependencies across one or more gems. To set up Bundler, do the following:

  1. Add the address of your repository as a `source` in your gemfile:
         
         # Gemfile
         # <...>
         source "https://LOCATION-ruby.pkg.dev/PROJECT/REPOSITORY"
         

  2. Authenticate to your repository by using `bundle config`:
         
         export GEM_TOKEN="oauth2accesstoken:$(gcloud auth print-access-token)"
         export HOST="https://LOCATION-ruby.pkg.dev/PROJECT/REPOSITORY"
         bundle config $HOST $GEM_TOKEN
         




Where:

  * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for the repository.
  * PROJECT is the project ID. If this flag is omitted, the current or [default project](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults#project) is used.
  * REPOSITORY is the ID of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) Artifact Registry repository, it is used when this flag is omitted from the command.



You will need to reauthenticate to your remote repository occasionally. In this event, run the same authentication command from Step 2.

For more information about configuring Bundler, see [Gemfiles](https://bundler.io/guides/gemfile.html) in the bundler.io documentation.

## What's next

  * [Configure access to repositories](https://docs.cloud.google.com/artifact-registry/docs/access-control)
  * [Learn about managing repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories)
  * [Learn about managing packages](https://docs.cloud.google.com/artifact-registry/docs/ruby/manage-packages)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

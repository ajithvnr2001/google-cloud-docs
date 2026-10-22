---
url: https://docs.cloud.google.com/artifact-registry/docs/ruby/store-ruby/
title: Quickstart: Store Ruby gems in Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:52.981609+00:00
---

# Quickstart: Store Ruby gems in Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/ruby/store-ruby/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Store Ruby gems in Artifact Registry

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This quickstart shows you how to set up a private Artifact Registry Ruby repository and then upload a package, also called a _gem_ , to that repository. 

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Artifact Registry API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com&redirect=https%3A//cloud.google.com/artifact-registry/docs/ruby/store-ruby)

  5. Make sure that you have the following role or roles on the project: Artifact Registry Administrator 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Artifact Registry API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com&redirect=https%3A//cloud.google.com/artifact-registry/docs/ruby/store-ruby)

  9. Make sure that you have the following role or roles on the project: Artifact Registry Administrator 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 




## Required roles

To get the permissions that you need to create and manage Artifact Registry Ruby gem repositories, ask your administrator to grant you the [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Launch Cloud Shell

In this quickstart, you will use [Cloud Shell](https://docs.cloud.google.com/shell/docs), which is a shell environment for managing resources hosted on Google Cloud.

Cloud Shell comes preinstalled with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) and Ruby. The gcloud CLI provides the primary command-line interface for Google Cloud.

Launch Cloud Shell:

  1. Go to Google Cloud console.

[Google Cloud console](https://console.cloud.google.com/)

  2. On the Google Cloud console toolbar, click **Activate Cloud Shell**.




A Cloud Shell session opens inside a frame lower on the console. You use this shell to run `gcloud` commands.

## Configure authentication

Ruby supports two methods for authenticating requests to your Artifact Registry repository:

  * RubyGems CLI: Supports push and pull requests. This CLI is available with Ruby by default. When you authenticate with RubyGems, you must authenticate each time you make a push or pull request to your repository.
  * [Bundler](https://bundler.io/) CLI: Supports pull requests. Bundler stores packages and upstreams in a gemfile, which allows users to standardize setups across multiple machines without needing to authenticate each individual pull request. However, you must still reauthenticate your credentials to Bundler occasionally.

To install the Bundler CLI, enter `gem install bundler`.




### Authenticate with the RubyGems CLI

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
            




### Authenticate with Bundler

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

For more information about authentication methods, see [Configure authentication to Artifact Registry for Ruby gem repositories](https://docs.cloud.google.com/artifact-registry/docs/ruby/authentication).

## Create a repository

Create the repository for your gem.

  1. Run the following command to create a new Ruby gem repository in the current project named `quickstart-ruby-repo` in the location `us-west1`.
         
         gcloud artifacts repositories create quickstart-ruby-repo \
             --repository-format=ruby \
             --location=us-west1 \
             --description="Ruby gem repository"
         

  2. Run the following command to verify that your repository was created:
         
         gcloud artifacts repositories list
         

  3. To simplify `gcloud` commands, set the default repository to `quickstart-ruby-repo` and the default location to `us-west1`. After the values are set, you don't need to specify them in `gcloud` commands that require a repository or a location.

To set the repository, run the following command:
         
         gcloud config set artifacts/repository quickstart-ruby-repo
         

To set the location, run the following command:
         
         gcloud config set artifacts/location us-west1
         

For more information about these commands, see the [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) documentation.




## Download a gem

When you build a Ruby project, distribution files are saved in a `lib` subdirectory in your Ruby project. To simplify this quickstart, you will create a directory and then download a gem to that directory.

To create the directory, run the following command:
    
    
    mkdir ruby-quickstart
    mkdir ruby-quickstart/lib
    cd ruby-quickstart/lib
    

Next, download your gem. You can either use your own gem or download a sample gem from the [Popular Gems page](https://rubygems.org/releases/popular) on rubygems.org. To download a gem from rubygems.org, run the following command:
    
    
    gem fetch GEM_NAME
    

You now have a gem titled GEM_NAME in your `ruby_quickstart/lib` directory. In the next section, you will use the RubyGems CLI to push your gem to your repository. 

## Push the gem to the repository

To push the gem to your repository, run the following command:
    
    
    gem push GEM_NAME --host https://us-west1-ruby.pkg.dev/PROJECT/quickstart-ruby-repo
    

Where:

  * GEM_NAME is the name of the gem to push to your repository.
  * PROJECT is the project ID. If this flag is omitted, then the current or [default project](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults#project) is used.



## View the gem in the repository

To verify that your gem was added, list the packages in the `ruby-quickstart` repository.

Run the following command:
    
    
    gcloud artifacts packages list --repository=ruby-quickstart
    

To view versions for a gem, run the following command:
    
    
    gcloud artifacts versions list --package=GEM_NAME
    

## Install the gem

To install the gem you just pushed to your Artifact Registry repository, run the following command:
    
    
    export GEM_TOKEN="oauth2accesstoken:$(gcloud auth print-access-token)"
    gem install GEM_NAME --source https://$GEM_TOKEN@us-west1-ruby.pkg.dev/PROJECT/quickstart-ruby-repo
    

Where:

  * GEM_NAME is the name of the gem to install in your repository.
  * PROJECT is the project ID. If this flag is omitted, then the current or [default project](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults#project) is used.



## Troubleshooting

See [Troubleshooting for Ruby gems](https://docs.cloud.google.com/artifact-registry/docs/ruby/troubleshooting) for more information.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

Before you remove the repository, ensure that any gems you want to keep are available in another location.

  1. To delete the `quickstart-ruby-repo` repository, run the following command:
         
         gcloud artifacts repositories delete quickstart-ruby-repo
         

  2. If you want to remove the default repository and location settings that you configured for the active `gcloud` configuration, run the following commands:
         
         gcloud config unset artifacts/repository
         gcloud config unset artifacts/location
         




## What's next

  * [Learn more about configuring authentication](https://docs.cloud.google.com/artifact-registry/docs/ruby/authentication)
  * [Learn about managing repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories)
  * [Learn about managing packages](https://docs.cloud.google.com/artifact-registry/docs/ruby/manage-packages)
  * Read our resources about [DevOps](https://docs.cloud.google.com/devops) and explore our [research program](https://www.devops-research.com/research.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

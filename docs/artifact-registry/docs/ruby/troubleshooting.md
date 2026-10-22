---
url: https://docs.cloud.google.com/artifact-registry/docs/ruby/troubleshooting/
title: Troubleshooting for Ruby gems \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:48.217231+00:00
---

# Troubleshooting for Ruby gems  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/ruby/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Troubleshooting for Ruby gems Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains why certain errors may occur when working with Ruby gems in an Artifact Registry repository, and possible remedies for those situations. 

## Expired push credentials

You made a push request but received the following error message:
    
    
    Pushing gem to https://LOCATION-ruby.pkg.devPROJECT/REPOSITORY..
    The request does not have valid authentication credentials.
    

To refresh your credentials, generate a new token by running the following command:
    
    
    export GEM_HOST_API_KEY="Bearer $(gcloud auth print-access-token)"
    export HOST="https://LOCATION-ruby.pkg.dev/PROJECT/REPOSITORY"
    bundle config $HOST $GEM_HOST_API_KEY
    

Where:

  * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for the repository.
  * PROJECT is the project ID. If this flag is omitted, then the current or [default project](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults#project) is used.
  * REPOSITORY is the ID of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) Artifact Registry repository, then that default repository is used when this flag is omitted from the command.



## Login prompt when pushing

You made a push request but received received a message requesting your `ruby.pkg.dev` credentials:
    
    
    Enter your https://us-ruby.pkg.dev/REPOSITORY/GEM_NAME credentials.
    Don't have an account yet? Create one at https://us-ruby.pkg.dev/REPOSITORY/GEM_NAME/sign_up
       Email:
    

Try running the following:
    
    
    GEM_HOST_API_KEY="Bearer $(gcloud auth print-access-token)"
    

## Expired pull credentials

You made a pull request but received the following error message:
    
    
     Unable to download data from https://oauth2accesstoken:REDACTED@LOCATION-ruby.pkg.dev/PROJECT/REPOSITORY/ - bad response Unauthorized 401 (https://oauth2accesstoken:REDACTED@LOCATION-ruby.pkg.dev/PROJECT/REPOSITORY/latest_specs.4.8.gz)
    

To refresh your credentials, remove the expired credential source from `gem sources`. Next, generate a new token by running the following command:
    
    
    export GEM_HOST_API_KEY="Bearer $(gcloud auth print-access-token)"
    export HOST="https://LOCATION-ruby.pkg.dev/PROJECT/REPOSITORY"
    bundle config $HOST $GEM_HOST_API_KEY
    

Where:

  * LOCATION is the location of your repository.
  * PROJECT is the project ID. If this flag is omitted, then the current or [default project](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults#project) is used.
  * REPOSITORY is the name of your repository in Artifact Registry.



## Pull request error: `Could not fetch specs`

You made a pull request but received the following error message:
    
    
    Retrying fetcher due to error (2/4): Bundler::HTTPError Could not fetch specs from https://LOCATION-ruby.pkg.dev/PROJECT/REPOSITORY/ due to underlying error <bad response Not Found 404 (https://LOCATION-ruby.pkg.dev/PROJECT/REPOSITORY/specs.4.8.gz)>
    

This error may incorrectly appear even though the pull request was successful. Use a `verbose` command to verify that your pull request succeeded, such as `bundle install --verbose`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

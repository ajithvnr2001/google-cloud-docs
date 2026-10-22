---
url: https://docs.cloud.google.com/appengine/docs/flexible/dotnet/runtime/
title: The .NET runtime \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:57.010678+00:00
---

# The .NET runtime  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/dotnet/runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  The .NET runtime Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Some [.NET runtimes](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#net) have reached [end of support](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/runtime-lifecycle#end_of_support). You cannot re-deploy versions that use runtimes after their end of support date. We recommend that you [upgrade your app](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/runtime#newversions) to use the latest version of .NET. 

The .NET runtime is the software stack responsible for installing your application code and dependencies, and then running that application in the flexible environment.

## .NET versions

.NET 10 is built using [buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview). For the full list of supported .NET versions, and their corresponding Ubuntu version, see the [Runtime support schedule](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#net).

To use a [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#net) .NET version, you must:

  * Update your project file with the .NET version you want to use.
        
        <Project Sdk="Microsoft.NET.Sdk.Web">
        
          <PropertyGroup>
            <TargetFramework>net10.0</TargetFramework>
            <Nullable>enable</Nullable>
            <ImplicitUsings>enable</ImplicitUsings>
          </PropertyGroup>
        
          <ItemGroup>
            <None Update="app.yaml">
              <CopyToPublishDirectory>PreserveNewest</CopyToPublishDirectory>
            </None>
          </ItemGroup>
        
        </Project>
        

  * Install gcloud CLI version **420.0.0 or later**. You can update your CLI tooling by running the [gcloud components update](https://docs.cloud.google.com/sdk/gcloud/reference/components/update) command. To view your installed version, you can run the [gcloud version](https://docs.cloud.google.com/sdk/gcloud/reference/version) command.

  * Specify the `operating_system` setting in your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml) file:
        
        runtime: aspnetcore
          env: flex
        
          runtime_config:
              operating_system: "ubuntu24"
        

  * Optionally, you can specify a runtime version by including the `runtime_version` setting in your `app.yaml` file. By default, App Engine uses the latest available LTS .NET version if the `runtime_version` setting is not specified. For example, the `app.yaml` file looks as follows when specifying .NET 10 on Ubuntu 24:
        
        runtime: aspnetcore
          env: flex
        
          runtime_config:
              runtime_version: "10"
              operating_system: "ubuntu24"
        




## Previous runtime versions

**Warning:** .NET **version 3 and earlier** have reached end of support. App Engine blocks you from deploying your applications using runtimes that have reached end of support. We recommend that you migrate your app to use a [supported version](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#net) of .NET or use a [custom runtime](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/about-custom-runtimes).

To target a specific .NET SDK version, update your project file. For more information, see [Migrate from ASP.NET Core 3.1 to 6.0](https://learn.microsoft.com/en-us/aspnet/core/migration/31-to-60?view=aspnetcore-6.0&tabs=visual-studio.).

If you want to use GKE or other Docker hosts, you need to create a Dockerfile that copies your application code and installs dependencies. For more information, see [Custom Runtimes](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes).

To deploy your .NET app, run the following commands from the root directory where your app resides:
    
    
        dotnet restore
        dotnet publish -c Release
        gcloud app deploy
    

## Support for other .NET runtimes

If you need to use a .NET version that isn't [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#net), you can create a [custom runtime](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/build) and select a valid base image with the .NET version you need.

For Google-supplied base images or [Docker .NET base images](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/docker/building-net-docker-images?view=aspnetcore-8.0), see [Building custom runtimes](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/build#base).

## HTTPS and forwarding proxies

App Engine terminates the HTTPS connection at the load balancer and forwards the request to your application. Applications can examine the `X-Forwarded-Proto` to observe whether the original protocol was HTTP or HTTPS.

Some applications also need to ascertain the user's IP address. This is available in the standard `X-Forwarded-For` header.

## Extending the runtime

The flexible environment .NET runtime can be used to create a custom runtime. Custom runtimes are configured via a `Dockerfile`.

You can customize the `Dockerfile` and `.dockerignore` as desired. Finally, you will need to specify `runtime: custom` instead of `runtime: aspnetcore` in `app.yaml`. See [Customizing the .NET Runtime](https://docs.cloud.google.com/appengine/docs/flexible/dotnet/customizing-the-dotnet-runtime) for more information.

## Environment variables

The following environment variables are set by the runtime environment:

Environment variable | Description  
---|---  
`GAE_INSTANCE` | The name of the current instance.  
`GAE_MEMORY_MB` | The amount of memory available to the application process.  
`GAE_SERVICE` | The service name specified in your application's `app.yaml` file, or if no service name is specified, it is set to `default`.  
`GAE_VERSION` | The version label of the current application.  
`GOOGLE_CLOUD_PROJECT` | The Project ID associated with your application, which is visible in the Google Cloud console  
`PORT` | The port that will receive HTTP requests.  
  
You can set additional configuration variables with `appsettings.json`.

## Metadata server

Each instance of your application can use the [Compute Engine metadata server](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata) to query information about the instance, including its host name, external IP address, instance ID, custom metadata, and service account information. App Engine does not allow you to set custom metadata for each instance, but you can set [project-wide custom metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#projectwide) and read it from your App Engine and Compute Engine instances.

This example function uses the metadata server to get the external IP address of the instance:
    
    
    var client = new HttpClient();
    client.DefaultRequestHeaders.Add("Metadata-Flavor", new[] { "Google" });
    response = await client.GetStringAsync(
        "http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/0/access-configs/0/external-ip");
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

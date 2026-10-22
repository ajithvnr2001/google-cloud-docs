---
url: https://docs.cloud.google.com/error-reporting/docs/setup/kubernetes-engine/
title: Setting up on Google Kubernetes Engine \u00a0|\u00a0 Error Reporting \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:03.227805+00:00
---

# Setting up on Google Kubernetes Engine  |  Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/docs/setup/kubernetes-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Guides ](https://docs.cloud.google.com/error-reporting/docs/grouping-errors)



Send feedback 

#  Setting up on Google Kubernetes Engine Stay organized with collections  Save and categorize content based on your preferences. 

Error Reporting lets you aggregate crashes and diagnose runtime exceptions from your Google Kubernetes Engine applications. You can send error data by streaming logs to Cloud Logging or by calling the Error Reporting API directly. If you use Logging, then your log entries must follow the [formatting requirements](https://docs.cloud.google.com/error-reporting/docs/formatting-error-messages).

## Using Logging to report errors

GKE's default logging agent provides a managed solution to deploy and manage the agents that send the logs for your clusters to Cloud Logging. The structure of the agent depends on the version of the cluster. For information about this agent, see [Managing GKE logs](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/managing-logs).

Error Reporting requires that exceptions or stack traces be contained in a single log entry. Most logging agents are capable of recognizing that several log lines—stack frames printed each on a new line—represent a stack trace and send it to Cloud Logging as a single log entry. If the agent isn't capable of reconstructing multiple lines as a single error, then use the [`projects.events.report` API endpoint](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report), which lets you to control the contents of an error.

## Using the Error Reporting API to write errors

The Error Reporting API provides a `report` endpoint for writing error information to the service.

  1. Enable the Error Reporting API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=clouderrorreporting.googleapis.com)

  2. Report errors to the API using either the REST API or a client library.

     * REST API

See the [reference documentation](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report) for information about the API.

     * Using client libraries

Libraries exist in a limited number of languages to help you call the Error Reporting API from your application:

       * [ASP.NET](https://docs.cloud.google.com/error-reporting/docs/setup/dotnet)
       * [Go](https://docs.cloud.google.com/error-reporting/docs/setup/go)
       * [Java](https://docs.cloud.google.com/error-reporting/docs/setup/java)
       * [Node.js](https://docs.cloud.google.com/error-reporting/docs/setup/nodejs)
       * [Ruby](https://docs.cloud.google.com/error-reporting/docs/setup/ruby)
       * [Python](https://docs.cloud.google.com/error-reporting/docs/setup/python)
       * [PHP](https://docs.cloud.google.com/error-reporting/docs/setup/php)



### Samples

###  ASP.NET 

The ASP.NET NuGet package reports uncaught exceptions from ASP.NET web applications to Error Reporting.

### Install the NuGet package

To install the Stackdriver ASP.NET NuGet package in Visual Studio:

  1. Right-click your solution and select **Manage NuGet packages for solution**.
  2. Select the **Include prerelease** checkbox.
  3. Search for and install the package named `Google.Cloud.Diagnostics.AspNet`.



### Usage

Once you've installed the Stackdriver ASP.NET NuGet package, add the following statement to your application code to start sending errors to Stackdriver:
    
    
    using Google.Cloud.Diagnostics.AspNet;
    

Add the following `HttpConfiguration` code to the `Register` method of your .NET web app after replacing `your-project-id` with your actual [project ID](https://support.google.com/cloud/answer/6158840) to enable the reporting of exceptions:
    
    
    public static void Register(HttpConfiguration config)
    {
        string projectId = "YOUR-PROJECT-ID";
        string serviceName = "NAME-OF-YOUR-SERVICE";
        string version = "VERSION-OF-YOUR-SERVCICE";
        // ...
        // Add a catch all for the uncaught exceptions.
        config.Services.Add(typeof(IExceptionLogger),
            ErrorReportingExceptionLogger.Create(projectId, serviceName, version));
        // ...
    }
    

Once you've added this method to your ASP.NET application, you can view any uncaught exceptions that occur as they get reported to Google Cloud in the [Error Reporting](https://console.cloud.google.com/errors) section of the Google Cloud console.

###  C# 

The following example can be found in the [GoogleCloudPlatform/dotnet-docs-samples](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/tree/vs2015) repository. To use it, after building the project, specify your [project ID](https://support.google.com/cloud/answer/6158840):
    
    
    C:\...\bin\Debug> set GOOGLE_PROJECT_ID=[YOUR_PROJECT_ID]
    

Make sure to replace `[YOUR_PROJECT_ID]` with the correct value from the Google Cloud console.

Then, send exception data with code similar to the following:
    
    
    public class ErrorReportingSample
    {
        public static void Main(string[] args)
        {
            try
            {
                throw new Exception("Generic exception for testing Stackdriver Error Reporting");
            }
            catch (Exception e)
            {
                report(e);
                Console.WriteLine("Stackdriver Error Report Sent");
            }
        }
    
        /// <summary>
        /// Create the Error Reporting service (<seealso cref="ClouderrorreportingService"/>)
        /// with the Application Default Credentials and the proper scopes.
        /// See: https://developers.google.com/identity/protocols/application-default-credentials.
        /// </summary>
        private static ClouderrorreportingService CreateErrorReportingClient()
        {
            // Get the Application Default Credentials.
            GoogleCredential credential = GoogleCredential.GetApplicationDefaultAsync().Result;
    
            // Add the needed scope to the credentials.
            credential.CreateScoped(ClouderrorreportingService.Scope.CloudPlatform);
    
            // Create the Error Reporting Service.
            ClouderrorreportingService service = new ClouderrorreportingService(new BaseClientService.Initializer
            {
                HttpClientInitializer = credential,
            });
            return service;
        }
    
        /// <summary>
        /// Creates a <seealso cref="ReportRequest"/> from a given exception.
        /// </summary>
        private static ReportRequest CreateReportRequest(Exception e)
        {
            // Create the service.
            ClouderrorreportingService service = CreateErrorReportingClient();
    
            // Get the project ID from the environement variables.
            string projectId = Environment.GetEnvironmentVariable("GOOGLE_PROJECT_ID");
    
            // Format the project id to the format Error Reporting expects. See:
            // https://cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report
            string formattedProjectId = string.Format("projects/{0}", projectId);
    
            // Add a service context to the report.  For more details see:
            // https://cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events#ServiceContext
            ServiceContext serviceContext = new ServiceContext()
            {
                Service = "myapp",
                Version = "8c1917a9eca3475b5a3686d1d44b52908463b989",
            };
            ReportedErrorEvent errorEvent = new ReportedErrorEvent()
            {
                Message = e.ToString(),
                ServiceContext = serviceContext,
            };
            return new ReportRequest(service, errorEvent, formattedProjectId);
        }
    
        /// <summary>
        /// Report an exception to the Error Reporting service.
        /// </summary>
        private static void report(Exception e)
        {
            // Create the report and execute the request.
            ReportRequest request = CreateReportRequest(e);
            request.Execute();
        }
    }

###  Go 

See [Setting up Error Reporting for Go](https://docs.cloud.google.com/error-reporting/docs/setup/go).

###  Java 

See [Setting up Error Reporting for Java](https://docs.cloud.google.com/error-reporting/docs/setup/java).

###  Node.js 

See [Setting up Error Reporting for Node.js](https://docs.cloud.google.com/error-reporting/docs/setup/nodejs).

###  Ruby 

See [Setting up Error Reporting for Ruby](https://docs.cloud.google.com/error-reporting/docs/setup/ruby).

###  Python 

See [Setting up Error Reporting for Python](https://docs.cloud.google.com/error-reporting/docs/setup/python).

###  PHP 

See [Setting up Error Reporting for PHP](https://docs.cloud.google.com/error-reporting/docs/setup/php).

## View error groups

In the Google Cloud console, go to the **Error Reporting** page: 

[Go to **Error Reporting**](https://console.cloud.google.com/errors)

You can also find this page by using the search bar.

**Note** : If you see the message "Set up Error Reporting" on the **Error Reporting** page, then your Google Cloud project has no error groups to display.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 

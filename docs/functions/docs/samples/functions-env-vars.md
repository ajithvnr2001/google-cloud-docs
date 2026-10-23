---
url: https://docs.cloud.google.com/functions/docs/samples/functions-env-vars/
title: Environment variables \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:50.004927+00:00
---

# Environment variables  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-env-vars/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Environment variables Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to use environment variables within a Cloud Function.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configure environment variables (1st gen)](https://docs.cloud.google.com/functions/1stgendocs/configuring/env-var)



## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Google.Cloud.Functions.Framework;
    using Microsoft.AspNetCore.Http;
    using System;
    using System.Threading.Tasks;
    
    namespace EnvironmentVariables;
    
    public class Function : IHttpFunction
    {
        public async Task HandleAsync(HttpContext context)
        {
            string foo = Environment.GetEnvironmentVariable("FOO")
                ?? "Specified environment variable is not set.";
            await context.Response.WriteAsync(foo, context.RequestAborted);
        }
    }

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package tips contains tips for writing Cloud Functions in Go.
    package tips
    
    import (
    	"fmt"
    	"net/http"
    	"os"
    )
    
    // EnvVar is an example of getting an environment variable in a Go function.
    func EnvVar(w http.ResponseWriter, r *http.Request) {
    	fmt.Fprintf(w, "FOO: %q", os.Getenv("FOO"))
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import java.io.BufferedWriter;
    import java.io.IOException;
    
    public class EnvVars implements HttpFunction {
    
      // Returns the environment variable "foo" set during function deployment.
      @Override
      public void service(HttpRequest request, HttpResponse response)
          throws IOException {
        BufferedWriter writer = response.getWriter();
        String foo = System.getenv("FOO");
        if (foo == null) {
          foo = "Specified environment variable is not set.";
        }
        writer.write(foo);
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    exports.envVar = (req, res) => {
      // Sends 'bar' as response
      res.send(process.env.FOO);
    };

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Psr\Http\Message\ServerRequestInterface;
    
    function envVar(ServerRequestInterface $request): string
    {
        return getenv('FOO') . PHP_EOL;
    }
    

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import os
    
    
    def env_vars(request):
        return os.environ.get("FOO", "Specified environment variable is not set.")
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "functions_framework"
    
    FunctionsFramework.http "env_vars" do |_request|
      ENV["FOO"] || "Specified environment variable is not set."
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

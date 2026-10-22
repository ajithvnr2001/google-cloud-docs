---
url: https://docs.cloud.google.com/functions/docs/samples/functions-concepts-filesystem/
title: File system \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:23.342467+00:00
---

# File system  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-concepts-filesystem/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  File system Stay organized with collections  Save and categorize content based on your preferences. 

Shows how to access a Cloud Functions instance's file system.

## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Google.Cloud.Functions.Framework;
    using Microsoft.AspNetCore.Http;
    using System.IO;
    using System.Threading.Tasks;
    
    namespace FileSystem;
    
    public class Function : IHttpFunction
    {
        public async Task HandleAsync(HttpContext context)
        {
            string[] files = Directory.GetFiles(".");
    
            await context.Response.WriteAsync("Files:\n", context.RequestAborted);
            foreach (string file in files)
            {
                await context.Response.WriteAsync($"\t{file}\n", context.RequestAborted);
            }
        }
    }

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package tips contains tips for writing Cloud Functions in Go.
    package tips
    
    import (
    	"fmt"
    	"log"
    	"net/http"
    	"os"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    )
    
    func init() {
    	functions.HTTP("ListFiles", ListFiles)
    }
    
    // ListFiles lists the files in the current directory.
    // Uses directory "serverless_function_source_code" as defined in the Go
    // Functions Framework Buildpack.
    // See https://github.com/GoogleCloudPlatform/buildpacks/blob/56eaad4dfe6c7bd0ecc4a175de030d2cfab9ae1c/cmd/go/functions_framework/main.go#L38.
    func ListFiles(w http.ResponseWriter, r *http.Request) {
    	files, err := os.ReadDir("./serverless_function_source_code")
    	if err != nil {
    		http.Error(w, "Unable to read files", http.StatusInternalServerError)
    		log.Printf("ListFiles: %v", err)
    		return
    	}
    	fmt.Fprintln(w, "Files:")
    	for _, f := range files {
    		fmt.Fprintf(w, "\t%v\n", f.Name())
    	}
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.HttpFunction;
    import com.google.cloud.functions.HttpRequest;
    import com.google.cloud.functions.HttpResponse;
    import java.io.File;
    import java.io.IOException;
    import java.io.PrintWriter;
    
    public class FileSystem implements HttpFunction {
    
      // Lists the files in the current directory.
      @Override
      public void service(HttpRequest request, HttpResponse response)
          throws IOException {
        File currentDirectory = new File(".");
        File[] files = currentDirectory.listFiles();
        PrintWriter writer = new PrintWriter(response.getWriter());
        writer.println("Files:");
        for (File f : files) {
          writer.printf("\t%s%n", f.getName());
        }
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const fs = require('fs');
    const functions = require('@google-cloud/functions-framework');
    
    /**
     * HTTP Cloud Function that lists files in the function directory
     *
     * @param {Object} req Cloud Function request context.
     * @param {Object} res Cloud Function response context.
     */
    functions.http('listFiles', (req, res) => {
      fs.readdir(__dirname, (err, files) => {
        if (err) {
          console.error(err);
          res.sendStatus(500);
        } else {
          console.log('Files', files);
          res.sendStatus(200);
        }
      });
    });

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Psr\Http\Message\ServerRequestInterface;
    
    function listFiles(ServerRequestInterface $request): string
    {
        $contents = scandir(__DIR__);
    
        $output = 'Files:' . PHP_EOL;
    
        foreach ($contents as $file) {
            $output .= "\t" . $file . PHP_EOL;
        }
    
        return $output;
    }
    

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import functions_framework
    
    
    @functions_framework.http
    def list_files(request):
        import os
        from os import path
    
        root = path.dirname(path.abspath(__file__))
        children = os.listdir(root)
        files = [c for c in children if path.isfile(path.join(root, c))]
        return f"Files: {files}"
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "functions_framework"
    
    FunctionsFramework.http "concepts_filesystem" do |_request|
      files = Dir.entries "."
      "Files: #{files.join "\n"}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 

---
url: https://docs.cloud.google.com/functions/1stgendocs/configuring/env-var/
title: Configure environment variables (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:39.309787+00:00
---

# Configure environment variables (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/configuring/env-var/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure environment variables (1st gen)

You can deploy arbitrary key/value pairs alongside a Cloud Run function. These pairs are made available to your function either as literal [environment variables](https://wikipedia.org/wiki/Environment_variable), accessible by your code at runtime, or as configuration information for [Google Cloud's buildpacks](https://docs.cloud.google.com/docs/buildpacks/service-specific-configs).

Environment variables are bound to a single function and are not visible to other functions in your Google Cloud project. Each variable is stored in the Cloud Run functions backend and exist within the same lifecycle as the function to which they are bound.

You can add or remove runtime environment variables using either the Google Cloud CLI or the Google Cloud console.

### Setting runtime environment variables

Use these methods to establish new variables or completely replace existing variables. To make additive changes, use the update process described in the next section.

###  gcloud 

To set a runtime environment variable using the Google Cloud CLI, use the `--set-env-vars` flag at deploy time:
    
    
    gcloud functions deploy --no-gen2 FUNCTION_NAME --set-env-vars FOO=bar FLAGS ...

You can also set multiple runtime environment variables using a comma separated list:
    
    
    gcloud functions deploy --no-gen2 FUNCTION_NAME --set-env-vars FOO=bar,BAZ=boo FLAGS...

If you want to store your configuration in a file (e.g. under source control), you can use a YAML file together with the `--env-vars-file` flag:
    
    
    gcloud functions deploy --no-gen2 FUNCTION_NAME --env-vars-file .env.yaml FLAGS...

where the contents of the `.env.yaml` file are:
    
    
     FOO: bar
     BAZ: boo
    

In the above examples, `FLAGS...` refers to other options that you pass during deployment of your function. For a complete reference for the `deploy` command, see [`gcloud functions deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy).

###  Google Cloud console UI 

You can set runtime environment variables during function creation in the Google Cloud console:

  1. Open the Functions Overview page in the Google Cloud console:

[Go to the Cloud Run functions Overview page](https://console.cloud.google.com/functions/list).

  2. Click **Create function**.

  3. Fill in the required fields for your function.

  4. Open the **Runtime, build and connections settings** section.

  5. Select the **Runtime** tab.

  6. In the **Runtime environment variables** section, click **Add variable** and add the name and value.

For instructions on how to add environment variables to an existing function, see Updating runtime environment variables.




### Updating runtime environment variables

You can also update runtime environment variables for existing functions. This is a non-destructive approach that changes or adds runtime environment variables, but does not delete.

###  gcloud 

To update a variable using the Google Cloud CLI, use the `--update-env-vars` flag at deploy time:
    
    
    gcloud functions deploy FUNCTION_NAME --no-gen2 --update-env-vars FOO=bar

You can also update multiple runtime environment variables using a comma separated list:
    
    
    gcloud functions deploy FUNCTION_NAME --no-gen2 --update-env-vars FOO=bar,BAZ=boo

###  Google Cloud console UI 

To update runtime environment variables using the Google Cloud console:

  1. Open the Functions Overview page in the Google Cloud console:

[Go to the Cloud Run functions Overview page](https://console.cloud.google.com/functions/list).

  2. Click an existing function to go to its details page.

  3. Click **Edit**.

  4. Open the **Runtime, build and connections settings** section.

  5. Select the **Runtime** tab.

  6. Make your edits in the **Runtime environment variables** section.




### Deleting runtime environment variables

###  gcloud 

If you want to selectively remove runtime environment variables you can use the `--remove-env-vars` flag at deploy time:
    
    
    gcloud functions deploy FUNCTION_NAME --no-gen2 --remove-env-vars FOO,BAZ

Alternatively, you can clear all previously set runtime environment variables with the `--clear-env-vars` flag:
    
    
    gcloud functions deploy FUNCTION_NAME --no-gen2 --clear-env-vars

###  Google Cloud console UI 

To delete runtime environment variables using the Google Cloud console:

  1. Open the Functions Overview page in the Google Cloud console:

[Go to the Cloud Run functions Overview page](https://console.cloud.google.com/functions/list).

  2. Click an existing function to go to its details page.

  3. Click **Edit**.

  4. Open the **Runtime, build and connections settings** section.

  5. Select the **Runtime** tab.

  6. In the **Runtime environment variables** section, click the garbage icon next to the key/value pair to delete it.




### Runtime environment variables set automatically

This section lists runtime environment variables that are set automatically.

Key | Description  
---|---  
`FUNCTION_TARGET` | Reserved: The function to be executed.  
`FUNCTION_SIGNATURE_TYPE` | Reserved: The type of the function: `http` for HTTP functions, and `event` for event-driven functions.   
`K_SERVICE` | Reserved: The name of the function resource.  
`K_REVISION` | Reserved: The version identifier of the function.  
`PORT` | Reserved: The port over which the function is invoked.  
**Note:** If your function requires one of the environment variables from an older runtime, you can set the variable when deploying your function. For example:
    
    
    gcloud functions deploy envVarMemory \
    --no-gen2 \
    --runtime nodejs10 \
    --set-env-vars FUNCTION_MEMORY_MB=2Gi \
    --memory 2Gi \
    --trigger-http
    

### Setting and retrieving runtime environment variables: an example

Set the runtime environment variable:

###  Node.js 
    
    
    gcloud functions deploy envVar \
    --runtime nodejs22 \
    --set-env-vars FOO=bar \
    --trigger-http

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Node.js version](https://docs.cloud.google.com/static/functions/docs/runtime-support#node.js) to run your function. 

###  Python 
    
    
    gcloud functions deploy env_vars \
    --runtime python312 \
    --set-env-vars FOO=bar \
    --trigger-http

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Python version](https://docs.cloud.google.com/functions/docs/runtime-support#python) to run your function. 

###  Go 
    
    
    gcloud functions deploy EnvVar \
    --runtime go121 \
    --set-env-vars FOO=bar \
    --trigger-http

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Go version](https://docs.cloud.google.com/functions/docs/runtime-support#go) to run your function. 

###  Java 
    
    
    gcloud functions deploy java-envVar-function \
    --entry-point functions.EnvVars \
    --runtime java17 \
    --memory 512MB \
    --set-env-vars FOO=bar \
    --trigger-http

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Java version](https://docs.cloud.google.com/functions/docs/runtime-support#java) to run your function. 

###  C# 
    
    
    gcloud functions deploy csharp-envVar-function \
    --entry-point EnvironmentVariables.Function \
    --runtime dotnet6 \
    --set-env-vars FOO=bar \
    --trigger-http
    

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported .NET version](https://docs.cloud.google.com/functions/docs/runtime-support#.net-core) to run your function. 

###  Ruby 
    
    
    gcloud functions deploy env_vars --runtime ruby33 \
    --set-env-vars FOO=bar \
    --trigger-http

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Ruby version](https://docs.cloud.google.com/functions/docs/runtime-support#ruby) to run your function. 

###  PHP 
    
    
     gcloud functions deploy envVar --runtime php82 \
    --set-env-vars FOO=bar \
    --trigger-http

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported PHP version](https://docs.cloud.google.com/functions/docs/runtime-support#php) to run your function. 

At runtime access the variables programmatically:

###  Node.js 

In Node.js use the `process.env` property to access runtime environment variables:
    
    
    exports.envVar = (req, res) => {
      // Sends 'bar' as response
      res.send(process.env.FOO);
    };

###  Python 

In Python use `os.environ` to access runtime environment variables:
    
    
    import os
    
    
    def env_vars(request):
        return os.environ.get("FOO", "Specified environment variable is not set.")
    
    

###  Go 

In Go use `os.Getenv()` to access runtime environment variables:
    
    
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
    

###  Java 

In Java use `System.getenv` to access runtime environment variables:
    
    
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

###  C# 

At runtime, environment variables are accessible using `Environment.GetEnvironmentVariable` in C#: 
    
    
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

###  Ruby 

At runtime, environment variables are accessible using `ENV` in Ruby: 
    
    
    require "functions_framework"
    
    FunctionsFramework.http "env_vars" do |_request|
      ENV["FOO"] || "Specified environment variable is not set."
    end

###  PHP 

At runtime, environment variables are accessible using PHP's `getenv` function: 
    
    
    use Psr\Http\Message\ServerRequestInterface;
    
    function envVar(ServerRequestInterface $request): string
    {
        return getenv('FOO') . PHP_EOL;
    }

## Using build environment variables

You can also set build environment variables for runtimes that support [buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview).

Build environment variables are key/value pairs deployed alongside a function that let you pass configuration information to buildpacks. For example, you might want to customize compiler options. You can add or remove these build environment variables using either the Google Cloud CLI or the Google Cloud console UI.

**Note:** Keys must start with an uppercase ASCII letter, and consist of uppercase ASCII letters, digits, and underscores. You should avoid creating variable keys with a `GOOGLE_*` prefix. [View all supported buildpacks environment variables](https://docs.cloud.google.com/docs/buildpacks/service-specific-configs). 

### Setting build environment variables

Use these methods to establish new variables or completely replace existing variables. To make additive changes, use the update process (the `--update-build-env-vars` flag in `gcloud`) described in the next section.

###  gcloud 

To set a variable using the Google Cloud CLI, use the `--set-build-env-vars` flag at deploy time:
    
    
    gcloud beta functions deploy FUNCTION_NAME --no-gen2 --set-build-env-vars FOO=bar FLAGS...

You can also set multiple build environment variables using a comma separated list:
    
    
    gcloud functions deploy FUNCTION_NAME --no-gen2 --set-build-env-vars FOO=bar,BAZ=boo FLAGS...

If you want to store your configuration in a file (e.g. under source control), you can use a YAML file together with the `--build-env-vars-file` flag:
    
    
    gcloud functions deploy FUNCTION_NAME --no-gen2 --build-env-vars-file FILE_NAME.yaml FLAGS...

where the contents of the `*.yaml` file are:
    
    
     FOO: bar
     BAZ: boo
    

In the above examples, `FLAGS...` refers to other options that you pass during deployment of your function. For a complete reference for the `deploy` command, see [`gcloud beta functions deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/functions/deploy).

###  Google Cloud console UI 

You can also set build environment variables during function creation in the Google Cloud console:

  1. Open the Functions Overview page in the Google Cloud console:

[Go to the Cloud Run functions Overview page](https://console.cloud.google.com/functions/list).

  2. Click **Create function**.

  3. Fill in the required fields for your function.

  4. Open the **Runtime, build and connections settings** section.

  5. Select the **Build** tab.

  6. In the **Build environment variables** section, click **Add variable** and add the name and value.




### Updating build environment variables

You can also update build environment variables for existing functions. This is a non-destructive approach that changes or adds build environment variables, but does not delete.

###  gcloud 

To set a variable using the Google Cloud CLI, use the `--update-build-env-vars` flag at deploy time:
    
    
    gcloud functions deploy FUNCTION_NAME --no-gen2 --update-build-env-vars FOO=bar

You can also update multiple build environment variables using a comma separated list:
    
    
    gcloud functions deploy FUNCTION_NAME --no-gen2 --update-build-env-vars FOO=bar,BAZ=boo

###  Google Cloud console UI 

To update build environment variables using the Google Cloud console:

  1. Open the Functions Overview page in the Google Cloud console:

[Go to the Cloud Run functions Overview page](https://console.cloud.google.com/functions/list).

  2. Click an existing function to go to its details page.

  3. Click **Edit**.

  4. Open the **Runtime, build and connections settings** section.

  5. Select the **Build** tab.

  6. Make your edits in the **Build environment variables** section.




### Deleting build environment variables

###  gcloud 

If you want to selectively remove build environment variables you can use the `--remove-build-env-vars` flag at deploy time:
    
    
    gcloud functions deploy FUNCTION_NAME --no-gen2 --remove-build-env-vars FOO,BAZ

Alternatively, you can clear all previously set build environment variables with the `--clear-build-env-vars` flag:
    
    
    gcloud functions deploy FUNCTION_NAME --no-gen2 --clear-build-env-vars

###  Google Cloud console UI 

To delete build environment variables using the Google Cloud console:

  1. Open the Functions Overview page in the Google Cloud console:

[Go to the Cloud Run functions Overview page](https://console.cloud.google.com/functions/list).

  2. Click an existing function to go to its details page.

  3. Click **Edit**.

  4. Open the **Runtime, build and connections settings** section.

  5. Select the **Build** tab.

  6. In the **Build environment variables** section, click the garbage icon next to the key/value pair to delete it.




## Variable lifecycle

All environment variables are bound to a deployment of a Cloud Run function, and can only be set or changed with a deployment. If a deployment fails for any reason, any changes to environment variables will _not_ be applied. Environment variable changes require a successful deployment.

## Best practices and reserved environment variables

Some additional environment variables are automatically set depending on the runtime your function uses. These are based on the runtime's operating system (for example, `DEBIAN_FRONTEND`, `SHLVL`, or `PATH`) and the language runtime (for example, `NODE_ENV`, `VIRTUAL_ENV`, or `GOPATH`).

Environment variables that are provided by the environment (other than the ones listed in Environment variables set automatically) might change in future runtime versions. As a best practice, we recommend that you do not depend on or modify any environment variables that you have not set explicitly.

Modifying environment variables that are provided by the environment might lead to unpredictable outcomes. Attempts to modify such environment variables could be blocked or, worse, lead to unintended consequences such as functions that cannot start. As a best practice, consider prefixing any environment variables with a unique key to avoid conflicts.

Finally, you cannot use the following environment variables:

Key | Description  
---|---  
Empty ('') | Keys cannot be an empty string.  
`=` | Keys cannot contain the '=' character.  
`X_GOOGLE_` | Keys cannot contain the prefix `X_GOOGLE_`.  
**Note:** Environment variables that appear in the execution environment but that are not documented in the above table should be considered deprecated and might disappear at any time without notice.

### Size limits

The total number of bytes used by runtime environment variable names and values for an individual function is limited to 32KiB. There are no specific limits on individual keys or values within this overall capacity.

For build environment variables, up to 100 variables can be defined, with the definition string `foo=bar` limited to 64KiB.

### Managing secrets

Environment variables can be used for function configuration, but are not recommended as a way to store secrets such as database credentials or API keys. These more sensitive values should be stored outside both your source code and outside environment variables. Some execution environments or the use of some frameworks can result in the contents of environment variables being sent to logs, and storing sensitive credentials in YAML files, deployment scripts or under source control is not recommended.

For storing secrets, we recommend that you use Secret Manager. To configure Cloud Run functions to access secrets stored in Secret Manager, see [Configure secrets](https://docs.cloud.google.com/functions/1stgendocs/configuring/secrets). Note that there is no Cloud Run functions-specific integration with Cloud KMS.

### Portability

It is possible that environment variables that currently work with your Cloud Run function won't work with a different runtime environment, such as in a different language or with certain tools or libraries. It is also possible that they will not be accepted by a different platform.

You can avoid such issues by following the [POSIX standard for environment variables](http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap08.html). If you use the Google Cloud console to edit variables, Google Cloud console will warn you whenever you define a variable that might have portability issues (but will not prevent deployment). As a general rule, we recommend that environment variable keys consist solely of uppercase letters, digits, and `<underscore>` (`_`), as defined in the [Portable Character Set](http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap06.html#tagtcjh_3), and that they do not begin with a digit.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

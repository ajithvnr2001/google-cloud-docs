---
url: https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/python-differences/
title: Migrate from Python 2.7 to the latest Python 3 runtime \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:38.394040+00:00
---

# Migrate from Python 2.7 to the latest Python 3 runtime  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/standard/migrate-to-second-gen/python-differences/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Migrate from Python 2.7 to the latest Python 3 runtime Stay organized with collections  Save and categorize content based on your preferences. 

This page covers instructions for migrating from the [first-generation to the second-generation](https://docs.cloud.google.com/appengine/docs/standard/runtimes) Python runtimes. To upgrade your second-generation app to use the latest supported version of Python, see [Upgrade an existing application](https://docs.cloud.google.com/appengine/docs/standard/python3/upgrade-python-runtime).

Python 2.7 is [deprecated](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/runtime-lifecycle#deprecated). You won't be able to deploy Python 2.7 applications, even if your organization previously used an organization policy to re-enable deployments of legacy runtimes. Your existing Python 2.7 applications will continue to run and receive traffic. We recommend that you migrate to the [latest supported version of Python](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#python).

Migrating to the Python 3 runtime lets you use up-to-date language features and build apps that are more portable, with idiomatic code. The Python 3 runtime uses the latest version of the open source Python interpreter provided by the [Python Software Foundation](https://docs.python.org/3/download.html). Apps built-in the Python 3 runtime can use Python's rich ecosystem of packages and frameworks in your app, including those that use C code, by declaring dependencies in a `requirements.txt` file.

## Overview of the runtime migration process

We recommend the following incremental approach to the runtime migration, in which you maintain a functioning and testable application throughout the process:

  1. Upgrade your app to be compatible with Python 3.

Several solutions are available to help with this upgrade. For example, use [Six](https://six.readthedocs.io/), [Python-Future](http://python-future.org/), or [Python-Modernize](https://python-modernize.readthedocs.io/en/latest/).

For more information about this step of the runtime migration process, see [Porting Python 2 Code to Python 3](https://docs.python.org/2/howto/pyporting.html) on the Python Software Foundation documentation site.

  2. Pick one of these implementation strategies for any App Engine bundled service your app uses:

     1. [Migrate the legacy bundled services](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services) in your Python 2 app to unbundled Google Cloud services, third-party services, or other [recommended replacements](https://docs.cloud.google.com/appengine/docs/standard/runtimes).

     2. Continue [using legacy bundled services in your Python 3 apps](https://docs.cloud.google.com/appengine/docs/standard/python3/services/access). This approach gives you flexibility to move to unbundled services later in the migration cycle.

**Note** : Not all the legacy bundled services available for Python 2 have a corresponding service in Python 3, so those will need to be migrated to either a Google Cloud or third-party service before porting to Python 3.

Make sure to test your app after migrating each service.

  3. Prepare App Engine configuration files for the Python 3 runtime. Several important changes affect the configuration settings in the `app.yaml` file, including but not limited to:

     * If you [use legacy bundled services in your Python 3 apps](https://docs.cloud.google.com/appengine/docs/standard/python3/services/access), add the `app_engine_bundled_services` setting in your `app.yaml` file to enable [access to specific bundled services](https://docs.cloud.google.com/appengine/docs/standard/services/overview).
     * Apps are now assumed to be threadsafe. If your application isn't threadsafe, you should set [`max_concurrent_requests`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#max_concurrent_requests) in your `app.yaml` to 1. This setting may result in more instances being created than you need for a threadsafe app, and lead to unnecessary cost.
     * The `app.yaml` file no longer routes requests to your scripts. Instead, you are required to use a web framework with in-app routing, and update or remove all `script` handlers in `app.yaml`. For an example of how to do this with the Flask framework, see the [App Engine migration guide code sample in GitHub](https://github.com/GoogleCloudPlatform/appengine-python2-3-migration/tree/main/application-framework).

To learn more about changing this and other configuration files, see the Configuration files section.

  4. In the second-generation runtimes, app logs are no longer nested within the request logs. Additional steps are necessary to display the nested view of request and app logs in the Logs Explorer. For more information, see [Migrate to Cloud Logging](https://docs.cloud.google.com/appengine/migration-center/standard/python/migrate-to-cloud-logging).

  5. [Test and deploy](https://docs.cloud.google.com/appengine/docs/standard/python3/migrate-to-python3/testing) your upgraded app in a Python 3 environment.

After all of your tests pass, deploy the upgraded app to App Engine but prevent traffic from automatically routing to the new version. Use [traffic splitting](https://docs.cloud.google.com/appengine/docs/standard/splitting-traffic) to slowly migrate traffic from your app in the Python 2 runtime to the app in the Python 3 runtime. If you run into problems, you can route all traffic to a stable version until the problem is fixed.




For examples of how to convert your Python 2 apps to Python 3, you can refer to these additional resources.

## Key differences between the Python 2 and Python 3 runtimes

Most of the changes you need to make during the runtime migration come from the following differences between the Python 2 and Python 3 runtimes:

  * Memory usage differences
  * CPU usage differences
  * Request header differences
  * Gunicorn worker differences
  * Compatibility issues between Python 2 and Python 3
  * App Engine bundled services in the Python 3 runtime
  * Configuration files differences
  * A web framework is required to route requests for dynamic content
  * Apps with only static content
  * Testing differences
  * Deployment differences



### Memory usage differences

Second-generation runtimes see a higher baseline of memory usage compared to first-generation runtimes. This is due to multiple factors, such as different base image versions, and differences in how the two generations calculate memory usage.

Second-generation runtimes calculate instance memory usage as the sum of what an application process uses, and the number of application files dynamically cached in memory. To avoid memory-intensive applications from experiencing instance shutdowns due to exceeding memory limits, upgrade to a larger [instance class](https://docs.cloud.google.com/appengine/docs/standard#instance_classes) with more memory.

### CPU usage differences

Second-generation runtimes can see a higher baseline of CPU usage upon instance cold-start. Depending on an application's scaling configuration, this might have unintended side effects, such as, a higher instance count than anticipated if an application is configured to scale based on CPU utilization. To avoid this issue, review and test application scaling configurations to ensure the number of instances are acceptable.

### Request header differences

First-generation runtimes allow request headers with underscores (e.g. `X-Test-Foo_bar`) to be forwarded to the application. Second-generation runtimes introduces Nginx into the host architecture. As a result of this change, second-generation runtimes are configured to automatically remove headers with underscores (`_`). To prevent application issues, avoid using underscores in application request headers.

### Gunicorn worker differences

For Python 3+ runtimes, the number of Gunicorn workers have a direct impact on memory usage. The increase in memory usage is directly proportional to the increase in worker count. To reduce memory consumption, consider reducing the number of Gunicorn workers. See [Entrypoint best practices](https://docs.cloud.google.com/appengine/docs/standard/python3/runtime#entrypoint_best_practices) for instructions on configuring Gunicorn worker count

### Compatibility issues between Python 2 and Python 3

When Python 3 was [first released in 2008](https://www.python.org/download/releases/3.0/), several [backward incompatible changes](https://docs.python.org/3.0/whatsnew/3.0.html) were introduced to the language. Some of these changes require only minor updates to your code, such as changing the `print` statement to a `print()` function. Other changes may require significant updates to your code, such as updating the way that you handle binary data, text, and strings.

Many popular open source libraries, including the Python standard libraries, also changed when they moved from Python 2 to Python 3.

### App Engine bundled services in the Python 3 runtime

To reduce migration effort and complexity, App Engine standard environment allows you to [access many of legacy bundled services and APIs in the Python 3 runtime](https://docs.cloud.google.com/appengine/docs/standard/python3/services/access), such as Memcache. Your Python 3 app can call the bundled services APIs through language idiomatic libraries, and access the same functionality as on the Python 2 runtime.

**Note:** For the full list of legacy bundled services APIs available for Python 3, see the [legacy bundled services Available APIs](https://docs.cloud.google.com/appengine/docs/standard/services/overview).

You also have the option to use Google Cloud products that offer similar functionality as the legacy bundled services. We recommend that you consider [migrating to the unbundled Google Cloud products](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services), as doing so lets you take advantage of ongoing improvements and new features.

For the bundled services that are not available as separate products in Google Cloud, such as image processing, search, and messaging, you can use our [suggested third-party providers or other workarounds](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services#migration_paths_for_bundled_services).

### Configuration files

Before you can run your app in the Python 3 runtime of the App Engine standard environment, you may need to change some of the configuration files that App Engine uses:

  * `app.yaml`. The behavior of some fields in your [`app.yaml` configuration file](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#entrypoint) has been modified. Remove any deprecated fields and update other fields as described in the [migration guide](https://docs.cloud.google.com/appengine/docs/standard/python3/migrate-to-python3/config-files).

  * `requirements.txt`. Create this file to [install third-party dependencies](https://docs.cloud.google.com/appengine/docs/standard/python3/specifying-dependencies), including Python packages that require native C extensions. App Engine automatically installs these dependencies during app deployment in the Python 3 runtime. Previously, to install dependencies in the Python 2 runtime, you had to list your copied or self-bundled libraries in this file then run a `pip install -t lib -r requirements.txt` command.

  * `appengine_config.py`. This file is not used in the Python 3 runtime and is ignored if deployed. Previously, in the Python 2 runtime, this file was used to configure Python modules and point the app to copied or self-bundled third-party libraries.




### Web framework required to route requests for dynamic content

In the Python 2 runtime, you can create URL handlers in the `app.yaml` file to specify which app to run when a specific URL or URL pattern is requested.

In the Python 3 runtime, your app needs to use a web framework such as Flask or Django to route requests for dynamic content instead of using URL handlers in `app.yaml`. For static content, you can continue to [create URL handlers](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#handlers_element) in your app's `app.yaml` file.

### Apps with only static content

When hosting a static webapp on App Engine, you specify handlers in your `app.yaml` file to map URLs to your static files.

In Python 2, if a request does not match any of the handlers specified in the `app.yaml` file, App Engine returns a `404` error code.

In Python 3, if a request does not match any of the handlers, App Engine looks for a `main.py` file, and returns a `5xx` error if a `main.py` file is not found. Since App Engine apps with only static content do not require a `main.py` file, most users see this error, in addition to seeing instance startup errors in app logs.

To keep the same behavior of returning a `404` error when none of the static handlers match, and to avoid errors in logs, you can either:

  * Add a catch-all static handler pointing to an empty directory in the `app.yaml` file
  * Add a simple dynamic app in the `main.py` file to return a `404` error



Examples of using either option:

### app.yaml

Create an empty directory in the root app directory, such as `empty/`. In the `app.yaml` file's handler section, create a new handler at the very end to catch all other URL patterns, and specify the `empty` directory in the [`static_files` and `upload` elements](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#handlers_static_files):
    
    
      handlers:
      - url:
        .
        .
        .
      - url: /(.*)$
        static_files: empty/\1
        upload: empty/.*$
    

### main.py

Create a `main.py` file and add the following code to return a `404` error:
    
    
      def app(env, start_response):
        start_response('404 Not Found', [('Content-Type','text/html')])
        return [b"Not Found"]
    

### Testing

We recommend that you use a testing approach that is idiomatic to Python rather than being dependent on `dev_appserver`. For example, you might use `venv` to create an isolated local Python 3 environment. Any standard Python testing framework can be used to write your unit, integration, and system tests. You might also consider setting up development versions of your services or use the local emulators that are available for many Google Cloud products.

Optionally, you can use the preview version of `dev_appserver` which supports Python 3. To learn more about this testing feature, see [Using the Local Development Server](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app#local-dev-server).

### Deploying

Deployments via `appcfg.py` is not supported for Python 3. Instead, use the [`gcloud` command line](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app) to deploy your app.

### Logging

Logging in the Python 3 runtime follows the logging standard in [Cloud Logging](https://docs.cloud.google.com/logging). In the Python 3 runtime, app logs are no longer bundled with the request logs but are separated in different records. To learn more about reading and writing logs in the Python 3 runtime, see the [logging guide](https://docs.cloud.google.com/appengine/docs/standard/writing-application-logs).

## Additional migration resources

For additional information on how to migrate your App Engine apps to standalone Cloud services or the Python 3 runtime, you can refer to these App Engine resources:

  * [Serverless app migration codelabs and videos](https://github.com/googlecodelabs/migrate-python2-appengine)
  * [Python 2 to Python 3 app migration community-contributed samples](https://github.com/GoogleCloudPlatform/appengine-python2-3-migration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

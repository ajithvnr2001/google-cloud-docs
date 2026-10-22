---
url: https://docs.cloud.google.com/appengine/docs/flexible/python/runtime/
title: The Python runtime \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:02.864473+00:00
---

# The Python runtime  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/python/runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  The Python runtime Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Some [Python runtimes](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#python) have reached [end of support](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/runtime-lifecycle#end_of_support). You cannot re-deploy versions that use runtimes after their end of support date. We recommend that you [upgrade your app](https://docs.cloud.google.com/appengine/docs/flexible/python/runtime#newversions) to use the latest version of Python. 

The Python runtime is the software stack responsible for installing your application code and dependencies, and then running that application in the flexible environment.

## Python versions

Python 3.14 uses [buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview). For the full list of supported Python versions, and their corresponding Ubuntu version, see the [Runtime support schedule](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#python).

To use a [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#python) Python version, you must:

  * Include the `runtime_config` and `operating_system` settings in your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#general) file to specify an operating system.

  * Install `gcloud` CLI version **420.0.0 or later**. You can update your CLI tooling by running the [`gcloud components update`](https://docs.cloud.google.com/sdk/gcloud/reference/components/update) command. To view your installed version, run the [`gcloud version`](https://docs.cloud.google.com/sdk/gcloud/reference/version) command.

  * Optionally, you can specify a runtime version by including the `runtime_version` setting in your `app.yaml` file. By default, the latest Python version is used if the `runtime_version` setting is not specified.




**Examples**

  * To specify Python 3.14 on Ubuntu 24:
        
        runtime: python
        env: flex
        entrypoint: gunicorn -b :$PORT main:app
        
        runtime_config:
            operating_system: "ubuntu24"
            runtime_version: "3.14"
        

  * To specify the latest supported Python version on Ubuntu 24:
        
        runtime: python
          env: flex
          entrypoint: gunicorn -b :$PORT main:app
        
          runtime_config:
              operating_system: "ubuntu24"
        




See the [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#general) reference page for more information.

### Support for other Python runtimes

If you need to use a Python version that isn't [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#python), you can create a [custom runtime](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/build) and select a valid base image with the Python version you need.

For Google-supplied base images or [Docker Python base images](https://hub.docker.com/_/python), see [Building custom runtimes](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes/build#base).

To further investigate containerizing App Engine apps for Cloud Run, see the [migration guide](https://docs.cloud.google.com/appengine/migration-center/run/migrate-app-engine-flexible-to-run).

## Dependencies

The runtime looks for a [`requirements.txt`](https://pip.readthedocs.org/en/stable/user_guide/#requirements-files) file in your application's source directory and uses [`pip`](https://pip.pypa.io/en/latest/) to install any dependencies before starting your application. For more information on declaring and managing packages, see [Using Python Libraries](https://docs.cloud.google.com/appengine/docs/flexible/python/specifying-dependencies).

If your app requires private dependencies, you need to use a [custom runtime](https://docs.cloud.google.com/appengine/docs/flexible/custom-runtimes) based on the Python runtime to install the appropriate packages.

## Application startup

The runtime starts your application using the `entrypoint` defined in your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml) file. The entrypoint should start a process that responds to HTTP requests on the port defined by the environment variable `PORT`.

Most web applications use a [WSGI server](https://www.fullstackpython.com/wsgi-servers.html) such as [Gunicorn](https://gunicorn.org/), [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) or [Waitress](https://docs.pylonsproject.org/projects/waitress/en/latest/).

Before you can use one of these servers, you must add them as a dependency in your application's `requirements.txt`. If you use `gunicorn` for your Flask application, ensure that your application's Python version is [compatible](https://pypi.org/project/gunicorn/#history) with `gunicorn`.

The runtime ensures that all dependencies are installed before your entrypoint is called.
    
    
    Flask==2.0.2
    gunicorn==20.1.0
    

An example entrypoint using gunicorn for a Flask application:
    
    
    entrypoint: gunicorn -b :$PORT main:app
    

An example entrypoint using gunicorn for a Django application:
    
    
    entrypoint: gunicorn -b :$PORT mydjangoapp:wsgi
    

**Note:** The entrypoint command will be executed by [bash's `exec` function](https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html#Bourne-Shell-Builtins). Shell variables such as `$PORT` will be replaced normally, but shell syntax such as `if`, `for` and `while` embedded in the `entrypoint` command will not function.

Gunicorn is the recommended WSGI server, but it's completely possible to use any other WSGI server. For example, here is an entrypoint that uses uWSGI with Flask:
    
    
    entrypoint: uwsgi --http :$PORT --wsgi-file main.py --callable app
    

For applications that can handle requests without a WSGI server, you can just execute a Python script:
    
    
    entrypoint: python main.py
    

### Recommended Gunicorn configuration

The basic entrypoint examples shown above are intended to be starting points and may work for your web applications. Most applications, however, will need to further configure the WSGI server. Instead of specifying all of the settings on the entrypoint, create a `gunicorn.conf.py` file in your project root directory, where your `app.yaml` file is located, and specify it in your entrypoint:
    
    
    entrypoint: gunicorn -c gunicorn.conf.py -b :$PORT main:app
    

You can read about all of Gunicorn's configuration values in its [documentation](https://docs.gunicorn.org/en/latest/settings.html).

#### Workers

Gunicorn uses workers to handle requests. By default, Gunicorn uses [sync workers](https://docs.gunicorn.org/en/latest/design.html#sync-workers). This worker class is compatible with all web applications, but each worker can only handle one request at a time. By default, gunicorn only uses one of these workers. This can often cause your instances to be underutilized and increase latency in applications under high load.

We recommend setting the number of workers to 2-4 times the number of CPU cores for your instance plus one. You can specify this in `gunicorn.conf.py` as:
    
    
    import multiprocessing
    
    workers = multiprocessing.cpu_count() * 2 + 1
    

Additionally, some web applications that are mostly I/O bound can see a performance improvement by using a [different worker class](https://docs.gunicorn.org/en/latest/design.html#choosing-a-worker-type). If your worker class requires additional dependencies such as gevent or tornado, those dependencies will need to be declared in your application's `requirements.txt`.

#### HTTPS and forwarding proxies

App Engine terminates the HTTPS connection at the load balancer and forwards the request to your application. Most applications do not need to know if the request was sent over HTTPS or not, but applications that do need this information should configure Gunicorn to trust the App Engine proxy in their `gunicorn.conf.py`:
    
    
    forwarded_allow_ips = '*'
    secure_scheme_headers = {'X-FORWARDED-PROTO': 'https'}
    

Gunicorn will now ensure that the `wsgi.url_scheme` to `'https'`, which most web frameworks will use as indication of the request is secure. If your WSGI server or framework doesn't support this, just check the value of the `X-Forwarded-Proto` header manually.

Some applications also need to ascertain the user's IP address. This is available in the `X-Forwarded-For` header.

Note that the `secure_scheme_headers` setting in `gunicorn.conf.py` should be upper case, like `X-FORWARDED-PROTO`, but the headers that your code can read will be in mixed case, like `X-Forwarded-Proto`.

## Extending the runtime

The flexible environment Python runtime can be used to create a custom runtime. See [Customizing the Python](https://docs.cloud.google.com/appengine/docs/flexible/python/customizing-the-python-runtime) for more information.

## Environment variables

The following environment variables are set by the runtime environment:

Environment Variable | Description  
---|---  
`GAE_INSTANCE` | The name of the current instance.  
`GAE_MEMORY_MB` | The amount of memory available to the application process.  
`GAE_SERVICE` | The service name specified in your application's `app.yaml` file, or if no service name is specified, it is set to `default`.  
`GAE_VERSION` | The version label of the current application.  
`GOOGLE_CLOUD_PROJECT` | The Project ID associated with your application, which is visible in the Google Cloud console  
`PORT` | The port that will receive HTTP requests.  
  
You can set additional environment variables in the [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#defining_environment_variables) file.

## Metadata server

Each instance of your application can use the [Compute Engine metadata server](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata) to query information about the instance, including its host name, external IP address, instance ID, custom metadata, and service account information. App Engine does not allow you to set custom metadata for each instance, but you can set [project-wide custom metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#projectwide) and read it from your App Engine and Compute Engine instances.

This example function uses the metadata server to get the external IP address of the instance:
    
    
    METADATA_NETWORK_INTERFACE_URL = (
        "http://metadata/computeMetadata/v1/instance/network-interfaces/0/"
        "access-configs/0/external-ip"
    )
    
    
    def get_external_ip():
        """Gets the instance's external IP address from the Compute Engine metadata
        server.
    
        If the metadata server is unavailable, it assumes that the application is running locally.
    
        Returns:
            The instance's external IP address, or the string 'localhost' if the IP address
            is not available.
        """
        try:
            r = requests.get(
                METADATA_NETWORK_INTERFACE_URL,
                headers={"Metadata-Flavor": "Google"},
                timeout=2,
            )
            return r.text
        except requests.RequestException:
            logging.info("Metadata server could not be reached, assuming local.")
            return "localhost"
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

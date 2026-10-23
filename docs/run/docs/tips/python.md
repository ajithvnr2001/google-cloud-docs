---
url: https://docs.cloud.google.com/run/docs/tips/python/
title: Optimize Python applications for Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:17.654587+00:00
---

# Optimize Python applications for Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/tips/python/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Optimize Python applications for Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes optimizations for Cloud Run services written in the Python programming language, along with background information to help you understand the tradeoffs involved in some of the optimizations. The information on this page supplements the [general optimization tips](https://docs.cloud.google.com/run/docs/tips), which also apply to Python.

Many of the best practices and optimizations in common Python web-based application revolve around:

  * Handling concurrent requests (both thread-based and non-blocking I/O)
  * Reducing response latency using connection pooling and batching non-critical functions, for example sending traces and metrics to background tasks.



## Optimize the container image

Optimize the container image to reduce load and startup times, using these methods:

  * Minimize files you load at startup
  * Optimize the WSGI server



### Minimize files you load at startup

To optimize startup time, load only the required files at startup, and reduce their size. For large files, consider the following options:

  * Store large files, such as AI models, in your container for faster access. Consider loading these files after startup or at runtime.

  * Consider [configuring Cloud Storage volume mounts](https://docs.cloud.google.com/run/docs/configuring/services/cloud-storage-volume-mounts) for large files that are not critical at startup, such as media assets.

  * Import only the required submodules from any heavy dependencies, or import modules when required in your code, instead of loading them at application startup.




### Optimize the WSGI server

Python has standardized the way that applications can interact with web servers by the implementation of the WSGI standard, [PEP-3333](https://www.python.org/dev/peps/pep-3333/). One of the more common WSGI servers is `gunicorn`, which is used in much of the sample documentation.

#### Optimize gunicorn

Add the following `CMD` to the `Dockerfile` to optimize the invocation of `gunicorn`:
    
    
    CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app

If you are considering changing these settings, adjust the number of workers and threads on a per-application basis. For example, try to use a number of workers equal to the cores available and make sure there is a performance improvement, then adjust the number of threads. Setting too many workers or threads can have a negative impact, such as longer cold start latency, more consumed memory, smaller requests per second, etc.

By default, `gunicorn` spawns workers and listens on the specified port when starting up, even before evaluating your application code. In this case, you should set up [custom startup probes](https://docs.cloud.google.com/run/docs/configuring/healthchecks) for your service, since the Cloud Run default startup probe immediately marks a container instance as healthy as soon as it starts to listen on `$PORT`.

If you want to change this behavior, you can invoke `gunicorn` with the [`--preload` setting](https://docs.gunicorn.org/en/stable/settings.html#preload-app) to evaluate your application code before listening. This can help to:

  * Identify serious runtime bugs at deploy time
  * Save memory resources



You should consider what your application is preloading before adding this.

#### Other WSGI servers

You are not restricted to using `gunicorn` for running Python in containers. You can use any WSGI or ASGI web server, as long as the container listens on HTTP port `$PORT`, as per the [Container runtime contract.](https://docs.cloud.google.com/run/docs/reference/container-contract)

Common alternatives include [`uwsgi`](https://uwsgi-docs.readthedocs.io/en/latest/), [`uvicorn`](https://www.uvicorn.org/), and [`waitress`](https://docs.pylonsproject.org/projects/waitress/en/latest/).

For example, given file named `main.py` containing the `app` object, the following invocations would start a WSGI server:
    
    
    # uwsgi: pip install pyuwsgi
    uwsgi --http :$PORT -s /tmp/app.sock --manage-script-name --mount /app=main:app
    
    # uvicorn: pip install uvicorn
    uvicorn --port $PORT --host 0.0.0.0 main:app
    
    # waitress: pip install waitress
    waitress-serve --port $PORT main:app
    

These can either be added as a `CMD exec` line in a `Dockerfile`, or as a `web:` entry in `Procfile` when using [Google Cloud's buildpacks](https://docs.cloud.google.com/docs/buildpacks/builders).

## Optimize applications

In your Cloud Run service code, you can also optimize for faster startup times and memory usage.

### Reduce threads

You can optimize memory by reducing the number of threads, by using non-blocking reactive strategies and avoiding background activities. Also avoid writing to the file system, as mentioned in the [general tips page](https://docs.cloud.google.com/run/docs/tips/general#deleting_temporary_files).

If you want to support background activities in your Cloud Run service, set your Cloud Run service to [instance-based billing](https://docs.cloud.google.com/run/docs/configuring/billing-settings) so you can run background activities outside of requests and still have CPU access.

### Reduce startup tasks

Python web-based applications can have many tasks to complete during startup, such as preloading data, warming up the cache, and establishing connection pools. When executed sequentially, these tasks can be slow. However, if you want them to execute in parallel, increase the number of CPU cores.

Cloud Run sends a real user request to trigger a cold start instance. Users who have a request assigned to a newly started instance might experience long delays.

## Improve security with slimline base images

To improve security for your application, use a slimline base image with fewer packages and libraries.

If you choose not to install Python from source within your containers, use an [official Python base image](https://hub.docker.com/_/python) from Docker Hub. These images are based on the Debian operating system.

If you are using the `python` image from Docker Hub, consider using the `slim` version. These images are smaller because they don't include a number of packages that would be used to build wheels, which you might not need to do for your application. The `python` image comes with the GNU C compiler, preprocessor and core utilities.

To identify the ten largest packages in a base image, run the following command:
    
    
    DOCKER_IMAGE=python # or python:slim
    docker run --rm ${DOCKER_IMAGE} dpkg-query -Wf '${Installed-Size}\t${Package}\t${Description}\n' | sort -n | tail -n10 | column -t -s $'\t'
    

Because there are fewer of these low level packages, the `slim` based images also offer less attack surface for potential vulnerabilities. Some of these images might not include the elements required to build wheels from source.

You can add specific packages back in by adding a `RUN apt install` line to your Dockerfile. For more information, see [Using system packages in Cloud Run](https://docs.cloud.google.com/run/docs/tutorials/system-packages).

There are also options for non-Debian based containers. The `python:alpine` option might result in a much smaller container, but many Python packages might not have pre-compiled wheels that support alpine-based systems. Support is improving (see [PEP-656](https://www.python.org/dev/peps/pep-0656/)), but continues to vary. Also consider using the [`distroless base image`](https://github.com/GoogleContainerTools/distroless/blob/main/python3/README.md), which doesn't contain any package managers, shells or any other programs.

## Use `PYTHONUNBUFFERED` environment variable for logging

To see unbuffered logs from your Python application, set the environment variable `PYTHONUNBUFFERED`. When you set this variable, `stdout` and `stderr` data is immediately visible in the container logs, instead of being held in a buffer until a certain amount of data has accumulated or the stream is closed.

## What's next

For more tips, see

  * [General tips](https://docs.cloud.google.com/run/docs/tips/general)
  * [Migrating an Existing Service](https://docs.cloud.google.com/run/docs/migrating)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

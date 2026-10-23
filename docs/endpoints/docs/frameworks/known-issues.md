---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/known-issues/
title: Known issues \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:55.385272+00:00
---

# Known issues  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  Known issues Stay organized with collections  Save and categorize content based on your preferences. 

This page contains known issues in Cloud Endpoints Frameworks.

## Java and Python

This section describes known issues that affect both the Java and Python versions of Endpoints Frameworks.

### Maximum request timeout

For APIs using Endpoints Frameworks version 2, the maximum request timeout is 60 seconds.

### Endpoints Frameworks migration

When you migrate your API to Endpoints Frameworks version 2, you must deploy your API to a new App Engine app. If you reuse the old App Engine app, requests that begin with the version 1 path, `/_ah/spi`, might get routed to the Endpoints Frameworks version 2 backend, which expects paths to begin with `/_ah/api`.

### Poor performance on automatic scaling instances

App Engine offers three scaling types: basic, manual, and automatic. Endpoints Frameworks uses background threads, which automatic scaling instances don't support. Endpoints Frameworks must communicate with Google services to check quotas and report API activity, among other things. For basic and manual scaling instances, a background thread performs this communication to avoid slowing down requests. Automatic scaling instances, however, don't support background threads. Instead, the communication with Google services happens during the request. Endpoints Frameworks still works, but with potentially reduced performance.

Because of this issue, you might want to configure another scaling type. See the following sections in the App Engine documentation:

  * [Python: Scaling types and instance classes](https://docs.cloud.google.com/appengine/docs/standard/python/how-instances-are-managed)
  * [Java: Scaling types and instance classes](https://docs.cloud.google.com/appengine/docs/standard/java/how-instances-are-managed)



### Paths with trailing slashes aren't supported

When you deploy an OpenAPI document by using `gcloud endpoints services deploy`, Cloud Endpoints rejects OpenAPI documents that include paths with a trailing slash, for example: 
    
    
    paths:
      "/echo/":
        post:
          description: "Echo back a given message."
    

In Endpoints Frameworks, you must remove the trailing slash in the Python method decorator or the Java method annotation.

## Java

This section describes known issues in Endpoints Frameworks for Java.

### Cloud Endpoints Frameworks for Java - version 1.0.14 or older

Includes an issue where new fields in the [Google Service Configuration](https://docs.cloud.google.com/service-infrastructure/docs/glossary#config) causes the Cloud Endpoints Frameworks Java library to fail when parsing the Service Config. The errors will similar to the following when using service configurations created after December 5th, 2024:
    
    
    Failed to parse the HTTP response as service configuration
    com.google.api.config.ServiceConfigException: Failed to parse the HTTP response as service configuration
    

See the [release notes](https://docs.cloud.google.com/endpoints/docs/endpoints-release-notes) for more information on upgrading to version 1.0.15 or later.

### Legacy (v1) Java Endpoints Frameworks

Endpoints Frameworks version 1 for Java has a bug that throws an exception when an enum is annotated. This issue is caused by a dependency on an old version of [Jackson](https://wikipedia.org/wiki/Jackson_\(API\)). To workaround this issue, you must [migrate to Endpoints Frameworks version 2](https://docs.cloud.google.com/endpoints/docs/frameworks/java/migrating).

## Python

This section describes known issues in Endpoints Frameworks for Python.

### Error message: `ImportError: cannot import name locked_file`

When you run `pip install` with a `requirements.txt` file, you might get an `ImportError: cannot import name locked_file` error message. The issue is caused when `pip` installs a version of the `oauth2client` package that is incompatible with `google-endpoints-api-management`. To workaround this issue, make sure that the `google-endpoints` and `google-endpoints-api-management` lines appear first in your `requirements.txt` file, for example:
    
    
    google-endpoints==4.8.0
    google-endpoints-api-management==1.11.1
    # Newer versions of rsa module are incompatible with Python 2.7
    rsa==4.5; python_version < '3'

Add other requirements _after_ these lines.

### API returns `404` errors when testing locally

Symptom: All endpoints return `404` when you use `dev_appserver.py` to test your API locally, but when you deploy your API to App Engine, the endpoints respond as expected. This issue has been observed in applications that use the [Django-six library](https://pypi.org/project/django-six/).

This issue is caused by a version conflict between the `python-future` library, which is included in both the Endpoints Frameworks for Python library and the Django-six library. The exact version of the Django-six library causing the conflict is unknown at this time.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

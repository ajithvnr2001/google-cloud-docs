---
url: https://docs.cloud.google.com/appengine/docs/flexible/using-firestore/
title: Use Firestore \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:11.399040+00:00
---

# Use Firestore  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/using-firestore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Use Firestore Stay organized with collections  Save and categorize content based on your preferences. 

Go Java Node.js PHP Python Ruby .NET Custom

Firestore is a NoSQL document database built for automatic scaling, high performance, and ease of application development. As the successor to Datastore, Firestore is the recommended database for all new applications. Firestore offers multiple interfaces, including a Datastore-compatible API to support legacy code built on Datastore.

This document describes how to use the [Cloud Client Libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries) to store and retrieve data in a Datastore mode database. You can use the sample application in this guide for any [supported](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#python) version of Python by specifying the runtime version and operating system in your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/flexible/python/runtime#newversions) file. 

## Prerequisites and setup

  * [Set up your environment and project](https://docs.cloud.google.com/appengine/docs/flexible/setting-up-environment) to understand how apps are structured in App Engine. Write down and save your project ID, because you will need it to run the sample application described in this document.



## Clone the repository

Download (clone) the sample:
    
    
      git clone https://github.com/GoogleCloudPlatform/python-docs-samples
      cd python-docs-samples/appengine/flexible/datastore
    

## Edit project configuration and set dependencies

Include the `google-cloud-datastore` library in `requirements.txt` file. This is the client library for Datastore mode.
    
    
    Flask==3.1.3; python_version >= '3.9'
    google-cloud-datastore==2.20.2
    gunicorn==23.0.0
    

## Application code

The sample application logs, retrieves, and displays visitor IPs. You can see that a log entry is a two-field class that is given the type `visit`, and is saved to Datastore mode using the [put](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client#google_cloud_datastore_client_Client_put) command. Then, the ten most recent visits are retrieved in descending order using the `query()` command.
    
    
    @app.route("/")
    def index():
        ds = datastore.Client()
    
        user_ip = request.remote_addr
    
        # Keep only the first two octets of the IP address.
        if is_ipv6(user_ip):
            user_ip = ":".join(user_ip.split(":")[:2])
        else:
            user_ip = ".".join(user_ip.split(".")[:2])
    
        entity = datastore.Entity(key=ds.key("visit"))
        entity.update(
            {
                "user_ip": user_ip,
                "timestamp": datetime.datetime.now(tz=datetime.timezone.utc),
            }
        )
    
        ds.put(entity)
        query = ds.query(kind="visit", order=("-timestamp",))
    
        results = []
        for x in query.fetch(limit=10):
            try:
                results.append("Time: {timestamp} Addr: {user_ip}".format(**x))
            except KeyError:
                print("Error with result format, skipping entry.")
    
        output = "Last 10 visits:\n{}".format("\n".join(results))
    
        return output, 200, {"Content-Type": "text/plain; charset=utf-8"}
    
    

## Using `index.yaml` files

The sample app performs queries. More elaborate Datastore mode queries require one or more [indexes](https://docs.cloud.google.com/datastore/docs/concepts/indexes), which you must specify in an [`index.yaml` file](https://docs.cloud.google.com/appengine/docs/flexible/configuring-datastore-indexes-with-index-yaml) that you upload along with your app. This file may be created manually, or generated automatically while testing your app locally. 

## Local testing

If you need to develop and test your application locally, you can [use the Datastore mode emulator](https://docs.cloud.google.com/datastore/docs/tools/datastore-emulator).

## For more information

For complete information on Datastore mode, including optimizations and concepts, see the [Firestore in Datastore mode documentation](https://docs.cloud.google.com/datastore/docs/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

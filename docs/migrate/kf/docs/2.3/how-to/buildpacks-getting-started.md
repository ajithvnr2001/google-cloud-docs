---
url: https://docs.cloud.google.com/migrate/kf/docs/2.3/how-to/buildpacks-getting-started/
title: Getting started with buildpacks \u00a0|\u00a0 Kf 2.3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:44.423618+00:00
---

# Getting started with buildpacks  |  Kf 2.3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.3/how-to/buildpacks-getting-started/

Version 2.3

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.3 ](https://docs.cloud.google.com/migrate/kf/docs/2.3)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.3/getting-started)



Send feedback 

#  Getting started with buildpacks Stay organized with collections  Save and categorize content based on your preferences. 

Kf supports a variety of buildpacks. This document covers some starter examples for using them.

## Before you begin

  * You should have Kf running on a cluster.
  * You should have run `kf target -s <space-name>` to target your space.



## Java (v2) Buildpack

Use [spring initializr](https://start.spring.io/) to create a Java 8 maven project with a spring web dependency and JAR packaging. Download it, extract it, and once extracted you can generate a JAR.
    
    
    ./mvnw package

Push the JAR to Kf with the Java v2 buildpack.
    
    
    kf push java-v2 --path target/helloworld-0.0.1-SNAPSHOT.jar

## Java (v3) Buildpack

Use [spring initializr](https://start.spring.io/) to create a Java 8 maven project with a spring web dependency and JAR packaging. Download it, extract it, and once extracted, push to Kf with the cloud native buildpack.
    
    
    kf push java-v3 --stack org.cloudfoundry.stacks.cflinuxfs3

## Python (v2) Buildpack

Create a new directory with files as shown in the following structure.
    
    
    tree
    .
    ├── Procfile
    ├── requirements.txt
    └── server.py
    
    
    cat Procfile
    web: python server.py
    
    
    cat requirements.txt
    Flask
    
    
    cat server.py
    from flask import Flask
    import os
    app = Flask(__name__)
    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    if __name__ == "__main__":
      port = int(os.getenv("PORT", 8080))
      app.run(host='0.0.0.0', port=port)

Push the Python flask app using v2 buildpacks.
    
    
    kf push python --buildpack python\_buildpack

## Python (v3) Buildpack

(same as above)

Push the Python flask app using cloud native buildpacks.
    
    
    kf push pythonv3 --stack org.cloudfoundry.stacks.cflinuxfs3

## Staticfile (v2) Buildpack

Create a new directory that holds your source code.

Add an `index.html` file with this content.
    
    
    <!DOCTYPE html>
    
    <html lang="en">
    
    <head><title>Hello, world!</title></head>
    
    <body><h1>Hello, world!</h1></body>
    
    </html>
    

Push the static content with the staticfile buildpack.
    
    
    kf push staticsite --buildpack staticfile\_buildpack

# Related documents

  * [Customizing buildbacks](https://docs.cloud.google.com/migrate/kf/docs/2.3/how-to/customizing-buildpacks)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

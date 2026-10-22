---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/writing-web-service/
title: Write a basic web service for App Engine \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:20.029664+00:00
---

# Write a basic web service for App Engine  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/writing-web-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Write a basic web service for App Engine Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you are deploying a new Python web service to Google Cloud, we recommend getting started with [Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service).

Write and locally test a web service that serves a static HTML file using Flask. Then, create the configuration files that you need for deploying the web service to App Engine.

In this step, you create and locally test a version of a web service that displays placeholder data. The goal here is to ensure that your basic web service is working before adding Datastore and Firebase authentication.

## Before you begin

  1. If you have not already created a Google Cloud project, [create a Google Cloud project](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/creating-gcp-project).

  2. If you have not already, set up your local environment for Python 3 development by completing the following:

     * [Download and install Python 3](https://docs.cloud.google.com/python/docs/setup#installing_python) for developing your web service and running the Google Cloud CLI.

     * Use your Google Cloud user credentials to authenticate with the Google Cloud CLI and enable local testing with Datastore:
           
           gcloud auth application-default login
           

**Tip:** For more extensive testing, it is recommended that you set up a service account rather than using user-end credentials. For more information on service accounts and other types of authentication, see [Authentication Overview](https://docs.cloud.google.com/docs/authentication).



## Structure your web service files

The project directory where you create your web service will have the following file structure:

  * `building-an-app/`
    * `app.yaml`
    * `main.py`
    * `requirements.txt`
    * `static/`
      * `script.js`
      * `style.css`
    * `templates/`
      * `index.html`



The following sections provide an example of how to set up the files in your project directory.

## Write your web service

The initial iteration of your web service uses Flask to serve a [Jinja-based HTML template](http://jinja.pocoo.org/docs/2.10/templates/).

To set up your web service:

  1. Create your `templates/index.html` file:
         
         <!doctype html>
         <!--
          Copyright 2021 Google LLC
         
          Licensed under the Apache License, Version 2.0 (the "License");
          you may not use this file except in compliance with the License.
          You may obtain a copy of the License at
         
               http://www.apache.org/licenses/LICENSE-2.0
         
          Unless required by applicable law or agreed to in writing, software
          distributed under the License is distributed on an "AS IS" BASIS,
          WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
          See the License for the specific language governing permissions and
          limitations under the License.
         -->
         
         <html>
         <head>
           <title>Datastore and Firebase Auth Example</title>
           <script src="{{ url_for('static', filename='script.js') }}"></script>
           <link type="text/css" rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
         </head>
         <body>
         
           <h1>Datastore and Firebase Auth Example</h1>
         
           <h2>Last 10 visits</h2>
           {% for time in times %}
             <p>{{ time }}</p>
           {% endfor %}
         
         </body>
         </html>
         

  2. Add behaviors and styles with `static/script.js` and `static/style.css` files:
         
         'use strict';
         
         window.addEventListener('load', function () {
         
           console.log("Hello World!");
         
         });
         
         /**
          * Copyright 2021 Google LLC
          *
          * Licensed under the Apache License, Version 2.0 (the "License");
          * you may not use this file except in compliance with the License.
          * You may obtain a copy of the License at
          *
          *      http://www.apache.org/licenses/LICENSE-2.0
          *
          * Unless required by applicable law or agreed to in writing, software
          * distributed under the License is distributed on an "AS IS" BASIS,
          * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
          * See the License for the specific language governing permissions and
          * limitations under the License.
          */
         
         body {
           font-family: "helvetica", sans-serif;
           text-align: center;
         }
         

  3. In your `main.py` file, use Flask to render your HTML template with the placeholder data:
         
         import datetime
         
         from flask import Flask, render_template
         
         app = Flask(__name__)
         
         
         @app.route("/")
         def root():
             # For the sake of example, use static information to inflate the template.
             # This will be replaced with real information in later steps.
             dummy_times = [
                 datetime.datetime(2018, 1, 1, 10, 0, 0),
                 datetime.datetime(2018, 1, 2, 10, 30, 0),
                 datetime.datetime(2018, 1, 3, 11, 0, 0),
             ]
         
             return render_template("index.html", times=dummy_times)
         
         
         if __name__ == "__main__":
             # This is used when running locally only. When deploying to Google App
             # Engine, a webserver process such as Gunicorn will serve the app. This
             # can be configured by adding an `entrypoint` to app.yaml.
             # Flask's development server will automatically serve static files in
             # the "static" directory. See:
             # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
             # App Engine itself will serve those files as configured in app.yaml.
             app.run(host="127.0.0.1", port=8080, debug=True)

  4. Configure all dependencies you will need for your web service in your `requirements.txt` file:
         
         Flask==3.1.3; python_version >= '3.9'
         




## Test your web service

Test your web service by running it locally in a virtual environment:

### Mac OS / Linux

  1. Create an [isolated Python environment](https://docs.cloud.google.com/python/docs/setup#installing_and_using_virtualenv): 
         
         python3 -m venv env
         source env/bin/activate

  2. If you're not in the directory that contains the sample code, navigate to the directory that contains the `hello_world` sample code. Then install dependencies: 
         
         cd YOUR_SAMPLE_CODE_DIR
         pip install -r requirements.txt

  3. Run the application: 
         
         python main.py

  4. In your web browser, enter the following address: 
         
         http://localhost:8080




### Windows

Use PowerShell to run your Python packages.

  1. Locate your installation of [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-windows). 
  2. Right-click on the shortcut to PowerShell and start it as an administrator.
  3. Create an [isolated Python environment](https://docs.cloud.google.com/python/docs/setup#installing_and_using_virtualenv). 
         
         python -m venv env
         .\env\Scripts\activate

  4. Navigate to your project directory and install dependencies. If you're not in the directory that contains the sample code, navigate to the directory that contains the `hello_world` sample code. Then, install dependencies: 
         
         cd YOUR_SAMPLE_CODE_DIR
         pip install -r requirements.txt

  5. Run the application: 
         
         python main.py

  6. In your web browser, enter the following address: 
         
         http://localhost:8080




## Configure your web service for App Engine

To deploy your web service to App Engine, you need an `app.yaml` file. This configuration file defines your web service's settings for App Engine.

To configure your web service for deployment to App Engine, create your `app.yaml` file in the root directory of your project, for example `building-an-app`:
    
    
    # Copyright 2021 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #      http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    runtime: python314
    
    handlers:
      # This configures Google App Engine to serve the files in the app's static
      # directory.
    - url: /static
      static_dir: static
    
      # This handler routes all requests not caught above to your main app. It is
      # required when static routes are defined, but can be omitted (along with
      # the entire handlers section) when there are no static files defined.
    - url: /.*
      script: auto
    

Notice that for this simple web service, your `app.yaml` file needs to define only the runtime setting and handlers for static files.

For more complicated web services, you can configure additional settings in your `app.yaml`, like scaling, additional handlers, and other application elements like environment variables and service names. For more information and a list of all the supported elements, see the [`app.yaml` reference](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml).

## Next steps

Now that you've configured, created, and tested your web service, you can deploy this version of your web service to App Engine.

[ Previous arrow_back  Create your project  ](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/creating-gcp-project)

[ Next Deploy your web service  arrow_forward  ](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/deploying-web-service)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

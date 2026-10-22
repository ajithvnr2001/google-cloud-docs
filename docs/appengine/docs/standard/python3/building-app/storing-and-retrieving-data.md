---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/storing-and-retrieving-data/
title: Store and retrieve data \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:20.590374+00:00
---

# Store and retrieve data  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/storing-and-retrieving-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Store and retrieve data Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python3/how-requests-are-routed#region-id). 

OK

**Note:** If you are deploying a new Python web service to Google Cloud, we recommend getting started with [Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service).

Update your web service to connect to and handle data through Firestore in Datastore mode (Datastore). Use the [Datastore client libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries#client-libraries-install-python) to connect your web service to Datastore, a non-relational (NoSQL) database built for automatic scaling, high performance, and ease of application development.

In this step, you update your web service so that it stores page request data in Datastore and then displays a list of the last ten page requests. The goal here is to get data storage working for your web service before you add Firebase Authentication and personalize data storage for authenticated users.

## Before you begin

If you have completed all the previous steps in this guide, skip this section. Otherwise, complete one of the following:

  * Start from [Build a Python 3 App](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app) and complete all the steps leading up to this one.

  * If you already have a [Google Cloud project](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/creating-gcp-project), you can continue by downloading a copy of the web service:

    1. Download the sample application repository using [Git](https://git-scm.com/):
           
           git clone https://github.com/GoogleCloudPlatform/python-docs-samples
           

Alternatively, you can [download the sample](https://github.com/GoogleCloudPlatform/python-docs-samples/archive/master.zip) as a zip file and then extract it.

    2. Navigate to the directory that contains a copy of the files from the previous step:
           
           cd python-docs-samples/appengine/standard_python3/building-an-app/building-an-app-1
           

    3. Enable the Datastore API:
           
           gcloud services enable datastore.googleapis.com
           




## Store and retrieve Datastore entities

Store and retrieve site request times as Datastore entities by completing the following:

  1. Add the following code to your `main.py` file:
         
         from google.cloud import [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest)
         
         datastore_client = [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest).[Client](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html)()
         
         def store_time(dt):
             entity = [datastore](https://docs.cloud.google.com/python/docs/reference/datastore/latest).[Entity](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.entity.Entity.html)(key=datastore_client.[key](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_key)("visit"))
             entity.update({"timestamp": dt})
         
             datastore_client.[put](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_put)(entity)
         
         
         def fetch_times(limit):
             query = datastore_client.[query](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.client.Client.html#google_cloud_datastore_client_Client_query)(kind="visit")
             query.[order](https://docs.cloud.google.com/python/docs/reference/datastore/latest/google.cloud.datastore.query.Query.html#google_cloud_datastore_query_Query_order) = ["-timestamp"]
         
             times = query.fetch(limit=limit)
         
             return times
         
         

The `store_time` method above uses the Datastore client libraries to create a new entity in Datastore. Datastore entities are data objects that consist of _keys_ and _properties_. In this case, the entity's key is its custom _kind_ , `visit`. The entity also has one property, `timestamp`, containing time of a page request.

The `fetch_times` method uses the key `visit` to query the database for the ten most recent `visit` entities and then stores those entities in a list in descending order.

  2. Update your `root` method to call your new methods:
         
         @app.route("/")
         def root():
             # Store the current access time in Datastore.
             store_time(datetime.datetime.now(tz=datetime.timezone.utc))
         
             # Fetch the most recent 10 access times from Datastore.
             times = fetch_times(10)
         
             return render_template("index.html", times=times)
         
         

  3. Update your `templates/index.html` file to print the `timestamp` of each entity:
         
         <h2>Last 10 visits</h2>
         {% for time in times %}
           <p>{{ time['timestamp'] }}</p>
         {% endfor %}

  4. Ensure that your `requirements.txt` file includes all necessary dependencies:
         
         Flask==3.1.3; python_version >= '3.9'
         google-cloud-datastore==2.15.1
         




For more information about Datastore entities, properties, and keys, see [Entities, Properties, and Keys](https://docs.cloud.google.com/datastore/docs/concepts/entities). For more information on using Datastore client libraries, see [Datastore Client Libraries](https://docs.cloud.google.com/datastore/docs/reference/libraries#client-libraries-install-python).

## Test your web service

Test your web service by running it locally in a virtual environment:

  1. Run the following commands in your project's main directory to install new dependencies and run your web service. If you have not set up a virtual environment for local testing, see [testing your web service](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/writing-web-service#testing_your_web_service).
         
         pip install -r requirements.txt
         python main.py
         

  2. Enter the following address in your web browser to view your web service:
         
         http://localhost:8080
         

**Tip:** Refresh the page to create additional page requests and store more entities in Datastore.



You can view the entities that are created by your web service in the Google Cloud console:

[Go to the Datastore entities page](https://console.cloud.google.com/datastore)

## Deploy your web service

Now that you have Datastore working locally, you can re-deploy your web service to App Engine.

Run the following command from the root directory of your project, where your `app.yaml` file is located:
    
    
    gcloud app deploy
    

All traffic is automatically routed to the new version you deployed.

For more information on managing versions, see [Managing Services and Versions](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/deploying-web-service#managing_services_and_versions).

## View your service

To quickly launch your browser and access your web service at `https://PROJECT_ID.REGION_ID.r.appspot.com`, run the following command:
    
    
    gcloud app browse
    

## Next Steps

Now that you have Datastore working with your web service, you're ready to learn how to add Firebase to your web service.

[ Previous arrow_back  Deploy your web service  ](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/deploying-web-service)

[ Next Add Firebase  arrow_forward  ](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/adding-firebase)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

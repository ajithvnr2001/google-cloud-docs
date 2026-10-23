---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/personalizing-data-for-authenticated-users/
title: Personalize data for authenticated users \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:45.392945+00:00
---

# Personalize data for authenticated users  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/personalizing-data-for-authenticated-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Personalize data for authenticated users Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python3/how-requests-are-routed#region-id). 

OK

**Note:** If you are deploying a new Python web service to Google Cloud, we recommend getting started with [Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service).

Use authenticated user information to store and retrieve user-specific data and personalize each user's experience with your web service.

In a previous step, you updated the web service to display the last ten requests from all users. In this step, you use authenticated user information to update your web service so that the page displays only a list of the last ten requests made by the currently authenticated user.

## Before you Begin

If you have completed all the previous steps in this guide, skip this section. Otherwise, complete one of the following:

  * Start from [Build a Python 3 App](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app) and complete all the steps leading up to this one.

  * If you already have a [Google Cloud project](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/creating-gcp-project), you can continue by downloading a copy of the web service and adding Firebase:

    1. Download the sample application repository using [Git](https://git-scm.com/):
           
           git clone https://github.com/GoogleCloudPlatform/python-docs-samples
           

Alternatively, you can [download the sample](https://github.com/GoogleCloudPlatform/python-docs-samples/archive/master.zip) as a zip file and then extract it.

    2. Navigate to the directory that contains a copy of the files from the previous step:
           
           cd python-docs-samples/appengine/standard_python3/building-an-app/building-an-app-3
           

    3. [Add Firebase to your Google Cloud project and web service](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/adding-firebase#adding-firebase-to-your-project).




## Store and retrieve user-specific data

You can indicate that data is connected to a certain user by using Firestore in Datastore mode (Datastore) ancestors, which allow you to organize your Datastore data hierarchically.

To do this, complete the following steps:

  1. Update your `store_time` and `fetch_time` methods to use Datastore ancestors for storing and retrieving `visit` entities:
         
         datastore_client = datastore.Client()
         
         def store_time(email, dt):
             entity = datastore.Entity(key=datastore_client.key("User", email, "visit"))
             entity.update({"timestamp": dt})
         
             datastore_client.put(entity)
         
         
         def fetch_times(email, limit):
             ancestor = datastore_client.key("User", email)
             query = datastore_client.query(kind="visit", ancestor=ancestor)
             query.order = ["-timestamp"]
         
             times = query.fetch(limit=limit)
         
             return times
         
         

Each `visit` entity now has an ancestor that it is connected to. These ancestors are Datastore entities that represent individual authenticated users. Each ancestor's _key_ includes the `User` _kind_ and a custom ID, which is the authenticated user's email address. You use the ancestor key to query the database for only the times that are associated with a specific user.

  2. Update the `store_times` method call in your `root` method and move it inside the `id_token` conditional so that it only runs if the server has authenticated a user:
         
         @app.route("/")
         def root():
             # Verify Firebase auth.
             id_token = request.cookies.get("token")
             error_message = None
             claims = None
             times = None
         
             if id_token:
                 try:
                     # Verify the token against the Firebase Auth API. This example
                     # verifies the token on each page load. For improved performance,
                     # some applications may wish to cache results in an encrypted
                     # session store (see for instance
                     # http://flask.pocoo.org/docs/1.0/quickstart/#sessions).
                     claims = google.oauth2.id_token.verify_firebase_token(
                         id_token, firebase_request_adapter
                     )
         
                     store_time(claims["email"], datetime.datetime.now(tz=datetime.timezone.utc))
                     times = fetch_times(claims["email"], 10)
         
                 except ValueError as exc:
                     # This will be raised if the token is expired or any other
                     # verification checks fail.
                     error_message = str(exc)
         
             return render_template(
                 "index.html", user_data=claims, error_message=error_message, times=times
             )
         
         




## Configure indexes

Datastore makes queries based on indexes. For simple entities, Datastore automatically generates these indexes. However, it cannot automatically generate indexes for more complicated entities, including those with ancestors. Because of this, you need to manually create an index for `visit` entities so that Datastore can perform queries involving `visit` entities.

To create an index for `visit` entities, complete the following steps:

  1. Create an `index.yaml` file in the root directory of your project, for example `building-an-app`, and add the following index:
         
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
         
         indexes:
         
         - kind: visit
           ancestor: yes
           properties:
           - name: timestamp
             direction: desc
         

  2. Deploy your `index.yaml` indexes in Datastore by running the following command and following the prompts:
         
         gcloud datastore indexes create index.yaml
         




It can take a while for Datastore to create indexes. Creating indexes before deploying your web service to App Engine both allows you to test locally using those indexes and prevents exceptions that might occur for queries that require an index that is still in the process of being built.

**Tip:** You can view the index you created in the Datastore console:

[View your indexes](https://console.cloud.google.com/datastore/indexes)

For more information on making Datastore indexes, see [Configuring Datastore Indexes](https://docs.cloud.google.com/appengine/docs/standard/python/config/indexconfig).

## Testing your web service

Test your web service by running it locally in a virtual environment:

  1. Run the following command in your project's main directory to run your web service. If you have not set up a virtual environment for local testing, see [testing your web service](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/writing-web-service#testing_your_web_service).
         
         python main.py
         

  2. Enter the following address in your web browser to view your web service:
         
         http://localhost:8080
         




## Deploy your web service

Now that you have Datastore working locally, you can re-deploy your web service to App Engine.

Run the following command from the root directory of your project, where your `app.yaml` file is located:
    
    
    gcloud app deploy
    

All traffic is automatically routed to the new version you deployed.

For more information on managing versions, see [Manage Services and Versions](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/deploying-web-service#managing_services_and_versions).

## View your service

To quickly launch your browser and access your web service at `https://PROJECT_ID.REGION_ID.r.appspot.com`, run the following command:
    
    
    gcloud app browse
    

## Next Steps

Congratulations! You've successfully built a web service that uses Datastore data storage and Firebase authentication to provide authenticated users with a personalized web page.

Now you can clean up by shutting down, deactivating, or disabling billing for your project.

[ Previous arrow_back  Authenticate users  ](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/authenticating-users)

[ Next Clean up  arrow_forward  ](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/cleaning-up)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

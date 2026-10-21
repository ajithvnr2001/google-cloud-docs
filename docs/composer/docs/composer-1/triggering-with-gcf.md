---
url: https://docs.cloud.google.com/composer/docs/composer-1/triggering-with-gcf/
title: Trigger Managed Service for Apache Airflow DAGs with Cloud Run functions and Airflow REST API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:01.324103+00:00
---

# Trigger Managed Service for Apache Airflow DAGs with Cloud Run functions and Airflow REST API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/triggering-with-gcf/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Trigger Managed Service for Apache Airflow DAGs with Cloud Run functions and Airflow REST API Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/triggering-with-gcf "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/triggering-with-gcf "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This page describes how to use Cloud Run functions to trigger Managed Service for Apache Airflow DAGs in response to events.

Apache Airflow is designed to run DAGs on a regular schedule, but you can also trigger DAGs in response to events. One way to do this is to use [Cloud Run functions](https://docs.cloud.google.com/functions/docs/concepts/overview) to trigger Managed Airflow DAGs when a specified event occurs.

You can also:

  * [Trigger DAGs using only the Airflow REST API](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-api).
  * Create a function that [triggers a DAG when a message is pushed to a Pub/Sub topic](https://docs.cloud.google.com/composer/docs/composer-1/triggering-gcf-pubsub).



The example in this guide demonstrates a function that triggers a DAG in response to an event:

  1. You configure triggers for your function in Cloud Run functions.
  2. When the function is triggered, it makes a request to trigger a DAG through the Airflow REST API of your Managed Airflow environment. The request contains event's identifier and type, and the event's payload.
  3. Airflow processes this request and runs the DAG specified in the request. The DAG outputs the data that was passed to it from the function.



## Before you begin

This section lists preparatory steps.

### Check your environment's networking configuration

This solution does not work in Private IP and VPC Service Controls configurations because it isn't possible to configure connectivity from Cloud Run functions to the Airflow web server in these configurations.

### Enable APIs for your project

###  Console 

Enable the Managed Airflow and Cloud Run functions APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=composer.googleapis.com,cloudfunctions.googleapis.com)

###  gcloud 

Enable the Managed Airflow and Cloud Run functions APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
    
    
    gcloud services enable cloudfunctions.googleapis.com composer.googleapis.com

### Enable the Airflow REST API

Depending on your version of Airflow:

  * For Airflow 2, the stable REST API is already enabled by default. If your environment has the stable API disabled, then [enable the stable REST API](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-api#enable-stable). 
  * For Airflow 1, [enable the experimental REST API](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-api#enable-experimental). 



### Allow API calls to Airflow REST API using web server network access control

Cloud Run functions can reach out to the Airflow REST API through a **IPv4 or IPv6 address**.

If you are not sure what will be the calling IP range then use a default configuration option in **Webserver Access Control** which is `All IP addresses have access (default)` to not accidentally block your Cloud Run functions. You can always [configure web server network access later](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-web-interface#network-access-controls).

### Get the Airflow web server URL

This example makes REST API requests to the Airflow web server endpoint. You use the part of the Airflow web interface URL before `.appspot.com` in your Cloud Function code. 

###  Console 

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. Click the name of your environment.

  3. On the **Environment details** page, go to the **Environment configuration** tab.

  4. The URL of the Airflow web server is listed in the **Airflow web UI** item.




###  gcloud 

Run the following command:
    
    
    gcloud composer environments describe ENVIRONMENT_NAME \
        --location LOCATION \
        --format='value(config.airflowUri)'
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.



### Get the client_id of the IAM proxy

**Caution:** This guide is for Managed Airflow (Legacy Gen 1) and the described steps won't work in Managed Airflow (Gen 2) or Managed Airflow (Gen 3). Instead, follow the instructions on the [Trigger DAGs with Cloud Run functions](https://docs.cloud.google.com/composer/docs/composer-2/triggering-with-gcf) page.

To make a request to the Airflow REST API endpoint, the function requires the client ID of the Identity and Access Management proxy that protects the Airflow web server.

Managed Airflow does not provide this information directly. Instead, make an unauthenticated request to the Airflow web server and capture the client ID from the redirect URL:

###  cURL 
    
    
    curl -v AIRFLOW_URL 2>&1 >/dev/null | grep -o "client_id\=[A-Za-z0-9-]*\.apps\.googleusercontent\.com"
    

Replace `AIRFLOW_URL` with the URL of the Airflow web interface.

In the output, search for the string following `client_id`. For example:
    
    
    client_id=**836436932391-16q2c5f5dcsfnel77va9bvf4j280t35c.apps.googleusercontent.com**
    

###  Python 

Save the following code in a file called `get_client_id.py`. Fill in your values for `project_id`, `location`, and `composer_environment`, then run the code in Cloud Shell or your local environment. 
    
    
    # This script is intended to be used with Composer 1 environments
    # In Composer 2, the Airflow Webserver is not in the tenant project
    # so there is no tenant client ID
    # See https://cloud.google.com/composer/docs/composer-2/environment-architecture
    # for more details
    import google.auth
    import google.auth.transport.requests
    import requests
    import six.moves.urllib.parse
    
    # Authenticate with Google Cloud.
    # See: https://cloud.google.com/docs/authentication/getting-started
    credentials, _ = google.auth.default(
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    authed_session = google.auth.transport.requests.AuthorizedSession(credentials)
    
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'us-central1'
    # composer_environment = 'YOUR_COMPOSER_ENVIRONMENT_NAME'
    
    environment_url = (
        "https://composer.googleapis.com/v1beta1/projects/{}/locations/{}"
        "/environments/{}"
    ).format(project_id, location, composer_environment)
    composer_response = authed_session.request("GET", environment_url)
    environment_data = composer_response.json()
    composer_version = environment_data["config"]["softwareConfig"]["imageVersion"]
    if "composer-1" not in composer_version:
        version_error = (
            "This script is intended to be used with Composer 1 environments. "
            "In Composer 2, the Airflow Webserver is not in the tenant project, "
            "so there is no tenant client ID. "
            "See https://cloud.google.com/composer/docs/composer-2/environment-architecture for more details."
        )
        raise (RuntimeError(version_error))
    airflow_uri = environment_data["config"]["airflowUri"]
    
    # The Composer environment response does not include the IAP client ID.
    # Make a second, unauthenticated HTTP request to the web server to get the
    # redirect URI.
    redirect_response = requests.get(airflow_uri, allow_redirects=False)
    redirect_location = redirect_response.headers["location"]
    
    # Extract the client_id query parameter from the redirect.
    parsed = six.moves.urllib.parse.urlparse(redirect_location)
    query_string = six.moves.urllib.parse.parse_qs(parsed.query)
    print(query_string["client_id"][0])

## Upload a DAG to your environment

[Upload a DAG to your environment](https://docs.cloud.google.com/composer/docs/composer-1/manage-dags#add). The following example DAG outputs the received DAG run configuration. You trigger this DAG from a function, which you create later in this guide.
    
    
    import datetime
    
    import airflow
    from airflow.operators.bash_operator import BashOperator
    
    with airflow.DAG(
            'composer_sample_trigger_response_dag',
            start_date=datetime.datetime(2026, 1, 1),
            # Not scheduled, trigger only
            schedule=None) as dag:
    
        # Print the dag_run's configuration, which includes information about the
        # Cloud Storage object change.
        print_gcs_info = BashOperator(
            task_id='print_gcs_info', bash_command='echo {{ dag_run.conf }}}}')
    

## Deploy a function that triggers the DAG

You can deploy a function using your preferred language supported by Cloud Run functions or Cloud Run. This tutorial demonstrates a Cloud Function implemented in [Python](https://docs.cloud.google.com/functions/docs/deploying/console) and [Java](https://docs.cloud.google.com/composer/docs/composer-1/functions/docs/securing/authenticating#functions-bearer-token-example-java).

### Specify function configuration parameters

  * **Trigger** : Select an Eventarc trigger or several triggers for your function.

For more information about creating triggers, see [Create triggers with Eventarc](https://docs.cloud.google.com/run/docs/triggering/trigger-with-events). For example, you can [trigger functions from Cloud Storage using Eventarc](https://docs.cloud.google.com/run/docs/tutorials/trigger-functions-storage).

**Caution:** Don't use Managed Airflow environment buckets as resources in your function's triggers because this might cause the function to trigger several times per second.
  * **Service account** : The service account that you specify for the trigger must have enough permissions to trigger DAGs in Managed Airflow environments.

We recommend to follow the minimum privilege principle and grant only the **Composer User** (`composer.user`) role to it. For more information about configuring permissions, see [Roles and permissions for Cloud Run targets](https://docs.cloud.google.com/eventarc/docs/roles-permissions).

  * **Function entry point** :

    * _(Python)_ When adding code for this example, select the **Python 3.10** or later runtime and specify `trigger_dag` as the entry point.




### Add requirements

Specify the dependencies in the `requirements.txt` file:
    
    
    requests-toolbelt==1.0.0
    google-auth==2.38.0
    google-cloud-pubsub==2.28.0
    

### Add function code

Put the following code to the `main.py` file and make the following replacements:

  * Replace the value of the `client_id` variable with the `client_id` value that you obtained earlier.

  * Replace the value of the `webserver_id` variable with your tenant project ID, which is a part of the Airflow web interface URL before `.appspot.com`. You obtained the Airflow web interface URL earlier.

  * Specify the Airflow REST API version that you use:

    * If you use the stable Airflow REST API, set the `USE_EXPERIMENTAL_API` variable to `False`.
    * If you use the experimental Airflow REST API, no changes are needed. The `USE_EXPERIMENTAL_API` variable is already set to `True`.



**Note:** The Airflow database in Airflow versions before 2.3.0 limits the length of the email field to 64 characters. Service accounts sometimes have email addresses that are longer than 64 characters. To access Airflow REST API with such a service account, use the workaround described in [Access Airflow REST API using a service account](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-api#long-service-account-email).
    
    
    from google.auth.transport.requests import Request
    from google.oauth2 import id_token
    import requests
    
    
    IAM_SCOPE = "https://www.googleapis.com/auth/iam"
    OAUTH_TOKEN_URI = "https://www.googleapis.com/oauth2/v4/token"
    # If you are using the stable API, set this value to False
    # For more info about Airflow APIs see https://cloud.google.com/composer/docs/access-airflow-api
    USE_EXPERIMENTAL_API = True
    
    
    def trigger_dag(data, context=None):
        """Makes a POST request to the Composer DAG Trigger API
    
        When called via Google Cloud Functions (GCF),
        data and context are Background function parameters.
    
        For more info, refer to
        https://cloud.google.com/functions/docs/writing/background#functions_background_parameters-python
    
        To call this function from a Python script, omit the ``context`` argument
        and pass in a non-null value for the ``data`` argument.
    
        This function is currently only compatible with Composer v1 environments.
        """
    
        # Fill in with your Composer info here
        # Navigate to your webserver's login page and get this from the URL
        # Or use the script found at
        # https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/composer/rest/get_client_id.py
        client_id = "YOUR-CLIENT-ID"
        # This should be part of your webserver's URL:
        # {tenant-project-id}.appspot.com
        webserver_id = "YOUR-TENANT-PROJECT"
        # The name of the DAG you wish to trigger
        dag_name = "composer_sample_trigger_response_dag"
    
        if USE_EXPERIMENTAL_API:
            endpoint = f"api/experimental/dags/{dag_name}/dag_runs"
            json_data = {"conf": data, "replace_microseconds": "false"}
        else:
            endpoint = f"api/v1/dags/{dag_name}/dagRuns"
            json_data = {"conf": data}
        webserver_url = "https://" + webserver_id + ".appspot.com/" + endpoint
        # Make a POST request to IAP which then Triggers the DAG
        make_iap_request(webserver_url, client_id, method="POST", json=json_data)
    
    
    # This code is copied from
    # https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/iap/make_iap_request.py
    # START COPIED IAP CODE
    def make_iap_request(url, client_id, method="GET", **kwargs):
        """Makes a request to an application protected by Identity-Aware Proxy.
        Args:
          url: The Identity-Aware Proxy-protected URL to fetch.
          client_id: The client ID used by Identity-Aware Proxy.
          method: The request method to use
                  ('GET', 'OPTIONS', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE')
          **kwargs: Any of the parameters defined for the request function:
                    https://github.com/requests/requests/blob/master/requests/api.py
                    If no timeout is provided, it is set to 90 by default.
        Returns:
          The page body, or raises an exception if the page couldn't be retrieved.
        """
        # Set the default timeout, if missing
        if "timeout" not in kwargs:
            kwargs["timeout"] = 90
    
        # Obtain an OpenID Connect (OIDC) token from metadata server or using service
        # account.
        google_open_id_connect_token = id_token.fetch_id_token(Request(), client_id)
    
        # Fetch the Identity-Aware Proxy-protected URL, including an
        # Authorization header containing "Bearer " followed by a
        # Google-issued OpenID Connect token for the service account.
        resp = requests.request(
            method,
            url,
            headers={"Authorization": "Bearer {}".format(google_open_id_connect_token)},
            **kwargs,
        )
        if resp.status_code == 403:
            raise Exception(
                "Service account does not have permission to "
                "access the IAP-protected application."
            )
        elif resp.status_code != 200:
            raise Exception(
                "Bad response from application: {!r} / {!r} / {!r}".format(
                    resp.status_code, resp.headers, resp.text
                )
            )
        else:
            return resp.text
    
    
    # END COPIED IAP CODE
    

## Test your function

To check that your function and DAG work as intended:

  1. Wait until your function deploys.
  2. Trigger the function according to the specified trigger. You can also trigger the function manually by selecting the **Test the function** action for it in Google Cloud console.
  3. Check the DAG page [in the Airflow web interface](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-web-interface). The DAG should have one active or already completed DAG run.
  4. In the Airflow UI, check task logs for this run. You should see that the `print_gcs_info` task outputs the data received from the function to the logs:



Example output:
    
    
    [2021-04-04 18:25:44,778] {bash_operator.py:154} INFO - Output:
    [2021-04-04 18:25:44,781] {bash_operator.py:158} INFO - Triggered from GCF:
        {bucket: example-storage-for-gcf-triggers, contentType: text/plain,
        crc32c: dldNmg==, etag: COW+26Sb5e8CEAE=, generation: 1617560727904101,
        ... }
    [2021-04-04 18:25:44,781] {bash_operator.py:162} INFO - Command exited with
        return code 0h
    

## What's next

  * [Access Airflow UI](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-web-interface)
  * [Access Airflow REST API](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-api)
  * [Write DAGs](https://docs.cloud.google.com/composer/docs/composer-1/write-dags)
  * [Write Cloud Run functions](https://docs.cloud.google.com/functions/docs/writing)
  * [Cloud Storage triggers](https://docs.cloud.google.com/functions/docs/calling/storage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 

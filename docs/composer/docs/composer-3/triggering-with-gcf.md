---
url: https://docs.cloud.google.com/composer/docs/composer-3/triggering-with-gcf/
title: Trigger Managed Service for Apache Airflow DAGs with Cloud Run functions and Airflow REST API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:13.904438+00:00
---

# Trigger Managed Service for Apache Airflow DAGs with Cloud Run functions and Airflow REST API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/triggering-with-gcf/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Trigger Managed Service for Apache Airflow DAGs with Cloud Run functions and Airflow REST API Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/triggering-with-gcf "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/triggering-with-gcf "View this page for Managed Airflow \(Legacy Gen 1\)")

This page describes how to use Cloud Run functions to trigger Managed Service for Apache Airflow DAGs in response to events.

Apache Airflow is designed to run DAGs on a regular schedule, but you can also trigger DAGs in response to events. One way to do this is to use [Cloud Run functions](https://docs.cloud.google.com/functions/docs/concepts/overview) to trigger Managed Airflow DAGs when a specified event occurs.

You can also:

  * [Trigger DAGs using only the Airflow REST API](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-api).
  * Create a function that [triggers a DAG when a message is pushed to a Pub/Sub topic](https://docs.cloud.google.com/composer/docs/composer-3/triggering-gcf-pubsub).



The example in this guide demonstrates a function that triggers a DAG in response to an event:

  1. You configure triggers for your function in Cloud Run functions.
  2. When the function is triggered, it makes a request to trigger a DAG through the Airflow REST API of your Managed Airflow environment. The request contains event's identifier and type, and the event's payload.
  3. Airflow processes this request and runs the DAG specified in the request. The DAG outputs the data that was passed to it from the function.



## Before you begin

This section lists preparatory steps.

### Check your environment's networking configuration

This solution does not work in Private IP and VPC Service Controls configurations because it isn't possible to configure connectivity from Cloud Run functions to the Airflow web server in these configurations.

In Managed Airflow (Gen 3), you can use another approach: [Trigger DAGs using Cloud Run functions and Pub/Sub Messages](https://docs.cloud.google.com/composer/docs/composer-3/triggering-gcf-pubsub).

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

### Allow API calls to Airflow REST API using web server network access control

Cloud Run functions can reach out to the Airflow REST API through a **IPv4 or IPv6 address**.

If you are not sure what will be the calling IP range then use a default configuration option in **Webserver Access Control** which is `All IP addresses have access (default)` to not accidentally block your Cloud Run functions. You can always [configure web server network access later](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface#network-access-controls).

### Get the Airflow web server URL

This example makes REST API requests to the Airflow web server endpoint. You use the URL of the Airflow web server in your Cloud Function code. 

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



## Upload a DAG to your environment

[Upload a DAG to your environment](https://docs.cloud.google.com/composer/docs/composer-3/manage-dags#add). The following example DAG outputs the received DAG run configuration. You trigger this DAG from a function, which you create later in this guide.

###  Airflow 3 
    
    
    import datetime
    
    import airflow
    from airflow.providers.standard.operators.bash import BashOperator
    
    with airflow.DAG(
            'composer_sample_trigger_response_dag',
            start_date=datetime.datetime(2026, 1, 1),
            # Not scheduled, trigger only
            schedule=None) as dag:
    
        # Print the dag_run's configuration, which includes information about the
        # Cloud Storage object change.
        print_gcs_info = BashOperator(
            task_id='print_gcs_info', bash_command='echo {{ dag_run.conf }}}}')
    

###  Airflow 2 
    
    
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

You can deploy a function using your preferred language supported by Cloud Run functions or Cloud Run. This tutorial demonstrates a Cloud Function implemented in [Python](https://docs.cloud.google.com/functions/docs/deploying/console) and [Java](https://docs.cloud.google.com/composer/docs/composer-3/functions/docs/securing/authenticating#functions-bearer-token-example-java).

### Specify function configuration parameters

  * **Trigger** : Select an Eventarc trigger or several triggers for your function.

For more information about creating triggers, see [Create triggers with Eventarc](https://docs.cloud.google.com/run/docs/triggering/trigger-with-events). For example, you can [trigger functions from Cloud Storage using Eventarc](https://docs.cloud.google.com/run/docs/tutorials/trigger-functions-storage).

**Caution:** Don't use Managed Airflow environment buckets as resources in your function's triggers because this might cause the function to trigger several times per second.
  * **Service account** : The service account that you specify for the trigger must have enough permissions to trigger DAGs in Managed Airflow environments.

We recommend to follow the minimum privilege principle and grant only the **Composer User** (`composer.user`) role to it. For more information about configuring permissions, see [Roles and permissions for Cloud Run targets](https://docs.cloud.google.com/eventarc/docs/roles-permissions).

  * **Function entry point** :

    * _(Python)_ When adding code for this example, select the **Python 3.10** or later runtime and specify `trigger_dag_with_gcf` as the entry point.

    * _(Java)_ When adding code for this example, select the **Java 17** or runtime and specify `functions.TriggerDagExample` as the entry point.




### Add requirements

###  Python 

Specify the dependencies in the `requirements.txt` file:
    
    
    google-auth>=2.38.0
    requests>=2.34.2
    functions-framework==3.*
    

###  Java 

Add the following dependencies to `dependencies` section in the `pom.xml`:
    
    
        <dependency>
          <groupId>com.google.apis</groupId>
          <artifactId>google-api-services-docs</artifactId>
          <version>v1-rev20250917-2.0.0</version>
        </dependency>
        <dependency>
          <groupId>com.google.api-client</groupId>
          <artifactId>google-api-client</artifactId>
          <version>2.9.0</version>
        </dependency>
        <dependency>
          <groupId>com.google.auth</groupId>
          <artifactId>google-auth-library-credentials</artifactId>
          <version>1.49.0</version>
        </dependency>
        <dependency>
          <groupId>com.google.auth</groupId>
          <artifactId>google-auth-library-oauth2-http</artifactId>
          <version>1.49.0</version>
        </dependency>
    

### Add function code

###  Python 

Put the following code to the `main.py` file:

  * Replace the value of the `web_server_url` variable with the Airflow web server address that you obtained earlier.

  * _(Airflow 3)_ Replace the value of the `airflow_major_version` variable with `3`, which is the major version of Airflow in your environment.

  * If you are triggering a different DAG, replace the value of the `dag_id` variable.



    
    
    from __future__ import annotations
    
    from typing import Any
    
    from datetime import datetime, timezone
    import google.auth
    from google.auth.transport.requests import AuthorizedSession
    import requests
    import functions_framework
    
    # Following Google Cloud best practices, these credentials should be
    # constructed at start-up time and used throughout
    # https://cloud.google.com/apis/docs/client-libraries-best-practices
    AUTH_SCOPE = "https://www.googleapis.com/auth/cloud-platform"
    CREDENTIALS, _ = google.auth.default(scopes=[AUTH_SCOPE])
    
    def make_managed_airflow_web_server_request(
        url: str, method: str = "GET", **kwargs: Any
    ) -> google.auth.transport.Response:
        """
        Make a request to environment's web server.
        Args:
          url: The URL to fetch.
          method: The request method to use ('GET', 'OPTIONS', 'HEAD', 'POST',
          'PUT', 'PATCH', 'DELETE')
          **kwargs: Any of the parameters defined for the request function:
                    https://github.com/requests/requests/blob/master/requests/api.py
                      If no timeout is provided, it is set to 90 by default.
        """
    
        authed_session = AuthorizedSession(CREDENTIALS)
    
        # Set the default timeout, if missing
        if "timeout" not in kwargs:
            kwargs["timeout"] = 90
    
        return authed_session.request(method, url, **kwargs)
    
    def trigger_dag_request(web_server_url: str, airflow_version: str, dag_id: str, data: dict, logical_date: str) -> str:
        """
        Make a request to trigger a dag using the Airflow REST API.
        https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html
    
        Args:
          web_server_url: The URL of the Airflow web server.
          airflow_version: Major version of Airflow. Determines the API endpoint.
          dag_id: The DAG ID.
          data: Additional configuration parameters for the DAG run (json).
          logical_date: Data interval for which to run the DAG.
        """
    
        if airflow_version == "2":
            endpoint = f"api/v1/dags/{dag_id}/dagRuns"
        elif airflow_version == "3":
            endpoint = f"api/v2/dags/{dag_id}/dagRuns"
        else:
            raise ValueError(
              f"Invalid Airflow version: {airflow_version}. Expected: 2 or 3.")
    
        request_url = f"{web_server_url}/{endpoint}"
        json_data = {
            "conf": data,
            "logical_date": logical_date,
        }
    
        response = make_managed_airflow_web_server_request(
            request_url, method="POST", json=json_data
        )
    
        if response.status_code == 403:
            raise requests.HTTPError(
                "You do not have a permission to perform this operation. "
                "Check Airflow RBAC roles for your account."
                f"{response.headers} / {response.text}"
            )
        elif response.status_code != 200:
            response.raise_for_status()
        else:
            return response.text
    
    @functions_framework.cloud_event
    def trigger_dag_with_gcf(cloud_event: CloudEvent) -> None:
        """
        Entry point for the Cloud Function. Triggers a DAG and passes event data.
        """
    
        # cloud_event.data contains the resource payload (e.g., storage object
        # details or pub/sub body)
        event_data = {
            "id": cloud_event["id"],
            "subject": cloud_event["subject"],
            "type": cloud_event["type"],
            "data": cloud_event.data
        }
    
        # TODO(developer): replace with your values
        # Replace web_server_url with the Airflow web server address. To obtain this
        # URL, run the following command for your environment:
        # gcloud composer environments describe example-environment \
        #  --location=your-composer-region \
        #  --format="value(config.airflowUri)"
        web_server_url = (
            "https://example-airflow-ui-url-dot-us-central1.composer.googleusercontent.com"
        )
    
        # TODO(developer): If your environment uses Airflow 3, replace with "3"
        airflow_major_version = "2"
    
        # Replace with the ID of the DAG that you want to run.
        dag_id = "composer_sample_trigger_response_dag"
    
        # The data interval for which to run the DAG
        # Format example: "2026-07-15T15:00:00Z"
        now = datetime.now(timezone.utc)
        logical_date = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    
        trigger_dag_request(web_server_url, airflow_major_version, dag_id, event_data, logical_date)
    

###  Java 

Put the following code to the `TriggerDagExample.java` file (put this file to `src/main/java/gcfv2/` directory):

  * Replace the value of the `webServerUrl` variable with the Airflow web server address that you obtained earlier.

  * _(Airflow 3)_ Replace the value of the `majorAirflowVersion` variable with `3`, which is the major version of Airflow in your environment.

  * If you are triggering a different DAG, replace the value of the `dagName` variable.



    
    
    package gcfv2;
    
    import com.google.api.client.http.[GenericUrl](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.GenericUrl.html);
    import com.google.api.client.http.[HttpContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpContent.html);
    import com.google.api.client.http.[HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html);
    import com.google.api.client.http.[HttpRequestFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestFactory.html);
    import com.google.api.client.http.[HttpResponse](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponse.html);
    import com.google.api.client.http.[HttpResponseException](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponseException.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.http.json.[JsonHttpContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.json.JsonHttpContent.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import com.google.cloud.functions.CloudEventsFunction;
    import com.google.gson.Gson;
    import io.cloudevents.CloudEvent;
    import java.nio.charset.StandardCharsets;
    import java.time.Instant;
    import java.util.logging.Logger;
    import java.util.HashMap;
    import java.util.Map;
    
    /**
     * Function that triggers an Airflow DAG in response to an event ad passes data.
     */
    public class TriggerDagExample implements CloudEventsFunction {
      private static final Logger logger = Logger.getLogger(TriggerDagExample.class.getName());
    
      @Override
      public void accept(CloudEvent event) throws Exception{
    
        // TODO(developer): replace with your values
        // Replace webServerUrl with the Airflow web server address. To obtain this
        // URL, run the following command for your environment:
        // gcloud composer environments describe example-environment \
        //  --location=your-composer-region \
        //  --format="value(config.airflowUri)"
        String webServerUrl = "https://example-airflow-ui-url-dot-us-central1.composer.googleusercontent.com";
        // TODO(developer): If your environment uses Airflow 3, replace with "3"
        String majorAirflowVersion = "2";
    
        String apiVersion = switch (majorAirflowVersion) {
          case "2" -> "v1";
          case "3" -> "v2";
          default  -> throw new IllegalArgumentException("Invalid Airflow version: " + majorAirflowVersion);
        };
    
        String dagName = "composer_sample_trigger_response_dag";
        String url = String.format("%s/api/%s/dags/%s/dagRuns", webServerUrl, apiVersion, dagName);
    
        logger.info(String.format("Triggering DAG %s as a result of an event on the object %s.",
          dagName, event.getSubject()));
        logger.info(String.format("Triggering DAG through the following URL: %s", url));
    
        [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) googleCredentials = [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html).[getApplicationDefault](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html#com_google_auth_oauth2_GoogleCredentials_getApplicationDefault__)()
            .createScoped("https://www.googleapis.com/auth/cloud-platform");
        [HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html) credentialsAdapter = new [HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html)(googleCredentials);
        [HttpRequestFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestFactory.html) requestFactory =
          new [NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html)().[createRequestFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport.html#com_google_api_client_http_HttpTransport_createRequestFactory__)(credentialsAdapter);
    
        Map<String, Object> conf = new HashMap<>();
    
        conf.put("id", event.getId());
        conf.put("subject", event.getSubject());
        conf.put("type", event.getType());
    
        if (event.getData() != null) {
          String dataJson = new String(event.getData().toBytes(), StandardCharsets.UTF_8);
          Gson gson = new Gson();
          Map<String, Object> dataMap = gson.[fromJson](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.ClientId.html#com_google_auth_oauth2_ClientId_fromJson_java_util_Map_java_lang_String_java_lang_Object__)(dataJson, Map.class);
          conf.put("data", dataMap);
        }
    
        String currentUtcTime = Instant.now().toString();
    
        Map<String, Object> json = new HashMap<>();
        json.put("conf", conf);
        json.put("logical_date", currentUtcTime);
    
        [HttpContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpContent.html) content = new [JsonHttpContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.json.JsonHttpContent.html)(new [GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html)(), json);
        [HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html) request = requestFactory.[buildPostRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestFactory.html#com_google_api_client_http_HttpRequestFactory_buildPostRequest_com_google_api_client_http_GenericUrl_com_google_api_client_http_HttpContent_)(new [GenericUrl](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.GenericUrl.html)(url), content);
        request.[getHeaders](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html#com_google_api_client_http_HttpRequest_getHeaders__)().setContentType("application/json");
    
        [HttpResponse](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponse.html) response = null;
        try {
          response = request.[execute](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html#com_google_api_client_http_HttpRequest_execute__)();
          int statusCode = response.[getStatusCode](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponse.html#com_google_api_client_http_HttpResponse_getStatusCode__)();
          logger.info("Response code: " + statusCode);
          logger.info(response.[parseAsString](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponse.html#com_google_api_client_http_HttpResponse_parseAsString__)());
        } catch ([HttpResponseException](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponseException.html) e) {
          logger.info("Received HTTP exception");
          logger.info(e.getLocalizedMessage());
          logger.info("- 400 error: wrong arguments passed to Airflow API");
          logger.info("- 401 error: check if service account has Composer User role");
          logger.info("- 403 error: check Airflow RBAC roles assigned to service account");
          logger.info("- 404 error: check Web Server URL");
        } catch (Exception e) {
          logger.info("Received exception");
          logger.info(e.getLocalizedMessage());
        } finally {
          // Safely close and release the HTTP connection pool resource
          if (response != null) {
            try {
              response.[disconnect](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponse.html#com_google_api_client_http_HttpResponse_disconnect__)();
            } catch (Exception e) {
              logger.warning("Failed to disconnect response: " + e.getMessage());
            }
          }
        }
      }
    }
    

## Test your function

To check that your function and DAG work as intended:

  1. Wait until your function deploys.
  2. Trigger the function according to the specified trigger. You can also trigger the function manually by selecting the **Test the function** action for it in Google Cloud console.
  3. Check the DAG page [in the Airflow web interface](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface). The DAG should have one active or already completed DAG run.
  4. In the Airflow UI, check task logs for this run. You should see that the `print_gcs_info` task outputs the data received from the function to the logs:



Example command to test the function:
    
    
    curl -X POST "https://service-id.region.run.app" \
    -H "Authorization: bearer $(gcloud auth print-identity-token)" \
      -X POST \
      -H "Content-Type: application/json" \
      -H "ce-id: 1234567890" \
      -H "ce-specversion: 1.0" \
      -H "ce-type: google.cloud.storage.object.v1.finalized" \
      -H "ce-source: //storage.googleapis.com/projects/_/buckets/example-bucket" \
      -d '{
        "name": "example-file.csv",
        "bucket": "example-bucket"
      }'
    

Example output:
    
    
    [2026-07-14, 15:10:12 UTC] {subprocess.py:88} INFO - Running command: ['/usr/bin/bash', '-c', "echo {'data': {'name': 'example-file.csv', 'bucket': 'example-bucket'}, 'id': '1234567890', 'type': 'google.cloud.storage.object.v1.finalized'}"]
    [2026-07-14, 15:10:12 UTC] {subprocess.py:99} INFO - Output:
    [2026-07-14, 15:10:12 UTC] {subprocess.py:106} INFO - {data: {name: example-file.csv, bucket: my-bucket}, id: 1234567890, type: google.cloud.storage.object.v1.finalized}
    [2026-07-14, 15:10:12 UTC] {subprocess.py:110} INFO - Command exited with return code 0
    
    [2026-07-15, 10:06:32 UTC] {subprocess.py:88} INFO - Running command: ['/usr/bin/bash', '-c', "echo {'id': '1234567890', 'subject': 'objects/example-file.csv', 'type': 'google.cloud.storage.object.v1.finalized', 'data': {'name': 'example-file.csv', 'bucket': 'example-bucket'}}"]
    [2026-07-15, 10:06:32 UTC] {subprocess.py:99} INFO - Output:
    [2026-07-15, 10:06:32 UTC] {subprocess.py:106} INFO - {id: 1234567890, subject: objects/example-file.csv, type: google.cloud.storage.object.v1.finalized, data: {name: example-file.csv, bucket: example-bucket}}
    [2026-07-15, 10:06:32 UTC] {subprocess.py:110} INFO - Command exited with return code 0
    

Troubleshooting:

  * If your function fails with a `NullPointerException: Null data` error and the stack trace points to the `BackgroundFunctionExecutor.parseLegacyEvent` function, it means that the event received by the function doesn't have standard `CloudEvent` metadata headers. The function assumes you are sending a legacy background event, tries to parse the `data` field from it, and fails. This might happen, for example, if you send an arbitrary event payload when you test the function.
  * If your function fails with `500 Internal Server Error: The server encountered an internal error and was unable to complete your request.`, double-check the value of the `airflow_major_version` variable. This variable determines the Airflow REST API endpoint, which is different in Airflow 2 and Airflow 3.



## What's next

  * [Access Airflow UI](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface)
  * [Access Airflow REST API](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-api)
  * [Write DAGs](https://docs.cloud.google.com/composer/docs/composer-3/write-dags)
  * [Write Cloud Run functions](https://docs.cloud.google.com/functions/docs/writing)
  * [Cloud Storage triggers](https://docs.cloud.google.com/functions/docs/calling/storage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

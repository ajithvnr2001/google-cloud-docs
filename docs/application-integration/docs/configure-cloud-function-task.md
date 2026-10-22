---
url: https://docs.cloud.google.com/application-integration/docs/configure-cloud-function-task/
title: Cloud Function task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:47.255258+00:00
---

# Cloud Function task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-cloud-function-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Function task

The **Cloud Function** task lets you configure and run Cloud Run functions from your integration. Cloud Run functions represent the next evolution of Cloud Functions, offering an event-driven programming model with enhanced control and scalability, leveraging the Cloud Run serverless platform. Cloud Run functions provide a single serverless solution for all workload types.

The Cloud Function task supports the following versions of Cloud Run functions:

  * [Cloud Functions (1st gen)](https://docs.cloud.google.com/functions/1stgendocs/concepts/overview)
  * Cloud Run functions created using the [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/reference/rest)



For detailed information about the differences between Cloud Run functions versions, see the [Cloud Functions comparison](https://docs.cloud.google.com/run/docs/functions/comparison) guide.

**Note:** This document uses the terms Cloud Run functions (1st gen), Cloud Functions (1st gen) and, Cloud Functions interchangeably.

## Before you begin

Ensure that you perform the following tasks in your Google Cloud project before configuring the **Cloud Function** task.

  1. To connect to Cloud Function, ensure that you have either [created an OAuth 2.0 profile](https://docs.cloud.google.com/application-integration/docs/configuring-auth-profile#createAuthProfile) or [attached a user-managed service account](https://docs.cloud.google.com/application-integration/docs/access-control#add-service-account) to your integration: 
     * If your integration has a service account attached, assign the **Cloud Function Invoker** IAM role to that service account. 

For information about granting roles to a service account, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).

     * The **Cloud Function** task only supports authentication profiles of type [Google OIDC ID Token](https://docs.cloud.google.com/application-integration/docs/configuring-auth-profile#googleOIDC). Create an authentication profile of type [Google OIDC ID Token](https://docs.cloud.google.com/application-integration/docs/configuring-auth-profile#googleOIDC) using the service account with the **Cloud Functions Invoker** IAM role assigned. If your **Cloud Function** task does not require authentication, the **Authentication profile** field in the task configuration pane can be left empty. 

If your integration has both OIDC ID profile and a user-managed service account configured, then by default the OIDC ID profile is used for authentication. If neither OIDC ID profile nor user-managed service account is configured, then the default service account (`service-PROJECT_NUMBER@gcp-sa-integrations.iam.gserviceaccount.com`) is used to call the **Cloud Function** task.

  2. Ensure that [VPC Service Controls](https://docs.cloud.google.com/application-integration/docs/vpc-service-controls) is **not** set up for Application Integration in your Google Cloud project. **Warning:** **Cloud Function** does not function, or stops functioning, if [VPC Service Controls](https://docs.cloud.google.com/application-integration/docs/vpc-service-controls) is set up for Application Integration in your Google Cloud project. 



## Configure the Cloud Function task

To configure the **Cloud Function** task in your integration, perform the following steps: 

  1. In the navigation menu, click **Integrations**. 

This opens the list of available integrations in the Application Integration UI. 

  2. Select an existing integration or click **Create integration**. 

If you are creating a new integration, enter a name and description in the create dialog, and click **Create**. 

  3. From the **Tasks** drop-down, click **Cloud Function** to place it in the integration editor. 
  4. Click the **Cloud Function** element on the designer to open the configuration pane, then click **Configure Cloud Function**. 
  5. If you are prompted to grant permissions to the service account, click **Grant**. 

Application Integration automatically grants the required permissions to the service account. 

  6. In the **Cloud Function configuration** pane, select one of the following options: 
     * **Link existing function:** Select this option to associate an existing function with your integration. You can link Cloud Functions (1st gen) and Cloud Functions created with the [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/reference/rest) from your integration. 
       * In the **Cloud Function Trigger URL** field, enter the trigger URL of the existing function. 

The URL should follow one of the following formats:
             
             # For Cloud Functions (1st gen)
             https://REGION_NAME-PROJECT_ID.cloudfunctions.net/FUNCTION_NAME
             
             # For Cloud Run functions created using the Cloud Functions v2 API
             https://FUNCTION_NAME-PROJECT_ID.REGION_NAME.run.app

**Important:** Ensure that the source files for the existing Cloud Function adhere to the format specified in the Cloud Function template.
     * **Create new function:** Select this option to create a new function for the integration. 
       1. In the **Function Name** field, enter a unique name for the new Cloud Run functions.
       2. From the **Region** drop-down, select the region where the Cloud Run functions is deployed.
       3. From the **Function Version** dropdown, select the desired Cloud Run functions version: 
          * **Cloud Functions (1st Gen):** This is the legacy version of Cloud Run functions, formerly known as Cloud Functions (1st gen), which uses the `.cloudfunctions.net` endpoint format.
          * **Cloud Functions (Latest Gen):** This is the latest version of Cloud Run functions, created using Cloud Functions v2 API. Built on Cloud Run and Eventarc, it supports extended request timeouts (up to 60 minutes), offers increased concurrency, and uses both `.cloudfunctions.net` and `.run.app` endpoint formats.
For more information about the differences between the two versions, see [Compare Cloud Functions](https://docs.cloud.google.com/functions/docs/concepts/version-comparison). 
  7. Click **Save**. 

Configuring a **Cloud Function** task in Application Integration creates a basic HTTP- triggered Cloud Run functions in your Google Cloud project. 




### Cloud function template

The following samples show how to use the **Cloud Function** task in your integration for different languages.

### Python

When configuring the Cloud Function using an existing Cloud Run functions, make sure that the function's `main.py`, `task.py`, and `requirements.txt` source files are in the following format:

### task.py
    
    
          # Sample Code:
          # print(event.get('task_string_key'))
          # event.set('task_int_array_key', [456, 789]);
          # event.log('some logging')
    
          def run(event):
            """Actual cloud function custom logic.
            Args:
              event : event object in main.py that contains all parameters.
            """
            return
        

### main.py
    
    
          """Un-editable platform wrapper which invokes user code."""
        import traceback
    
        from flask import json
        from flask import jsonify
        from task import run
    
        VALUE_NAME = [
            'stringValue', 'intValue', 'doubleValue', 'booleanValue', 'protoValue'
        ]
        ARRAY_VALUE_NAME = {
            'stringArray': 'stringValues',
            'intArray': 'intValues',
            'doubleArray': 'doubleValues',
            'booleanArray': 'booleanValues',
            'protoArray': 'protoValues'
        }
        VALUE_TYPE_URL = 'type.googleapis.com/google.protobuf.Value'
        CLOUD_FUNCTION_EXCEPTION_KEY = 'CloudFunctionException'
        CLOUD_FUNCTION_LOGGING_KEY = 'CloudFunctionLogging'
    
    
        class _Event(object):
          """Event object."""
    
          def __init__(self, json_payload):
            self._event_params = json_payload.get('eventParameters', dict())
            self._task_params = json_payload.get('taskParameters', dict())
            self._log = []
            print('Event param is ' + str(self._event_params))
            print('Task param is ' + str(self._task_params))
    
          def set(self, key, value):
            """Set the event parameters key-value.
    
            Args:
              key: parameter key.
              value: parameter value.
            """
            new_param = self._create_param(key, value)
            param = self._get_param_by_key(key)
            if param is None:
              if 'parameters' not in self._event_params:
                self._event_params['parameters'] = []
              self._event_params['parameters'].append(new_param)
            else:
              param['value'] = new_param['value']
    
          def _create_param(self, key, value):
            """Create a new parameter with given key value pair.
    
            Args:
              key: parameter key.
              value: parameter value.
    
            Returns:
              parameter.
            """
            new_param = {}
            new_param['key'] = key
            if isinstance(value, str):
              new_param['value'] = {'stringValue': value}
            elif isinstance(value, int):
              new_param['value'] = {'intValue': value}
            elif isinstance(value, float):
              new_param['value'] = {'doubleValue': value}
            elif isinstance(value, bool):
              new_param['value'] = {'booleanValue': value}
            elif isinstance(value, dict):
              if 'type@' in value:
                new_param['value'] = {'protoValue': value}
              else:
                new_param['value'] = {
                    'protoValue': {
                        '@type': 'type.googleapis.com/google.protobuf.Value',
                        'value': value
                    }
                }
            elif isinstance(value, list):
              if not value:
                raise RuntimeError('Cannot create a param with empty list')
              if any(not isinstance(val, type(value[0])) for val in value):
                print('Not all elements in the list have the same type')
                new_param['value'] = {
                    'protoValue': {
                        '@type': 'type.googleapis.com/google.protobuf.Value',
                        'value': value
                    }
                }
              elif isinstance(value[0], str):
                new_param['value'] = {'stringArray': {'stringValues': value}}
              elif isinstance(value[0], int):
                new_param['value'] = {'intArray': {'intValues': value}}
              elif isinstance(value[0], float):
                new_param['value'] = {'doubleArray': {'doubleValues': value}}
              elif isinstance(value[0], bool):
                new_param['value'] = {'booleanArray': {'booleanValues': value}}
              elif isinstance(value[0], dict):
                if all('@type' in val and val['@type'] == value[0]['@type']
                       for val in value):
                  new_param['value'] = {'protoArray': {'protoValues': value}}
                else:
                  new_param['value'] = {
                      'protoValue': {
                          '@type': 'type.googleapis.com/google.protobuf.Value',
                          'value': value
                      }
                  }
              else:
                raise RuntimeError('The type ' + type(value[0]) +
                                   ' in the list is not supported')
            else:
              raise RuntimeError('Value ' + str(value) + ' has the type ' +
                                 type(value) + ' that is not supported')
            return new_param
    
          def get(self, key):
            """Get the event parameter value for specified key.
    
            Args:
              key: parameter key.
    
            Returns:
              Parameter value.
            """
            param = self._get_param_by_key(key)
            if param is None:
              raise RuntimeError('Can not find param with key ' + key)
            return self._get_param_value(param)
    
          def _get_param_by_key(self, key):
            """Get the parameter for specified key.
    
            Args:
              key: parameter key.
    
            Returns:
              Parameter.
            """
            param = self._get_param_by_key_from_params(key, self._task_params)
            if param is None:
              return self._get_param_by_key_from_params(key, self._event_params)
            value = self._get_param_value(param)
            if isinstance(value, str) and len(value) > 2 and value.startswith(
                '$') and value.endswith('$'):
              return self._get_param_by_key_from_params(value[1:-1], self._event_params)
            return param
    
          def _get_param_by_key_from_params(self, key, params):
            """Get the parameter for specified key from event parameters.
    
            Args:
              key: parameter key.
              params: event parameters.
    
            Returns:
              Parameter.
            """
            if not isinstance(params, dict) or 'parameters' not in params:
              return None
            for param in params['parameters']:
              if param['key'] == key:
                return param
            return None
    
          def _get_param_value(self, param):
            """Get the parameter value for specified parameter.
    
            Args:
              param: parameter.
    
            Returns:
              Parameter value.
            """
            value = param['value']
            if len(value) != 1:
              raise RuntimeError('param does not have size of 1')
            for value_name in VALUE_NAME:
              if value_name in value:
                if value_name == 'protoValue' and value[value_name][
                    '@type'] == VALUE_TYPE_URL:
                  return value[value_name]['value']
                return value[value_name]
            for array_value_name in ARRAY_VALUE_NAME:
              if array_value_name in value:
                return value[array_value_name][ARRAY_VALUE_NAME[array_value_name]]
            raise RuntimeError('Cannot get value from param ' + str(param))
    
          def set_error(self):
            """Set the cloud function error to event parameters in order for user to see on IP."""
    
            self.set(CLOUD_FUNCTION_EXCEPTION_KEY, traceback.format_exc())
    
          def log(self, message):
            self._log.append(str(message))
    
          def get_response(self):
            """Get the response that can be returned to IP.
    
            Returns:
              The response text or any set of values that can be turned into a
              Response object using
              `make_response
              <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
            """
            if self._log:
              self.set(CLOUD_FUNCTION_LOGGING_KEY, self._log)
            res = {
                'eventParameters': self._event_params,
            }
            return jsonify(res)
    
    
        def execute_function(request):
          """Entry point of the cloud function.
    
          Args:
            request (flask.Request): HTTP request object.
    
          Returns:
            The response text or any set of values that can be turned into a
            Response object using
            `make_response
            <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
          """
          try:
            request_json = request.get_json(silent=True)
            event = _Event(request_json)
            run(event)
          except:
            event.set_error()
          return event.get_response()
    
        

### requirements.txt
    
    
        # Function dependencies, for example:
        # package>=version
        

For more information about response format, see [ValueType](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/ValueType).

### Java

The following sample shows how to use the **Cloud Function** task in your integration. Ensure that the response follows the supported JSON format as described in the sample:
    
    
    private static final Gson gson = new Gson();
    
    @Override
    public void service(HttpRequest request, HttpResponse response) throws Exception {
      JsonObject body = gson.fromJson(request.getReader(), JsonObject.class);
    
      JsonArray resParams = new JsonArray();
      for (JsonElement param: body.getAsJsonObject("eventParameters").getAsJsonArray("parameters")) {
        if (param.getAsJsonObject().get("key").getAsString().equals("input")) {
          JsonObject newParam= new JsonObject();
          newParam.addProperty("key", "input");
          JsonObject value = new JsonObject();
          value.addProperty("stringValue","2");
          newParam.add("value", value);
          resParams.add(newParam);
        } else {
          resParams.add(param);
        }
      }
      JsonObject parameters = new JsonObject();
      parameters.add("parameters", resParams);
      JsonObject res = new JsonObject();
      res.add("eventParameters", parameters);
      System.out.println(res);
      BufferedWriter writer = response.getWriter();
      writer.write(res.toString());
    }

For more information about response format, see [ValueType](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/ValueType).

### Javascript

The following sample shows how to use the **Cloud Function** task in your integration. Ensure that the response follows the supported JSON format as described in the sample:
    
    
    const functions = require('@google-cloud/functions-framework');
    
    functions.http('execute_function', (req, res) => {
      console.log(JSON.stringify(req.body));
      let response = {"eventParameters":{"parameters":[{"key":"input","value":{"stringValue":"2"}}]}};
      res.send(JSON.stringify(response));
    });

For more information about response format, see [ValueType](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/ValueType).

### PHP

The following sample shows how to use the **Cloud Function** task in your integration. Ensure that the response follows the supported JSON format as described in the sample:
    
    
    use Psr\Http\Message\ServerRequestInterface;
    function execute_function(ServerRequestInterface $request)
    {
      return '{"eventParameters":{"parameters":[{"key":"input","value":{"stringValue":"2"}}]}}';
    }

For more information about response format, see [ValueType](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/ValueType).

## Edit a Cloud Function task

Application Integration directs you to the appropriate Google Cloud console page to edit the Cloud Run functions based on the version type.

### Cloud Functions (1st gen)

To edit a Cloud Function task that is configured using the Cloud Functions (1st gen) version, perform the following steps:

  1. In the task configuration pane, click **Open Cloud Function**. 

You are directed to the **Cloud Functions (1st gen) > Function details** page in your Google Cloud console. 

  2. Click **Edit**.
  3. On the **Edit function** page, the **Configuration** step lets you edit the default configuration settings of the Cloud Function. See [Configuring Cloud Functions](https://cloud.google.com/functions/docs/configuring) for more information.
  4. Click **Next** to proceed to the **Code** step and edit the Cloud Function's source code. 

By default, the Cloud Function contains the following source files: 

     * _main.py_ : This file contains the initialization code to run the Cloud Function from your integration. **Caution:** Do not edit or modify the _main.py_ file. 
     * _task.py_ : This file contains the executable code of the Cloud Function. Write your script inside the `run(event)` function. This function is called when the Cloud Function task executes. The `event` object from the _main.py_ file contains all the task parameters. 

See Access integration variables for information about how to use the variables defined at the integration level in your script. 

  5. Click **Deploy**.



### Cloud Run functions

To edit a Cloud Function task that is configured using the Cloud Functions (Latest Gen) version, perform the following steps:

  1. In the task configuration pane, click **Open Cloud Function**. 

You are redirected to the **Cloud Run functions > Service details** page in your Google Cloud console. 

  2. On the **Source** tab, click **Edit source** to edit the source code files of the Cloud Run functions. 

By default, the Cloud Run functions contain the following source files: 

     * _main.py_ : This file contains the initialization code to run the Cloud Functions from your integration. **Caution:** Do not edit or modify the _main.py_ file. 
     * _task.py_ : This file contains the executable code of the Cloud Functions. Write your script inside the `run(event)` function. This function is called when the Cloud Run functions task executes. The `event` object from the _main.py_ file contains all the task parameters. 

See Access integration variables for information about how to use the variables defined at the integration level in your script. 

  3. Click **Save and redeploy**.



## Access integration variables

To access an integration variable in your Cloud Function, pass the variable as task parameter to the **Cloud Function** task. The task parameter is a key-value pair where **Key** is the name of the reference variable used in your Cloud Function source file and the **Value** is the corresponding integration variable name that the reference variable points to. You can add one or more task parameters in the **Task parameters** section of the task configuration pane. 

The following methods are used to access integration variables from your Cloud Function: 

  * **set** : Writes the value to a variable.
  * **get** : Reads the value of a variable.



For example, if you have an integration variable named EmployeeName that you want to use in your Cloud Function source file, define the following task parameters: 

  * **Key** : EmployeeKey
  * **Value** : EmployeeName



The following sample script shows the usage of set and get functions to access the defined integration variables. 
    
    
    def run(event):  
      # Read the integration variable EmployeeName using the reference variable EmployeeKey
      value = event.get('EmployeeKey');
      # Change the integration variable EmployeeName value using the reference variable EmployeeKey
      event.set('EmployeeKey' , 'XYZ');
      # The new value of the integration variable is retained throughout the Cloud Function task.
      return

## Error handling strategy

An error handling strategy for a task specifies the action to take if the task fails due to a [temporary error](https://docs.cloud.google.com/application-integration/docs/error-handling). For information about how to use an error handling strategy, and to know about the different types of error handling strategies, see [Error handling strategies](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy). 

## SLA exclusions

The Cloud Function task has a dependency on the [Google Cloud Functions](https://docs.cloud.google.com/functions/docs/concepts/overview) product. Because this dependency is external to Application Integration, all executions of `active` integrations that fail because of the failure in the Cloud Function task are excluded from the [Application Integration Service Level Agreement (SLA)](https://cloud.google.com/application-integration/sla) terms and conditions.

## Quotas and limits

The **Cloud Function** task has an execution timeout limit of **2 minutes (120 seconds)**. If the invoked function takes longer than 2 minutes to complete and respond, the task fails with an execution timeout error (`TIMEOUT_WEB`).

**Caution:** Even if the underlying Cloud Run functions is configured with a longer request timeout (e.g., up to 60 minutes) or your integration runs with an asynchronous (`ASYNC`) execution strategy, the **Cloud Function** task waits synchronously for the HTTP response and times out after 2 minutes. 

If your workload requires execution times longer than 2 minutes, consider the following workarounds:

  * **Asynchronous trigger using Pub/Sub:** Use a Pub/Sub task or connector in your integration to publish an event message, and configure your Cloud Run functions to trigger asynchronously from the Pub/Sub topic subscription to process the workload in the background.
  * **Immediate HTTP acknowledgment and asynchronous callback:** Configure your HTTP-triggered Cloud Run functions to return an immediate HTTP `200 OK` response upon receiving the request, process the long-running task asynchronously in the background, and optionally invoke an Application Integration API trigger endpoint to resume downstream integration steps once processing is complete.



For information about general quotas and limits for both Cloud Run functions and Cloud Functions (1st gen), see [Configuration Comparison](https://docs.cloud.google.com/run/docs/functions/comparison#configuration).

## What's next

  * Learn about [all tasks and triggers](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks).
  * Learn how to [test and publish an integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).
  * Learn about [error handling](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy).
  * Learn about [integration execution logs](https://docs.cloud.google.com/application-integration/docs/introduction-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

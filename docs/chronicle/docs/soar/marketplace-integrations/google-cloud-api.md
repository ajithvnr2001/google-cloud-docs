---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-api/
title: Google Cloud API \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:04.621370+00:00
---

# Google Cloud API  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google Cloud API

This document provides guidance to help you configure and integrate Google Cloud API with Google Security Operations.

## Use cases

The **Google Cloud API** integration uses Google SecOps capabilities to support the following use cases:

  * **Automated resource management** : Execute actions across Google Cloud services like Compute Engine or Cloud Storage to remediate threats or manage infrastructure dynamically.

  * **Identity and access governance** : Programmatically adjust Identity and Access Management policies or roles in response to detected security incidents.

  * **Custom API orchestration** : Interact with any enabled Google Cloud API that does not have a dedicated integration, providing maximum flexibility for complex playbooks.

  * **Keyless authentication** : Securely access Google Cloud resources using Workload Identity to eliminate the risks associated with static service account keys.




## Before you begin

Before you configure the integration in the Google SecOps platform, verify that you have the following:

  * **Target APIs enabled** : Identify and enable the specific Google Cloud services you plan to automate.

  * **IAM permissions** : Ensure your identity has the necessary roles for the specific actions you intend to perform.

  * **Authentication method** : Choose between the recommended Workload Identity or a service account JSON key for authentication.




### Identify and enable target APIs

Because this integration is a generic gateway, there are no fixed APIs. Requirements depend on your specific use case. You must enable the target APIs (such as Compute Engine, Cloud Storage, or IAM) in your project to execute them through the integration.

Use the following procedure to identify and enable the target APIs:

  1. In the Google Cloud console, go to **APIs & Services > Library**.

  2. Search for and enable the required services.




### Configure IAM permissions

The service account or identity used by this integration must have the appropriate IAM roles.

  * **Principle of least privilege** : Grant only the specific roles necessary for your intended API calls.

  * **Dynamic requirements** : Permissions vary based on the operation. For example, managing resources requires different roles than listing them.




### Select an authentication method

Google SecOps supports two authentication paths for this integration:

  * Option 1: Workload Identity (recommended)

  * Option 2: Service account JSON key




#### Authenticate using a Workload Identity (recommended)

Workload Identity is the most secure method because it eliminates the need to manage or rotate long-lived JSON keys. It utilizes service account impersonation to allow the platform to securely access your resources.

##### Identify the Google SecOps instance identity

Follow these steps to find the unique identity for your instance:

  1. In Google SecOps, go to **Content Hub > Response Integrations**.

  2. Select the **Google Cloud API** integration.

  3. Enter the target service account email into the **Workload Identity Email** field.

  4. Click **Save** and then click **Test**. The test is expected to fail.

  5. Click close_small to the right of **Test** and search the error message for the identity email beginning with `gke-init-python@...` or `soar-python@...`.

  6. Copy this unique email address.




##### Grant impersonation permissions

Authorize the instance identity to access your resources by completing these steps:

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select the target service account and go to **Permissions > Grant Access**.

  3. Paste the unique email address into the **New principals** field and assign the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`).

**Note:** It may take a few minutes after completing this step for the test to pass.



#### Authenticate using a JSON key

Only use this method if Workload Identity isn't available in your environment.

Use the following procedure to authenticate the integration using a service account JSON key:

  1. In the Google Cloud console, create a service account.

  2. Go to the **Keys** tab and select **Add key > Create new key**.

  3. Select `JSON` as the key type and download the file.

  4. Copy the entire content of this file and paste it into `Service Account Json File Content` during the integration configuration in Google SecOps.




## Integrate Google Cloud API with Google SecOps SOAR

The integration requires the following parameters:

Parameters | Description  
---|---  
`Test URL` | _Optional_ A test URL for validating the authentication to the Google Cloud API. This parameter uses a GET request.  
`Service Account Json File Content` | _Optional_ The content of the service account key JSON file. You can configure either this parameter, the `Workload Identity Email` parameter, or set all the preceding integration parameters. To configure this parameter, provide the full content of the service account key JSON file that you have downloaded when creating a service account. For more information about using service accounts as an authentication method, see [Service accounts overview](https://docs.cloud.google.com/iam/docs/service-account-overview) and [Service account impersonation](https://docs.cloud.google.com/iam/docs/service-account-overview#impersonation).  In this integration, authenticating with the service account key JSON file has a priority over the Workload identity email.  
`Organization ID` | _Optional_ The organization ID to use in the integration. To retrieve the value from this parameter during the action execution, set the following placeholder: `{{org_id}}`.   
`Project ID` | _Optional_ The project ID to use in the integration. To retrieve the value from this parameter during the action execution, set the following placeholder: `{{project_id}}`.  
`Quota Project ID` | _Optional_ The Google Cloud project ID which you use for Google Cloud APIs and billing. This parameter requires you to grant the `Service Usage Consumer` role to your service account. The integration attaches this parameter value to all API requests. If you do not set a value for this parameter, the integration retrieves the project ID from your Google Cloud service account.  
`Workload Identity Email` | _Optional_ The client email address of your Service Account. You can configure either this parameter or the `Service Account Json File Content` parameter. In this integration, authenticating with the service account key JSON file has priority over the Workload identity email. To impersonate service accounts with Workload identity, grant the `Service Account Token Creator` role to the Google SecOps instance identity on your service account. For more details about workload identities and how to work with them, see [Identities for workloads](https://docs.cloud.google.com/iam/docs/workload-identities).  
`OAuth Scopes` | _Optional_ A comma-separated list of OAuth scopes that are required to execute the Google Cloud API requests.  
`Verify SSL` | _Required_ If selected, the integration verifies that the SSL certificate for connecting to the Google Cloud service is valid. Selected by default.  
  
For instructions about configuring an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage if needed. After you configure an integration instance, you can use it in playbooks. For more information about configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Execute HTTP Request

Use the **Execute HTTP Request** action to construct and execute a customized HTTP API request against a target URL.

This action doesn't run on Google SecOps entities. 

#### Action behavior

This action supports complex behaviors including asynchronous polling, dynamic payload construction, and file management.

##### Asynchronous polling

When `Expected Response Values` is provided, the action operates in asynchronous mode. In this mode, the action repeatedly polls the target endpoint to track the state of a response (for example, waiting for a long-running task to complete). 

The action evaluates the response body against the JSON conditions provided in the parameter and continues execution until the conditions are met or the action reaches its timeout.

###### Condition logic

The action supports the following logic for tracking response states:

  * **Single field matching** : The action waits for a specific field to reach a single value.
        
        {
          "state": "finished"
        }
        

  * **Multiple values (OR logic)** : The action stops execution if a field matches any value in a provided list. This is useful for stopping on both "success" and "error" states to avoid unnecessary polling.
        
        {
          "state": ["finished", "error"]
        }
        

  * **Multiple fields (AND logic)** : The action waits until all specified fields match their respective values simultaneously.
        
        {
          "state": "finished",
          "percentage": "100"
        }
        

  * **Combined logic** : You can combine multiple conditions within the JSON object.
        
        {
          "state": ["finished", "error"],
          "percentage": "10"
        }
        




###### JSON parsing behavior

When evaluating conditions, the action follows these rules:

  * **Global search** : The action searches the entire JSON response object for the specified keys. Provide the key name exactly as it appears in the JSON without prepending parent object names or using prefixes (for example, use `"state"`, not `"data_state"` or `"data-state"`).

  * **Multiple identical keys** : If the response contains multiple keys with the same name at different levels of the JSON hierarchy, the expected output is only reached when all matching key names satisfy the identical expected value.

For example, to search for the `finished` state in the JSON response and ignore other states, set all `state` keys in `Expected Response Values` to `finished`:
        
        {
        "data": {
          "state": "finished"
          },
          "state": "finished"
        }
        




##### Body payload construction

The action constructs the request body based on the `Content-Type` header provided in `Headers`. 

This is the `Body Payload` input used for the following construction examples:
    
    
    {
      "Id": "123123",
      "sorting": "asc"
    }
    

  * **`application/x-www-form-urlencoded`** : The action generates the payload as `Id=123123&sorting=asc`.

  * **`application/json`** : The action generates the following JSON payload:
        
        {
          "Id": "123123",
          "sorting": "asc"
        }
        

  * **`XML`** : If the third-party product requires XML, provide an XML-formatted input directly in `Body Payload`:
        
        <?xml version="1.0" encoding="utf-8"?>
        <soap:Envelope xmlns:soap="[http://schemas.xmlsoap.org/soap/envelope/](http://schemas.xmlsoap.org/soap/envelope/)">
        <soap:Body>
          <NumberToWords xmlns="[http://www.dataaccess.com/webservicesserver/](http://www.dataaccess.com/webservicesserver/)">
            <ubiNum>500</ubiNum>
          </NumberToWords>
        </soap:Body>
        </soap:Envelope>
        




##### File handling

The action supports the following workflows for managing files:

  * **Downloading files** :

    * To return file data as part of the JSON result in base64 format, select `Base64 Output`.

    * To save a file directly to the Case Wall as a ZIP archive, select `Save To Case Wall`.

  * **Uploading files** : To upload a file, convert it to a base64-encoded string and include it as part of the `Body Payload` value.

The following example shows an image file converted to a base64-encoded string:
        
        iVBORw0KGgoAAAANSUhEUgAAAOEAAADgCAMAAADCMfHtAAAAvVBMVEX////2yBctLS32xgAAAAASEhLPz8/2xwAfHx8qKiqTk5P1wwD2xw4XFxf///u9vb3w8PAlJSXi4uJBQUH++eb+++z//fP76rH99df98sz64qD64Y/523b41Vr53Hz39/f87bv878T989H3zjH634j76rL3zzz76Kj42GbZ2dn41FCvr68TExM6OjpRUVFmZmb40kiOjo6wsLB8fHxdXV3645j41V9ubm5ISEjGxsahoaFhYWGFhYX53Xn63oxSMwp1AAAMpUlEQVR4nO1da1fiOhemBmg7KWCV+00QBUQdmVHU8Z2Z//+zDpfxgn3SZKdJi+/q8+GctWZJk6fJvmY3u1DIkSNHjhw5cuTIkSNHjq+DZn08brVm3S1ardG4Xc96SqbQHs2GC4dxzj6Bc3c67806zaxnmADt1nDKNsyCwIEI3A1Td7AafUGane5iQ05A7RPRNU1neNnIes7qaLbmLlcjt8dysupkPXUVNLtLzlwSu3eW3B2OsyYgweWCunifwJh70c6ahRDtoaLgSUjy6ayaNReEyylnyeltsRbKi0Mzl9Wua2L53sH443nWpD6g2WOmlu8dAV8ejGq1we8fx4PQrDPXDr8dx0Hm8jh27PHbcexn6tHVB9yofkFgbJYdwZ59fluO04x8gPbE7gZ9R8AvsnABLtJZwB2Yk/oy1qfEBQy2weArXFHIKPw576VLcKbuwQTBhpAzWc77vd7laI1urzcfTHfxrzpRtkwxgKzOuSK7DYVFb3SOrFqjPW79mTjuhr/aw1Kz/3UlFbNhN+2NZRa7et6aO4pOLb9IhV9hrDCdYB0E/xkrb6v2bBmokGSDNHTqSr5DGZv0qJFBYzRQIMkc+15cX0ZwPc++XlDQmE2lPnzgWg6qqgPJFAKWKEBv9wMZRzYyxgagKrGCLlskjekaK0eyWXnLCBc8uhObRHPZwITnUe1K4hW+MjAKRMOJe7mBGX4byDjaohhPkE1N5hyqvdi42g7FWILMMS0c9cc4cbThpVYn4gEDZiMQH8e5TrxrerjqVKxk2MROUqw6jFlG4xo1xg6yvjVXqhOjcbjZ1zoXjuS6I6Mj7aMqHthhJoNisS9qPWoTR6KBY27okZjg0NggIrSFO9WdmhqjLhoiSCXR11yIxmdzMyMI7UTgpnSw0BdR5Gbe8KPg+UEKsdo/XAhX0UQs1RUIIZukmG7vCt9yckslEsJUCRYKLdE0kouiQAjZNOUDk5GAYmLfRiABKa/gBiKKLNlMzrEQBpMMzhFmmGKwSPRUHDEFTiZneitMMdE+7eFnuhkdzIpERv99C/Qoy6yCAJvmBPp0AfdohmeyAvdKO5AaQzWTgrMtRgMuYjDRfBxUM8HS6JSpGON9qretsKfkZlzsirWNq2O9qjAxYzenroIl2llMJ/cGXxbrG58xFVgUNSxGEz3IhCufGNC3YfTDU7iEhvNbmoBGjLyIUAoPYI9uAB0R8iJCH5DynspaONafHFWdwo1AsTrFkgaKNbWHI0vNaHn+S/CWaJ5D8UgDFUWG0NsKSAyR/0dTM1YZQqNIMtVt8I6CAYWgZYZwghR/EiUoOe2YwC7DwgBtMvWwtYqkkLaEthmiRSS4bkjPEJfQNkO4iK7yr4Eck4Mm2wzRIirrwkaSH6fFEC2Dss8FXFt6FG2dIcqfMsXfTsHbIQfR1hkit0uxArWJ1BQ5arLPEHinijkkoElder7OPsM6WAk1bTqPBk4aGVL7DJGuUbNpQILVDU2aDMFmUwowwGGMRooAMQw9GVSjpx2AwlAy20iANZIXUYbh/TcZflyRxgDpDBV7AX6msUkBwxJt+goAB8MqiwE0qU56BjAsazwmFsD5UhBE4O9pZYHTYAiyGQohEFh5rpPIT4UhSHnKJWoY+VHg6AyeCkNwTiMPg6MZGh1bkRJDYC/kIgXUk/Q3CKkwBIIoVTXA2SOkPz4gDWuBZErqQoOoSzXo2kc6axjVi9JINhr9BnpVnOkw7NAXJKp/Nc/t02EIVA2XVA5HU1hMryAnHTks0CM9YCz0vk2NMqzUTt5xfKb11AiiMaJM9euYUAgQPVXezpjC8PT70+/rK7XDtDj0I4so23NgX+sNLYmAfT/0Kje3T9cJSUYLRtjf2B8Ac6hnLNRifD+seE+1JBs2GudLkqbnhrxSQhYjLD2/6HOM2m9JHWbUvujWQBHyNH7llJS9+AiwJPH2G7wS4pnTK0iZKL/0pCmPUbGSbLooQ91CPWKuzTv6pTVMNMw/VIZH/s1PnWFAIiM+Bo56snrRoU6+tPSiMw7VvEUdb916WY2McElnFb8Uw6Oihm/+tRj6Pt0wUhlmKYdrePfWGWanS3coUiMssi61xND/gFiG4ffEDMn2UNunqVS20ZK3ZXX6hluv5IXmFpHs05jzS1+uf9XKb/HuB5yUX+7EHEOiJAK/NH7C5mKLWJzc34h2a4X2JHJsYS4+lOCXSCCJ+SpyfIiUr53i9SsBRY/mu5FjfHN5Gil+lbAg3pGeQs/TGMu1yXEH1Y1/S3pItLpJlmsD+VJbn6qV8SKWSA8B+VLJB+zGct4KwAyLlEcAl0aW8wZHHcZun/iM71DXkBhqnFsYO3tSwBMURBJDcJAkO3sydn6ogPvkDKOqVF6CZ+oMuCDX+g+QIUnTaJwBI/WrpWpqxQfZnxwhOfRPCYNoneObqsXwfe85Pgd6BkNIksUHWkOmSmHBn/xHUVxX1pO9jQ2FahXE0PtGGEWrngbVRF0SBt3hLNzswDC8jvmbZ2gsSAWYWjVRqK6NXiH84u2EqiLO1l/fIIJHRUJ6H0VCCgWmJmoTz7y3TXckWMYy3KM0txR8VKBSm6j5sz388N6nXHlGB4Q1z0DwpFlfimqEifbieM/j9G+eX072/+DkviIIgIsn+JEIujXCwF2nbtN7b3/avhc+fCuf7CTs+KT25HuY31EoNaIfoFvnnbxW/wTWeN/4p98fHh6+n4aVUJhSJOX1wZcvarX6ib+3wP7mtjohDGMTpqQl1P/eAn4zQyiiRUuoCIoUouuBVBUG+u6J8KE0zk6ooELxZ5C+UJUm9O2aum8qSE4oIHymEETfrqlqRPT9oXo+6ll3CX2fVK2AdpqyVQOWVD25f32jR9GvkI4s0D1r6p+BJvsO+OSuFH/AhAne0JLdyb4DTvotd+1W5LIIEd5S1KjgW27CLd/RMJj2MffZi0/jWPofsWIIfo9PiGMTX1lQOH65VZfHsEItNEl+6QNQVA6npffPfj4UBQHEJ37FJ9oOLeB7MWjzQ8aG/j331Y/bkoSkHxbv6DUmcHrEdBK8Yoh+0/tZ+fdp0RN52v7aCf+tU/0N76chnq/Ay9q0rmA8u3p5Oip53r7P7YeeV7y916uehRdWUu8YwvdE6V7BeHZ1/ePu1C+WSpVtAUPRu334fX2lWTiL74kiN4SAdzERlc0+zo6Py+Xaz5+1cvk4Uak+vpOOvL/wlXvB/9F9bYLbvrK/zwxfqqqjIgT3JtKzw4aBTLWGFG6AbyZmGbdAx3dfakoPvr/U2pGwEvCd15rfZonuoM1SFLEQat9BWxhgUTy8e4S1+weI7oLOrNMy7nSRZFcJ7ghnGd3nLehzkejiX7wrTHZ4IUBwfzpPZMBQpOkc1r36rmaJ7ysE7y2D3ggCgkl7IwhciAwoirqU8FHSJx9IjxIRQRPtglrCPjMpalSBUjdUoy1qDHYQvYLMdCYT93tKx/SLm68Z6vck7tmlk5uio7kUrqAxFxm74LsxrBvGjrC9q7m+a+KuVpuuSJaFcRXTO8+kNhd2PlsLo82ovylqibZZQpP9D0Ve/W4Z7e3UcUwPS+PdbmK6OTPHjk6t9uP6kI6MDxfTajVgcwsOziiu7bGN1tXN2H7AgWm7UR/E9gNOv+XxWqma3KrNCxbXAtxe2+q4UQO2NNW6vrqK7yFvr/V4M755fMAGJjjKe6tb9KSq8RQdly2T7tVGT8IvYdZCipjezv/WcTJLkMQ5n8f2VN8StO3u/xE6cG8cg7meMa53J0zGLzDsySDMZBTXepU5QyrJemsZxNmHf0+epJHl68gnsl5I5sxHyk75+WqqQG9N8DGdHF89rnH9x5UMpsOxbFM1O7PBWkMp0FuLoE7vMT305Tt1i/VSus5iOOq0gVfXOB9355PNi1B7mJtWC+ktLlWntaO5cVCmg3mv15uNRuv/9ufLyVpprP9d/TFskW7+si6xjIDohtEr3ECd2u7X9vwYIVacOMkkYBP7RiKKNnkZdRHoXpKTGKvYAMAYrOeCYtCY29+qzLUQ7BLQUbON2nD5MOPGp4VCS+or6yPg8+w26Ad0LXEM+CALDQrRVXS7KHD540H0BH3FzDHLkfH5wazfK0YLbmqzBsz9m3FxGUb7wshmZXyarX2IxehROVQQ0XN6B6E+xWi2Fkyai8AIGHcvDkq7iFC97LucuJTrEItPVwenXGLQnj2uWSrR3ERVfPJ3dAAF1lS0L/8uNzSZKBjcRozcmXfHX5DdG+rj2d/BxOWc7YNz7iz73db5Vya3h3q7M2q1Wt1ud7b+33hcz9yhzpEjR44cOXLkyJEjh0H8ByMJ8u+aLBzeAAAAAElFTkSuQmCC
        

  * **Security** : For sensitive files (such as malware), select `Password Protect Zip`. This automatically encrypts the saved ZIP archive created using `Save To Case Wall` with the password `infected`.




#### Playbook block configuration

The following configuration demonstrates how to use the **Execute HTTP Request** action within a playbook block. Use this example to understand how to apply placeholders and input prefixes.

When using block inputs as placeholders, you must include the `Input.` prefix (for example, `[Input.comment]`).

  * **Method** : `PUT`

  * **URL Path** :
        
        https://{API_URL}/[Input.table_name]/[Input.sys_id]
        

  * **Headers** :
        
        {
          "Content-type": "application/json; charset=utf-8",
          "Accept": "application/json",
          "User-Agent": "GoogleSecops"
        }
        

  * **Body Payload** :
        
        {
          "work_notes": "[Input.comment]"
        }
        




#### Action inputs

The **Execute HTTP Request** action requires the following parameters:

Parameter | Description  
---|---  
`Method` | _Optional_ A method to use in the request.The default value is `GET`. Possible values are:

  * `GET`
  * `POST`
  * `PUT`
  * `PATCH`
  * `DELETE`
  * `HEAD`
  * `OPTIONS`

  
`URL Path` | _Optional_ A URL to execute.The default value is `https://`.  
`URL Params` | _Optional_ The URL parameters.The action uses any value provided alongside the values that you directly provided in the **URL Path** parameter. This parameter requires the JSON object format as an input. The default value is as follows:
    
    
    {
        "URL Field Name": "URL_FIELD_VALUE"
        }  
  
`Headers` | _Optional_ Headers to use in the HTTP request. This parameter requires the JSON object format as an input. The default value is as follows:
    
    
    {
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "application/json",
        "User-Agent" : "GoogleSecOps"
        }  
  
`Cookie` | _Optional_ The parameters to use in the `Cookie` header. This parameter overwrites cookies provided in the **Headers** parameter. This parameter requires the JSON object format as an input. The default value is as follows:
    
    
    {
        "Cookie_1": "COOKIE_1_VALUE"
        }  
  
##### `Body Payload`

| _Optional_ A body for the HTTP request. The action constructs different payloads depending on the `Content-Type` header value provided in the `Headers` parameter. This parameter requires the JSON object format as an input except when a third-party product requires XML or the `multipart/form-data` content. If you submit or upload a file using the API request, provide the base64-encoded version of the file in the **Body Payload** parameter and set the header to `"Content-type": "multipart/form-data"`. The default value is as follows:
    
    
    {
        "Body Field Name": "BODY_FIELD_VALUE"
        }  
  
`Expected Response Values` | Optional. The JSON object containing the field-value pairs that define the required state of the response body. **Note:** Providing a value for this parameter triggers asynchronous polling behavior. For detailed information on formatting conditions and logical operators, see Action behavior.   
`Save To Case Wall` | _Optional_ If selected, the action saves the file and attaches the saved file to the case wall. The file is archived with the `.zip` extension. The `.zip` file isn't password-protected.Not selected by default.  
`Password Protect Zip` | _Optional_ If selected, the action adds a password to the `.zip` file created using the `Save To Case Wall` parameter. The password is as follows: `infected`. Use this parameter when working with suspicious files.Selected by default.  
`Follow Redirects` | _Optional_ If selected, the action follows the redirects.Selected by default.  
`Fail on 4xx/5xx` | _Optional_ If selected, the action fails if the status code of the response is 4xx or 5xx errors.Selected by default.  
`Base64 Output` | _Optional_ If selected, the action converts the response to the base64 format.Use this parameter when downloading files.The JSON result cannot exceed 15 MB.Not selected by default.  
`Fields To Return` | _Required_ The fields to return. The possible values are as follows:

  * `response_data`
  * `redirects`
  * `response_code`
  * `response_cookies`
  * `response_headers`
  * `apparent_encoding`

  
`Request Timeout` | _Required_ A period to wait for the server to send data before the action fails.The default value is 120 seconds.  
  
#### Action outputs

The **Execute HTTP Request** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Execute HTTP Request** action:
    
    
    {
       "response_data": {
           "data": {
               "relationships": {
                   "comment": [
                       {
                           "name": "item",
                           "description": "Object to which the comment belongs to."
                       },
                       {
                           "name": "author",
                           "description": "User who wrote the comment."
                       }
                   ]
               }
           }
       },
       "redirects": [],
       "response_code": 200,
       "cookies": {},
       "response_headers": {
           "Content-Type": "application/json",
           "X-Cloud-Trace-Context": "VALUE",
           "Date": "Fri, 03 Nov 2023 16:14:13 GMT",
           "Server": "Google Frontend",
           "Content-Length": "36084"
       },
       "apparent_encoding": "ascii"
    }
    

##### Output messages

The **Execute HTTP Request** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully executed API request.` `Successfully executed API request, but the status code {4xx/5xx} was returned. Please check the request or try again later.` | The action succeeded.  
`Failed to execute API request. Error: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Execute HTTP Request** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test connectivity to Google Cloud.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Ping** action:
    
    
    {
    "endpoint": "TEST_URL"
    }
    

##### Output messages

The **Ping** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully tested connectivity.` | The action succeeded.  
`Failed to test connectivity.` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/iap/docs/saml-attribute-propagation/
title: Configure SAML attribute propagation \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:22.595850+00:00
---

# Configure SAML attribute propagation  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/saml-attribute-propagation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Configure SAML attribute propagation Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable and use Security Assertion Markup Language (SAML) attribute propagation. You can use this feature to propagate SAML attributes from an identity provider to applications protected by Identity-Aware Proxy (IAP). When you propagate SAML attributes, you can specify which attributes to propagate, and how to deliver the attributes.

## Before you begin

You should be knowledgeable about the [SAML V2.0 Assertions and Protocols specification (PDF)](https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf).

### Understanding how the data is handled

Before you enable SAML attribute propagation, ensure that you understand how Google Cloud manages the data, and what type of information you should and shouldn't pass over this channel.

You can configure IAP to include one or more attributes in the information it provides to your protected applications. If you set up [SSO via a third party Identity provider](https://support.google.com/a/topic/7579248?&ref_topic=7556686) and your identity provider includes an `<AttributeStatement>` in the SAML assertion, Google Cloud temporarily stores the attributes associated with a user's Google account session. When a Google account session expires, an asynchronous process permanently removes the information within a week. You can configure the expiration date.

Don't use SAML attribute propagation for sensitive personally identifiable information (PII), such as account credentials, government ID numbers, card holder data, financial account data, healthcare information, or sensitive background information.

## Enabling SAML attribute propagation

Enable SAML attribute propagation by [creating an SSO profile](https://support.google.com/a/answer/12032922#create_profile) in Google Workspace, and then update the IAP settings by using the Google Cloud CLI or the REST API.

**Note:** When you enable this feature for specific users or user groups, your existing SAML configuration is overridden.

### Console

  1. In the Google Cloud console, go to the IAP page.  
[ Go to IAP ](https://console.cloud.google.com/security/iap)
  2. Open the settings for a resource, and then scroll to **Attribute propagation**.
  3. Select **Enable attribute propagation** , and then click **Save**.
  4. In the **SAML Attributes** tab, enter the attributes that you want to propagate using the following format: `attribute1, attribute2, attribute3`

You can also enter the attributes by using a custom expression.The attributes for your custom expression are displayed in the **SAML Attributes** tab. You must use the following expression format for your attributes to be displayed in the **SAML Attributes** tab:  
`attributes.saml_attributes.filter(attribute, attribute.name in ['attribute', 'attribute2', 'attribute1'])`

  5. For **Credential types to pass** , select at least one attribute format coming from the IdP to pass to applications.




### gcloud

Run the following [IAP gcloud CLI commands](https://docs.cloud.google.com/sdk/gcloud/reference/iap/settings) to update the SAML attribute propagation settings:
    
    
    gcloud iap settings set SETTING_FILE [--folder=FOLDER --organization=ORGANIZATION --project=PROJECT> --resource-type=RESOURCE_TYPE --service=SERVICE --version=VERSION] [GCLOUD_WIDE_FLAG …]
    

Replace the following:

  * FOLDER: The folder in which your application resides.
  * ORGANIZATION: The organization in which your application resides.
  * PROJECT: The project in which your application resides.
  * RESOURCE_TYPE: The resource type.
  * SERVICE: The service.
  * VERSION: The version number.



YAML: 
    
    
    applicationSettings:
     attributePropagationSettings:
      expression: CEL_EXPRESSION
      outputCredentials: ARRAY[OUTPUT_CREDENTIALS]
      enable: BOOLEAN
    

JSON: 
    
    
    {
       "application_settings":{
          "attribute_propagation_settings": {
            "expression": CEL_EXPRESSION,
            "output_credentials": ARRAY[OUTPUT_CREDENTIALS]
            "enable": BOOLEAN
          }
       }
    }
    

### REST API

You can configure the SAML attributes to propagate by using the [`ApplicationSettings`](https://docs.cloud.google.com/iap/docs/reference/rest/v1/IapSettings#ApplicationSettings) object in [IapSettings](https://docs.cloud.google.com/iap/docs/reference/rest/v1/IapSettings), as shown in the following examples:
    
    
    {
     "csmSettings": {
        object (CsmSettings)
      },
      "accessDeniedPageSettings": {
        object (AccessDeniedPageSettings)
      },
     "attributePropagationSettings": {
        object (AttributePropagationSettings)
      },
      "cookieDomain": string,
    }
    

**`AttributePropagationSettings`**
    
    
    {
     "expression": string,
     "output_credentials": array
     "enable": boolean
    }
    

## Setting the output credentials

When using SAML attribute propagation, you can send attributes across multiple mediums, including JSON Web Token (JWT) and headers, by setting output credentials. To set the credentials in the API, you can specify a list of comma-separated strings, as shown in the following example:
    
    
    "output_credentials": ["HEADER", "JWT", "RCTOKEN"]
    

## Filtering SAML attributes using Common Expression Language

You can use [Common Expression Language (CEL)](https://github.com/google/cel-spec) functions to filter SAML attributes.

Using CEL expressions with SAML attribute propagation has the following limitations:

  * An expression must return a list of attributes.
  * An expression can select a maximum of 45 attributes.
  * An expression string cannot exceed 1000 characters.



Following are the CEL functions that are supported when using the IAP SAML attribute propagation feature.

Note that the functions are case sensitive and must be used exactly as written. The ordering of the `strict` and `emitAs` functions does not matter when chaining function calls.

Function | Example | Description  
---|---|---  
Field Selection | `a.b` | Select field `b` from the proto `a`. The character `b` can be another proto, a list, or a simple value type such as string.  
Filtering Lists | `list.Filter(iter_var, condition)` | Returns a subset of `list` where items meet `condition`.  
List Membership | `a` in `b` | Returns `true` if the value `a` is a member of list `b`.  
selectByName | `list.selectByName("name")` | From the list, select the attribute where `name = "name"`.  
append | `list.append(attribute)` | Appends the given attribute to the given list.  
strict | `attribute.strict()` | Emits the attribute without the `x-goog-iap-attr-` prefix when using `HEADERS` as an output credential.  
emitAs | `attribute.emitAs("new_name")` | Outputs the given attribute with the name `"new_name"` to all of the selected output credentials.  
  
### Example CEL expression

Assume a SAML assertion: 
    
    
    <saml2:AttributeStatement xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <saml2:Attribute Name="my_saml_attr_1">
        <saml2:AttributeValue xsi:type="xsd:string">value_1</saml2:AttributeValue>
        <saml2:AttributeValue xsi:type="xsd:string">value_2</saml2:AttributeValue>
      </saml2:Attribute>
     <saml2:Attribute Name="my_saml_attr_2">
        <saml2:AttributeValue xsi:type="xsd:string">value_3</saml2:AttributeValue>
        <saml2:AttributeValue xsi:type="xsd:string">value_4</saml2:AttributeValue>
      </saml2:Attribute>
     <saml2:Attribute Name="my_saml_attr_3">
        <saml2:AttributeValue xsi:type="xsd:string">value_5</saml2:AttributeValue>
        <saml2:AttributeValue xsi:type="xsd:string">value_6</saml2:AttributeValue>
      </saml2:Attribute>
    </saml2:AttributeStatement>
    

To select `my_saml_attr_1`, use the following CEL expression:
    
    
    attributes.saml_attributes.filter(attribute, attribute.name in ["my_saml_attr_1"])
    

To select `my_saml_attr_1` and `my_saml_attr_2`, use the following CEL expression:
    
    
    attributes.saml_attributes.filter(attribute, attribute.name in ["my_saml_attr_1", "my_saml_attr_2"])
    

## Attribute format

All selected attributes are fully duplicated in all selected output credentials.

Example: Assume a SAML assertion 
    
    
    <saml2:AttributeStatement xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <saml2:Attribute Name="my_saml_attr_1">
        <saml2:AttributeValue xsi:type="xsd:string">value_1</saml2:AttributeValue>
        <saml2:AttributeValue xsi:type="xsd:string">value_2</saml2:AttributeValue>
      </saml2:Attribute>
    </saml2:AttributeStatement>
    

### JWT and RC token

The JWT token provides the attributes through the `additional_claims` field. The field is an object and contains a mapping of the attribute names to a list of the attribute values. The attribute names are unchanged from the provided SAML assertions.

For the example SAML assertion, the IAP JWT contains the following:
    
    
    {
      "additional_claims": {
        "my_saml_attr_1": ["value_1", "value_2"]
      }
    }
    

### Headers in a SAML assertion

In headers, the values of the attributes, keys, and names are URL escaped according to [RFC 3986](https://www.ietf.org/rfc/rfc3986.txt) and joined by commas. For example, `header&name: header$value` becomes `x-goog-iap-attr-header%26name: header%24value`.

To uniquely identify IAP headers, each header contains the IAP prefix `x-goog-iap-attr-`. For security reasons, the load balancer removes any request headers with the prefix `x-goog-iap-attr`. This ensures that headers received by the app are generated by IAP.

For the example SAML assertion, the header looks like the following:
    
    
    "x-goog-iap-attr-my_saml_attr_1": "value_1,value_2"
    

The following example demonstrates how IAP escapes special characters when propagating attributes in headers, such as `value&1`, `value$2`, and `value,3`:
    
    
    "x-goog-iap-attr-my_saml_attr_1": "value%261,value%242,value%2C3"
    

Following is an example of how a header name is escaped.

Header name:
    
    
    "iap,test,3": "iap_test3_value1,iap_test3_value2"
    

Escaped header name:
    
    
    "X-Goog-IAP-Attr-iap%2Ctest%2C3": "iap_test3_value1,iap_test3_value2"
    

## Customize attributes

You can use the `selectByName`, `append`, `strict`, and `emitas` functions to modify the propagated attributes names, specify whether or not to use the header prefix for some attributes, and select new IAP-provided attributes.

If you don't require SAML attribute propagation, but need the email address, device ID, or timestamp in an SM_USER field, you can select those attributes from the `iap_attributes list`: `attributes.iap_attributes`…

IAP provides the following attributes: `user_email`, `device_id`, and `timestamp`.

### Examples

The following examples show how to customize attributes by using the `selectByName`, `append`, `strict`, and `emitas` functions.

Assume the example SAML assertion.

**`selectByName`**

Use the `selectByName` function to select a single attribute from a given list by name. For example, to select `my_saml_attr_1`, use the following expression:
    
    
    attributes.saml_attributes.selectByName("my_saml_attr_1")
    

**`append`**

Use the `append` function to append an attribute onto a list of attributes. You must select this attribute from one of the supported IAP attribute lists. For example, to append `my_saml_attr_2` to a list containing `my_saml_attr_1`, use the following expression:
    
    
    attributes.saml_attributes.filter(x, x.name in ["my_saml_attr_1"]).append(attributes.saml_attributes.selectByName("my_saml_attr_2"))
    

You can add `"my_saml_attr_2"` to the filter list. You can also add multiple attributes and append them to a list by chaining the appends, like the following:
    
    
    attributes.saml_attributes.filter(x, x.name in ["my_saml_attr_1"]).append(
    attributes.saml_attributes.selectByName("my_saml_attr_2")).append(
    attributes.saml_attributes.selectByName("my_saml_attr_3"))
    

Appending single attributes is most useful when combined with the `strict` and `emitAs` functionality.

**`strict`**

Use the `strict` function to flag an attribute so that IAP does not prefix the name with `x-goog-iap-attr-`. This is useful when an attribute name must be exact for the backend application. Example:
    
    
    attributes.saml_attributes.selectByName("my_saml_attr_1").strict()
    

**`emitAs`**

Use the `emitAs` function to specify a new name for the attribute. The name you specify will be output to all credentials. For example, to rename `my_saml_attr_1` to `custom_name`, use the following expression:
    
    
    attributes.saml_attributes.selectByName("my_saml_attr_1").emitAs("custom_name")
    

You can use the various functions to customize attributes for specific use cases. For example, you can use the following expression to propagate a user's email from IAP attributes as `"SM_USER"` along with other SAML attributes:
    
    
    attributes.saml_attributes.filter(x, x.name in ["my_saml_attr_1"]).append(
    attributes.iap_attributes.selectByName("user_email").emitAs("SM_USER").strict())
    

The output headers look like the following:
    
    
    "x-goog-iap-attr-my_saml_attr_1": "value_1,value_2"
    "SM_USER": "email@domain.com"
    

## Constraints when using SAML attribute propagation

At sign-in, incoming attributes from the identity provider have a limit of 2KB of SAML attribute data. Assertions that exceed the 2KB maximum are declined and sign-in fails.

Most web servers have an 8KB request size limit. This limits the size of outgoing custom attributes, including duplicating attributes in headers. If the size of the attributes (name plus values) exceeds 5000 bytes when duplicated and encoded, IAP rejects the request and returns the IAP error code 401.

## Unicode characters in SAML attribute propagation

This feature does not support Unicode and UTF-8 characters, so attribute values must be low-ASCII strings. If an assertion is not low-ASCII, sign-in fails.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/summary_class/
title: Package Classes (0.10.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:03:26.299566+00:00
---

# Package Classes (0.10.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.10.0  0.9.0  0.8.0  0.7.0  0.6.16  0.5.3  0.4.0  0.3.2  0.2.0  0.1.1 

Summary of entries of Classes for bigquerydatapolicy.

## Classes 

### [DataPolicyServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient)

Data Policy Service provides APIs for managing the label-policy bindings.

### [DataPolicyServiceClient](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient)

Data Policy Service provides APIs for managing the label-policy bindings.

### [ListDataPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.pagers.ListDataPoliciesAsyncPager)

A pager for iterating through `list_data_policies` requests.

This class thinly wraps an initial [ListDataPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.types.ListDataPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `data_policies` field.

If there are more pages, the `__aiter__` method will make additional `ListDataPolicies` requests and continue to iterate through the `data_policies` field on the corresponding responses.

All the usual [ListDataPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.types.ListDataPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDataPoliciesPager](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.pagers.ListDataPoliciesPager)

A pager for iterating through `list_data_policies` requests.

This class thinly wraps an initial [ListDataPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.types.ListDataPoliciesResponse) object, and provides an `__iter__` method to iterate through its `data_policies` field.

If there are more pages, the `__iter__` method will make additional `ListDataPolicies` requests and continue to iterate through the `data_policies` field on the corresponding responses.

All the usual [ListDataPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.types.ListDataPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [CreateDataPolicyRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.types.CreateDataPolicyRequest)

Request message for the CreateDataPolicy method.

### [DataMaskingPolicy](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.types.DataMaskingPolicy)

The data masking policy that is used to specify data masking rule.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PredefinedExpression](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.types.DataMaskingPolicy.PredefinedExpression)

The available masking rules. Learn more here: <https://cloud.google.com/bigquery/docs/column-data-masking-intro#masking_options>.
    
    
        - STRING: ""
        - BYTES: b''
        - INTEGER: 0
        - FLOAT: 0.0
        - NUMERIC: 0
        - BOOLEAN: FALSE
        - TIMESTAMP: 1970-01-01 00:00:00 UTC
        - DATE: 1970-01-01
        - TIME: 00:00:00
        - DATETIME: 1970-01-01T00:00:00
        - GEOGRAPHY: POINT(0 0)
        - BIGNUMERIC: 0
        - ARRAY: []
        - STRUCT: NOT_APPLICABLE
        - JSON: NULL
    LAST_FOUR_CHARACTERS (9):
        Masking expression shows the last four characters of text.
        The masking behavior is as follows:
    
        - If text length > 4 characters: Replace text with XXXXX,
          append last four characters of original text.
        - If text length <= 4 characters: Apply SHA-256 hash.
    FIRST_FOUR_CHARACTERS (10):
        Masking expression shows the first four characters of text.
        The masking behavior is as follows:
    
        - If text length > 4 characters: Replace text with XXXXX,
          prepend first four characters of original text.
        - If text length <= 4 characters: Apply SHA-256 hash.
    EMAIL_MASK (12):
        Masking expression for email addresses. The masking behavior
        is as follows:
    
        - Syntax-valid email address: Replace username with XXXXX.
          For example, cloudysanfrancisco@gmail.com becomes
          XXXXX@gmail.com.
        - Syntax-invalid email address: Apply SHA-256 hash.
    
        For more information, see `Email
        mask <https://cloud.google.com/bigquery/docs/column-data-masking-intro#masking_options>`__.
    DATE_YEAR_MASK (13):
        Masking expression to only show the year of `Date`,
        `DateTime` and `TimeStamp`. For example, with the year
        2076:
    
        - DATE : 2076-01-01
        - DATETIME : 2076-01-01T00:00:00
        - TIMESTAMP : 2076-01-01 00:00:00 UTC
    
        Truncation occurs according to the UTC time zone. To change
        this, adjust the default time zone using the `time_zone`
        system variable. For more information, see the System
        variables reference.
    

### [DataPolicy](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.types.DataPolicy)

Represents the label-policy binding.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DataPolicyType](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.types.DataPolicy.DataPolicyType)

A list of supported data policy types.

### [DeleteDataPolicyRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.types.DeleteDataPolicyRequest)

Request message for the DeleteDataPolicy method.

### [GetDataPolicyRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.types.GetDataPolicyRequest)

Request message for the GetDataPolicy method.

### [ListDataPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.types.ListDataPoliciesRequest)

Request message for the ListDataPolicies method.

### [ListDataPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.types.ListDataPoliciesResponse)

Response message for the ListDataPolicies method.

### [RenameDataPolicyRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.types.RenameDataPolicyRequest)

Request message for the RenameDataPolicy method.

### [UpdateDataPolicyRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.types.UpdateDataPolicyRequest)

Response message for the UpdateDataPolicy method.

### [DataPolicyServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient)

Data Policy Service provides APIs for managing the label-policy bindings.

### [DataPolicyServiceClient](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient)

Data Policy Service provides APIs for managing the label-policy bindings.

### [ListDataPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.pagers.ListDataPoliciesAsyncPager)

A pager for iterating through `list_data_policies` requests.

This class thinly wraps an initial [ListDataPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.types.ListDataPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `data_policies` field.

If there are more pages, the `__aiter__` method will make additional `ListDataPolicies` requests and continue to iterate through the `data_policies` field on the corresponding responses.

All the usual [ListDataPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.types.ListDataPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDataPoliciesPager](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.pagers.ListDataPoliciesPager)

A pager for iterating through `list_data_policies` requests.

This class thinly wraps an initial [ListDataPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.types.ListDataPoliciesResponse) object, and provides an `__iter__` method to iterate through its `data_policies` field.

If there are more pages, the `__iter__` method will make additional `ListDataPolicies` requests and continue to iterate through the `data_policies` field on the corresponding responses.

All the usual [ListDataPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.types.ListDataPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [CreateDataPolicyRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.types.CreateDataPolicyRequest)

Request message for the CreateDataPolicy method.

### [DataMaskingPolicy](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.types.DataMaskingPolicy)

The data masking policy that is used to specify data masking rule.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PredefinedExpression](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.types.DataMaskingPolicy.PredefinedExpression)

The available masking rules. Learn more here: <https://cloud.google.com/bigquery/docs/column-data-masking-intro#masking_options>.
    
    
        - STRING: ""
        - BYTES: b''
        - INTEGER: 0
        - FLOAT: 0.0
        - NUMERIC: 0
        - BOOLEAN: FALSE
        - TIMESTAMP: 0001-01-01 00:00:00 UTC
        - DATE: 0001-01-01
        - TIME: 00:00:00
        - DATETIME: 0001-01-01T00:00:00
        - GEOGRAPHY: POINT(0 0)
        - BIGNUMERIC: 0
        - ARRAY: []
        - STRUCT: NOT_APPLICABLE
        - JSON: NULL
    

### [DataPolicy](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.types.DataPolicy)

Represents the label-policy binding.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DataPolicyType](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.types.DataPolicy.DataPolicyType)

A list of supported data policy types.

### [DeleteDataPolicyRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.types.DeleteDataPolicyRequest)

Request message for the DeleteDataPolicy method.

### [GetDataPolicyRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.types.GetDataPolicyRequest)

Request message for the GetDataPolicy method.

### [ListDataPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.types.ListDataPoliciesRequest)

Request message for the ListDataPolicies method.

### [ListDataPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.types.ListDataPoliciesResponse)

Response message for the ListDataPolicies method.

### [UpdateDataPolicyRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.types.UpdateDataPolicyRequest)

Response message for the UpdateDataPolicy method.

### [DataPolicyServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient)

Data Policy Service provides APIs for managing the BigQuery Data Policy.

### [DataPolicyServiceClient](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient)

Data Policy Service provides APIs for managing the BigQuery Data Policy.

### [ListDataPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.pagers.ListDataPoliciesAsyncPager)

A pager for iterating through `list_data_policies` requests.

This class thinly wraps an initial [ListDataPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.types.ListDataPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `data_policies` field.

If there are more pages, the `__aiter__` method will make additional `ListDataPolicies` requests and continue to iterate through the `data_policies` field on the corresponding responses.

All the usual [ListDataPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.types.ListDataPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDataPoliciesPager](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.pagers.ListDataPoliciesPager)

A pager for iterating through `list_data_policies` requests.

This class thinly wraps an initial [ListDataPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.types.ListDataPoliciesResponse) object, and provides an `__iter__` method to iterate through its `data_policies` field.

If there are more pages, the `__iter__` method will make additional `ListDataPolicies` requests and continue to iterate through the `data_policies` field on the corresponding responses.

All the usual [ListDataPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.types.ListDataPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AddGranteesRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.types.AddGranteesRequest)

Request message for the AddGrantees method.

### [CreateDataPolicyRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.types.CreateDataPolicyRequest)

Request message for the CreateDataPolicy method.

### [DataMaskingPolicy](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.types.DataMaskingPolicy)

The policy used to specify data masking rule.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PredefinedExpression](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.types.DataMaskingPolicy.PredefinedExpression)

The available masking rules. Learn more here: <https://cloud.google.com/bigquery/docs/column-data-masking-intro#masking_options>.
    
    
        - STRING: ""
        - BYTES: b''
        - INTEGER: 0
        - FLOAT: 0.0
        - NUMERIC: 0
        - BOOLEAN: FALSE
        - TIMESTAMP: 1970-01-01 00:00:00 UTC
        - DATE: 1970-01-01
        - TIME: 00:00:00
        - DATETIME: 1970-01-01T00:00:00
        - GEOGRAPHY: POINT(0 0)
        - BIGNUMERIC: 0
        - ARRAY: []
        - STRUCT: NOT_APPLICABLE
        - JSON: NULL
    LAST_FOUR_CHARACTERS (4):
        Masking expression shows the last four characters of text.
        The masking behavior is as follows:
    
        - If text length > 4 characters: Replace text with XXXXX,
          append last four characters of original text.
        - If text length <= 4 characters: Apply SHA-256 hash.
    FIRST_FOUR_CHARACTERS (5):
        Masking expression shows the first four characters of text.
        The masking behavior is as follows:
    
        - If text length > 4 characters: Replace text with XXXXX,
          prepend first four characters of original text.
        - If text length <= 4 characters: Apply SHA-256 hash.
    EMAIL_MASK (6):
        Masking expression for email addresses. The masking behavior
        is as follows:
    
        - Syntax-valid email address: Replace username with XXXXX.
          For example, cloudysanfrancisco@gmail.com becomes
          XXXXX@gmail.com.
        - Syntax-invalid email address: Apply SHA-256 hash.
    
        For more information, see `Email
        mask <https://cloud.google.com/bigquery/docs/column-data-masking-intro#masking_options>`__.
    DATE_YEAR_MASK (7):
        Masking expression to only show the year of `Date`,
        `DateTime` and `TimeStamp`. For example, with the year
        2076:
    
        - DATE : 2076-01-01
        - DATETIME : 2076-01-01T00:00:00
        - TIMESTAMP : 2076-01-01 00:00:00 UTC
    
        Truncation occurs according to the UTC time zone. To change
        this, adjust the default time zone using the `time_zone`
        system variable. For more information, see `System variables
        reference <https://cloud.google.com/bigquery/docs/reference/system-variables>`__.
    RANDOM_HASH (8):
        Masking expression that uses hashing to mask
        column data. It differs from SHA256 in that a
        unique random value is generated for each query
        and is added to the hash input, resulting in the
        hash / masked result to be different for each
        query. Hence the name "random hash".
    

### [DataPolicy](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.types.DataPolicy)

Represents the label-policy binding.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DataPolicyType](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.types.DataPolicy.DataPolicyType)

A list of supported data policy types.

### [Version](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.types.DataPolicy.Version)

The supported versions for the Data Policy resource.

### [DeleteDataPolicyRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.types.DeleteDataPolicyRequest)

Request message for the DeleteDataPolicy method.

### [GetDataPolicyRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.types.GetDataPolicyRequest)

Request message for the GetDataPolicy method.

### [ListDataPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.types.ListDataPoliciesRequest)

Request message for the ListDataPolicies method.

### [ListDataPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.types.ListDataPoliciesResponse)

Response message for the ListDataPolicies method.

### [RemoveGranteesRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.types.RemoveGranteesRequest)

Request message for the RemoveGrantees method.

### [UpdateDataPolicyRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.types.UpdateDataPolicyRequest)

Request message for the UpdateDataPolicy method.

### [DataPolicyServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient)

Data Policy Service provides APIs for managing the BigQuery Data Policy.

### [DataPolicyServiceClient](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient)

Data Policy Service provides APIs for managing the BigQuery Data Policy.

### [ListDataPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.pagers.ListDataPoliciesAsyncPager)

A pager for iterating through `list_data_policies` requests.

This class thinly wraps an initial [ListDataPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.types.ListDataPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `data_policies` field.

If there are more pages, the `__aiter__` method will make additional `ListDataPolicies` requests and continue to iterate through the `data_policies` field on the corresponding responses.

All the usual [ListDataPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.types.ListDataPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDataPoliciesPager](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.pagers.ListDataPoliciesPager)

A pager for iterating through `list_data_policies` requests.

This class thinly wraps an initial [ListDataPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.types.ListDataPoliciesResponse) object, and provides an `__iter__` method to iterate through its `data_policies` field.

If there are more pages, the `__iter__` method will make additional `ListDataPolicies` requests and continue to iterate through the `data_policies` field on the corresponding responses.

All the usual [ListDataPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.types.ListDataPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AddGranteesRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.types.AddGranteesRequest)

Request message for the AddGrantees method.

### [CreateDataPolicyRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.types.CreateDataPolicyRequest)

Request message for the CreateDataPolicy method.

### [DataMaskingPolicy](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.types.DataMaskingPolicy)

The policy used to specify data masking rule.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PredefinedExpression](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.types.DataMaskingPolicy.PredefinedExpression)

The available masking rules. Learn more here: <https://cloud.google.com/bigquery/docs/column-data-masking-intro#masking_options>.
    
    
        - STRING: ""
        - BYTES: b''
        - INTEGER: 0
        - FLOAT: 0.0
        - NUMERIC: 0
        - BOOLEAN: FALSE
        - TIMESTAMP: 1970-01-01 00:00:00 UTC
        - DATE: 1970-01-01
        - TIME: 00:00:00
        - DATETIME: 1970-01-01T00:00:00
        - GEOGRAPHY: POINT(0 0)
        - BIGNUMERIC: 0
        - ARRAY: []
        - STRUCT: NOT_APPLICABLE
        - JSON: NULL
    

### [DataPolicy](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.types.DataPolicy)

Represents the label-policy binding.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DataPolicyType](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.types.DataPolicy.DataPolicyType)

A list of supported data policy types.

### [Version](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.types.DataPolicy.Version)

The supported versions for the Data Policy resource.

### [DeleteDataPolicyRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.types.DeleteDataPolicyRequest)

Request message for the DeleteDataPolicy method.

### [GetDataPolicyRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.types.GetDataPolicyRequest)

Request message for the GetDataPolicy method.

### [ListDataPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.types.ListDataPoliciesRequest)

Request message for the ListDataPolicies method.

### [ListDataPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.types.ListDataPoliciesResponse)

Response message for the ListDataPolicies method.

### [RemoveGranteesRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.types.RemoveGranteesRequest)

Request message for the RemoveGrantees method.

### [UpdateDataPolicyRequest](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.types.UpdateDataPolicyRequest)

Request message for the UpdateDataPolicy method.

## Modules 

### [pagers](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.pagers)

API documentation for `bigquery_datapolicies_v1.services.data_policy_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.pagers)

API documentation for `bigquery_datapolicies_v1beta1.services.data_policy_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.pagers)

API documentation for `bigquery_datapolicies_v2.services.data_policy_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.pagers)

API documentation for `bigquery_datapolicies_v2beta1.services.data_policy_service.pagers` module.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 

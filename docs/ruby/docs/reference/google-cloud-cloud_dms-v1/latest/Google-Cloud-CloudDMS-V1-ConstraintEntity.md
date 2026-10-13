---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConstraintEntity/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::ConstraintEntity (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:22.438462+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::ConstraintEntity (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConstraintEntity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::ConstraintEntity (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::ConstraintEntity.

Constraint is not used as an independent entity, it is retrieved as part of another entity such as Table or View.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #custom_features
    
    
    def custom_features() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Struct)) — Custom engine specific features. 



### #custom_features=
    
    
    def custom_features=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Struct)) — Custom engine specific features. 



**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Struct)) — Custom engine specific features. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — The name of the table constraint. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the table constraint. 



**Returns**

  * (::String) — The name of the table constraint. 



### #reference_columns
    
    
    def reference_columns() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Reference columns which may be associated with the constraint. For example, if the constraint is a FOREIGN_KEY, this represents the list of full names of referenced columns by the foreign key. 



### #reference_columns=
    
    
    def reference_columns=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Reference columns which may be associated with the constraint. For example, if the constraint is a FOREIGN_KEY, this represents the list of full names of referenced columns by the foreign key. 



**Returns**

  * (::Array<::String>) — Reference columns which may be associated with the constraint. For example, if the constraint is a FOREIGN_KEY, this represents the list of full names of referenced columns by the foreign key. 



### #reference_table
    
    
    def reference_table() -> ::String

**Returns**

  * (::String) — Reference table which may be associated with the constraint. For example, if the constraint is a FOREIGN_KEY, this represents the list of full name of the referenced table by the foreign key. 



### #reference_table=
    
    
    def reference_table=(value) -> ::String

**Parameter**

  * **value** (::String) — Reference table which may be associated with the constraint. For example, if the constraint is a FOREIGN_KEY, this represents the list of full name of the referenced table by the foreign key. 



**Returns**

  * (::String) — Reference table which may be associated with the constraint. For example, if the constraint is a FOREIGN_KEY, this represents the list of full name of the referenced table by the foreign key. 



### #table_columns
    
    
    def table_columns() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Table columns used as part of the Constraint, for example primary key constraint should list the columns which constitutes the key. 



### #table_columns=
    
    
    def table_columns=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Table columns used as part of the Constraint, for example primary key constraint should list the columns which constitutes the key. 



**Returns**

  * (::Array<::String>) — Table columns used as part of the Constraint, for example primary key constraint should list the columns which constitutes the key. 



### #table_name
    
    
    def table_name() -> ::String

**Returns**

  * (::String) — Table which is associated with the constraint. In case the constraint is defined on a table, this field is left empty as this information is stored in parent_name. However, if constraint is defined on a view, this field stores the table name on which the view is defined. 



### #table_name=
    
    
    def table_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Table which is associated with the constraint. In case the constraint is defined on a table, this field is left empty as this information is stored in parent_name. However, if constraint is defined on a view, this field stores the table name on which the view is defined. 



**Returns**

  * (::String) — Table which is associated with the constraint. In case the constraint is defined on a table, this field is left empty as this information is stored in parent_name. However, if constraint is defined on a view, this field stores the table name on which the view is defined. 



### #type
    
    
    def type() -> ::String

**Returns**

  * (::String) — Type of constraint, for example unique, primary key, foreign key (currently only primary key is supported). 



### #type=
    
    
    def type=(value) -> ::String

**Parameter**

  * **value** (::String) — Type of constraint, for example unique, primary key, foreign key (currently only primary key is supported). 



**Returns**

  * (::String) — Type of constraint, for example unique, primary key, foreign key (currently only primary key is supported). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 

---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.JobCategory
title: Enum JobCategory (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:33.310709+00:00
---

# Enum JobCategory (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.JobCategory

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum JobCategory (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.6  2.2.9 
    
    
    public enum JobCategory extends Enum<JobCategory> implements ProtocolMessageEnum

An enum that represents the categorization or primary focus of specific role. This value is different than the "industry" associated with a role, which is related to the categorization of the company listing the job.

Protobuf enum `google.cloud.talent.v4beta1.JobCategory`

## Implements

[ProtocolMessageEnum](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolMessageEnum.html)

## Inherited Members

[Enum.<T>valueOf(Class<T>,String)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#valueOf-java.lang.Class-java.lang.String-)

[Enum.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#clone--)

[Enum.compareTo(E)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#compareTo-E-)

[Enum.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#equals-java.lang.Object-)

[Enum.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#finalize--)

[Enum.getDeclaringClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#getDeclaringClass--)

[Enum.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#hashCode--)

[Enum.name()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#name--)

[Enum.ordinal()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#ordinal--)

[Enum.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#toString--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields   
  
---  
**Name** | **Description**  
`ACCOUNTING_AND_FINANCE` |  An accounting and finance job, such as an Accountant. `ACCOUNTING_AND_FINANCE = 1;`  
`ACCOUNTING_AND_FINANCE_VALUE` |  An accounting and finance job, such as an Accountant. `ACCOUNTING_AND_FINANCE = 1;`  
`ADMINISTRATIVE_AND_OFFICE` |  An administrative and office job, such as an Administrative Assistant. `ADMINISTRATIVE_AND_OFFICE = 2;`  
`ADMINISTRATIVE_AND_OFFICE_VALUE` |  An administrative and office job, such as an Administrative Assistant. `ADMINISTRATIVE_AND_OFFICE = 2;`  
`ADVERTISING_AND_MARKETING` |  An advertising and marketing job, such as Marketing Manager. `ADVERTISING_AND_MARKETING = 3;`  
`ADVERTISING_AND_MARKETING_VALUE` |  An advertising and marketing job, such as Marketing Manager. `ADVERTISING_AND_MARKETING = 3;`  
`ANIMAL_CARE` |  An animal care job, such as Veterinarian. `ANIMAL_CARE = 4;`  
`ANIMAL_CARE_VALUE` |  An animal care job, such as Veterinarian. `ANIMAL_CARE = 4;`  
`ART_FASHION_AND_DESIGN` |  An art, fashion, or design job, such as Designer. `ART_FASHION_AND_DESIGN = 5;`  
`ART_FASHION_AND_DESIGN_VALUE` |  An art, fashion, or design job, such as Designer. `ART_FASHION_AND_DESIGN = 5;`  
`BUSINESS_OPERATIONS` |  A business operations job, such as Business Operations Manager. `BUSINESS_OPERATIONS = 6;`  
`BUSINESS_OPERATIONS_VALUE` |  A business operations job, such as Business Operations Manager. `BUSINESS_OPERATIONS = 6;`  
`CLEANING_AND_FACILITIES` |  A cleaning and facilities job, such as Custodial Staff. `CLEANING_AND_FACILITIES = 7;`  
`CLEANING_AND_FACILITIES_VALUE` |  A cleaning and facilities job, such as Custodial Staff. `CLEANING_AND_FACILITIES = 7;`  
`COMPUTER_AND_IT` |  A computer and IT job, such as Systems Administrator. `COMPUTER_AND_IT = 8;`  
`COMPUTER_AND_IT_VALUE` |  A computer and IT job, such as Systems Administrator. `COMPUTER_AND_IT = 8;`  
`CONSTRUCTION` |  A construction job, such as General Laborer. `CONSTRUCTION = 9;`  
`CONSTRUCTION_VALUE` |  A construction job, such as General Laborer. `CONSTRUCTION = 9;`  
`CUSTOMER_SERVICE` |  A customer service job, such s Cashier. `CUSTOMER_SERVICE = 10;`  
`CUSTOMER_SERVICE_VALUE` |  A customer service job, such s Cashier. `CUSTOMER_SERVICE = 10;`  
`EDUCATION` |  An education job, such as School Teacher. `EDUCATION = 11;`  
`EDUCATION_VALUE` |  An education job, such as School Teacher. `EDUCATION = 11;`  
`ENTERTAINMENT_AND_TRAVEL` |  An entertainment and travel job, such as Flight Attendant. `ENTERTAINMENT_AND_TRAVEL = 12;`  
`ENTERTAINMENT_AND_TRAVEL_VALUE` |  An entertainment and travel job, such as Flight Attendant. `ENTERTAINMENT_AND_TRAVEL = 12;`  
`FARMING_AND_OUTDOORS` |  A farming or outdoor job, such as Park Ranger. `FARMING_AND_OUTDOORS = 13;`  
`FARMING_AND_OUTDOORS_VALUE` |  A farming or outdoor job, such as Park Ranger. `FARMING_AND_OUTDOORS = 13;`  
`HEALTHCARE` |  A healthcare job, such as Registered Nurse. `HEALTHCARE = 14;`  
`HEALTHCARE_VALUE` |  A healthcare job, such as Registered Nurse. `HEALTHCARE = 14;`  
`HUMAN_RESOURCES` |  A human resources job, such as Human Resources Director. `HUMAN_RESOURCES = 15;`  
`HUMAN_RESOURCES_VALUE` |  A human resources job, such as Human Resources Director. `HUMAN_RESOURCES = 15;`  
`INSTALLATION_MAINTENANCE_AND_REPAIR` |  An installation, maintenance, or repair job, such as Electrician. `INSTALLATION_MAINTENANCE_AND_REPAIR = 16;`  
`INSTALLATION_MAINTENANCE_AND_REPAIR_VALUE` |  An installation, maintenance, or repair job, such as Electrician. `INSTALLATION_MAINTENANCE_AND_REPAIR = 16;`  
`JOB_CATEGORY_UNSPECIFIED` |  The default value if the category isn't specified. `JOB_CATEGORY_UNSPECIFIED = 0;`  
`JOB_CATEGORY_UNSPECIFIED_VALUE` |  The default value if the category isn't specified. `JOB_CATEGORY_UNSPECIFIED = 0;`  
`LEGAL` |  A legal job, such as Law Clerk. `LEGAL = 17;`  
`LEGAL_VALUE` |  A legal job, such as Law Clerk. `LEGAL = 17;`  
`MANAGEMENT` |  A management job, often used in conjunction with another category, such as Store Manager. `MANAGEMENT = 18;`  
`MANAGEMENT_VALUE` |  A management job, often used in conjunction with another category, such as Store Manager. `MANAGEMENT = 18;`  
`MANUFACTURING_AND_WAREHOUSE` |  A manufacturing or warehouse job, such as Assembly Technician. `MANUFACTURING_AND_WAREHOUSE = 19;`  
`MANUFACTURING_AND_WAREHOUSE_VALUE` |  A manufacturing or warehouse job, such as Assembly Technician. `MANUFACTURING_AND_WAREHOUSE = 19;`  
`MEDIA_COMMUNICATIONS_AND_WRITING` |  A media, communications, or writing job, such as Media Relations. `MEDIA_COMMUNICATIONS_AND_WRITING = 20;`  
`MEDIA_COMMUNICATIONS_AND_WRITING_VALUE` |  A media, communications, or writing job, such as Media Relations. `MEDIA_COMMUNICATIONS_AND_WRITING = 20;`  
`OIL_GAS_AND_MINING` |  An oil, gas or mining job, such as Offshore Driller. `OIL_GAS_AND_MINING = 21;`  
`OIL_GAS_AND_MINING_VALUE` |  An oil, gas or mining job, such as Offshore Driller. `OIL_GAS_AND_MINING = 21;`  
`PERSONAL_CARE_AND_SERVICES` |  A personal care and services job, such as Hair Stylist. `PERSONAL_CARE_AND_SERVICES = 22;`  
`PERSONAL_CARE_AND_SERVICES_VALUE` |  A personal care and services job, such as Hair Stylist. `PERSONAL_CARE_AND_SERVICES = 22;`  
`PROTECTIVE_SERVICES` |  A protective services job, such as Security Guard. `PROTECTIVE_SERVICES = 23;`  
`PROTECTIVE_SERVICES_VALUE` |  A protective services job, such as Security Guard. `PROTECTIVE_SERVICES = 23;`  
`REAL_ESTATE` |  A real estate job, such as Buyer's Agent. `REAL_ESTATE = 24;`  
`REAL_ESTATE_VALUE` |  A real estate job, such as Buyer's Agent. `REAL_ESTATE = 24;`  
`RESTAURANT_AND_HOSPITALITY` |  A restaurant and hospitality job, such as Restaurant Server. `RESTAURANT_AND_HOSPITALITY = 25;`  
`RESTAURANT_AND_HOSPITALITY_VALUE` |  A restaurant and hospitality job, such as Restaurant Server. `RESTAURANT_AND_HOSPITALITY = 25;`  
`SALES_AND_RETAIL` |  A sales and/or retail job, such Sales Associate. `SALES_AND_RETAIL = 26;`  
`SALES_AND_RETAIL_VALUE` |  A sales and/or retail job, such Sales Associate. `SALES_AND_RETAIL = 26;`  
`SCIENCE_AND_ENGINEERING` |  A science and engineering job, such as Lab Technician. `SCIENCE_AND_ENGINEERING = 27;`  
`SCIENCE_AND_ENGINEERING_VALUE` |  A science and engineering job, such as Lab Technician. `SCIENCE_AND_ENGINEERING = 27;`  
`SOCIAL_SERVICES_AND_NON_PROFIT` |  A social services or non-profit job, such as Case Worker. `SOCIAL_SERVICES_AND_NON_PROFIT = 28;`  
`SOCIAL_SERVICES_AND_NON_PROFIT_VALUE` |  A social services or non-profit job, such as Case Worker. `SOCIAL_SERVICES_AND_NON_PROFIT = 28;`  
`SPORTS_FITNESS_AND_RECREATION` |  A sports, fitness, or recreation job, such as Personal Trainer. `SPORTS_FITNESS_AND_RECREATION = 29;`  
`SPORTS_FITNESS_AND_RECREATION_VALUE` |  A sports, fitness, or recreation job, such as Personal Trainer. `SPORTS_FITNESS_AND_RECREATION = 29;`  
`TRANSPORTATION_AND_LOGISTICS` |  A transportation or logistics job, such as Truck Driver. `TRANSPORTATION_AND_LOGISTICS = 30;`  
`TRANSPORTATION_AND_LOGISTICS_VALUE` |  A transportation or logistics job, such as Truck Driver. `TRANSPORTATION_AND_LOGISTICS = 30;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-talent/latest/com.google.cloud.talent.v4beta1.JobCategory#com_google_cloud_talent_v4beta1_JobCategory_forNumber_int_) instead._  
`valueOf(String name)` |   
`values()` |   
  
## Methods   
  
---  
**Name** | **Description**  
`getDescriptorForType()` |   
`getNumber()` |   
`getValueDescriptor()` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 

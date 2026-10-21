---
url: https://docs.cloud.google.com/cortex/docs/data-product/
title: Data products overview \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:36:56.946115+00:00
---

# Data products overview  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/data-product/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data products overview

Data products in Cortex Framework represent the curated, logical packaging of data assets engineered to solve specific business problems. They serve as the ultimate business-facing layer, directly powering business intelligence (BI) dashboards, reporting tools, machine learning models, and autonomous agents.

Dataform pipelines function as the execution engine for Cortex Framework [available data products](https://docs.cloud.google.com/cortex/docs/data-product#available_data_products). They run extract, load, transform (ELT) processes that aggregate, join, and shape data from the standardized [data foundation layer](https://docs.cloud.google.com/cortex/docs/overview#data_foundation_layer) and, where applicable, other upstream data products into these final, consumer-ready structures.

## Key concepts

**Data asset** \- A pointer to a physical data resource, such as a BigQuery dataset, table, or view. A data product contains one or more assets.

**Data product** \- A curated, logical grouping of data assets, formally packaged to be discoverable, trusted, and accessible for solving specific business problems. Cortex Framework delivers two types of data products:

  * **Source-aligned data products** : A collection of tables in an analytical data model (for example, sales orders or customers). They feed from the [data foundation layer](https://docs.cloud.google.com/cortex/docs/overview#data_foundation_layer), serve as foundational entities, and can be used to feed more complex use case specific models.

  * **Consumption data products** : Specialized analytical models engineered for particular business scenarios, delivering complex KPI logic and high-fidelity metrics (for example, sales performance insights). Consumption data products typically consume and aggregate upstream data foundation modules, data products exposed by catalog modules, as well as source-aligned data products, to drive immediate decision-making.




For more information, see [**Available data products**](https://docs.cloud.google.com/cortex/docs/data-product#available_data_products) and [**Consumption data product samples**](https://docs.cloud.google.com/cortex/docs/solution-samples/overview) documentation.

You can extend Google Cloud Cortex Framework content by utilizing the [extensibility framework](https://docs.cloud.google.com/cortex/docs/extensibility-guide-data-product) to either manually develop custom data products or use the [agentic data product builder](https://docs.cloud.google.com/cortex/docs/agentic-skills-for-data-product-building) to seamlessly modify existing data products and create new ones from scratch.

## Available data products

The following table outlines the data products available within Cortex Framework, detailing their functional descriptions, source data, and supported sources.

Type | Data product | Data asset | Description | Source data | Supported sources  
---|---|---|---|---|---  
SAP ECC | SAP S/4HANA | SAP BDC  
Source-aligned | Any | Any | Any SAP BDC data product (SAP-managed or customer-managed) that is shared with the connected BigQuery Delta Share Catalog can be registered. | SAP BDC data products |  |  | ✅  
Accounting Documents | Accounting Documents Header | Accounting document headers at the granularity of Client(System), Company Code, Accounting Document Number, and Fiscal Year. | bkpf, tcurx | ✅ | ✅ |   
Accounting Documents Item | Accounting document items at the granularity of Client(System), Company Code, Accounting Document Number, Fiscal Year, and Line Item Number. | bkpf, bseg, t005, tcurx | ✅ | ✅ |   
Accounts Payable | Accounts Payable | Accounts payable journal entries at the granularity of Client(System), Ledger, Company Code, Fiscal Year, Document Number, and Line Item. | acdoca, bkpf, bseg |  | ✅ |   
Vendor Cleared Items | Vendor cleared items at the granularity of Client(System), Company Code, Vendor, Special G/L Transaction Type, Special G/L Indicator, Clearing Date, Clearing Document, Assignment, Fiscal Year, Document Number, and Line Item. | bkpf, bsak | ✅ |  |   
Vendor Open Items | Vendor open items at the granularity of Client(System), Company Code, Vendor, Special G/L Transaction Type, Clearing Date, Clearing Document, Assignment, Fiscal Year, Document Number, and Line Item. | bkpf, bsik | ✅ |  |   
Accounts Receivable | Accounts Receivable | Accounts receivable journal entries at the granularity of Client(System), Ledger, Company Code, Fiscal Year, Document Number, and Line Item. | acdoca, bkpf, bseg |  | ✅ |   
Customer Cleared Items | Customer cleared items at the granularity of Client(System), Company Code, Customer, Special G/L Transaction Type, Special G/L Indicator, Clearing Date, Clearing Document, Assignment, Fiscal Year, Document Number, and Line Item. | bkpf, bsad | ✅ |  |   
Customer Open Items | Customer open items at the granularity of Client(System), Company Code, Customer, Special G/L Transaction Type, Special G/L Indicator, Clearing Date, Clearing Document, Assignment, Fiscal Year, Document Number, and Line Item. | bkpf, bsid | ✅ |  |   
Addresses | Addresses | Addresses at the granularity of Client(System), Address Number, Valid From Date, Version ID for International Addresses, Person Number, and Sequence Number. | adrc, adr6, adrct | ✅ | ✅ |   
Agency Business Settlement Documents | Agency Settlement Document Headers | Agency settlement document headers at the granularity of Client(System) and Settlement Document Number. | wbrk | ✅ | ✅ |   
Agency Settlement Document Items | Agency settlement document items at the granularity of Client(System), Settlement Document Number, and Document Item Number. | wbrk, wbrp | ✅ | ✅ |   
Asset Documents | Asset Accounting Statistical Line Items | Captures statistical line items for asset postings from the SAP S/4HANA FAAT_DOC_IT table, including asset number, depreciation area, transaction type, posted amounts in company code and global currencies, and document metadata, enriched with calendar date dimensions. | faat_doc_it, tcurx |  | ✅ |   
Asset Annual Cumulative Balances | Tracks cumulative asset values (APC, ordinary, special, and unplanned depreciation) along with expired useful life attributes by fiscal year and depreciation area. | anlc, faat_ydda, tcurx | ✅ | ✅ |   
Asset Document Headers | Captures asset posting document header-level transaction metadata from SAP ANEK (such as company code, asset number, fiscal year, posting date, and entry time), enriched with calendar date dimensions to support asset transaction analysis. | anek, tcurx | ✅ |  |   
Asset Document Line Items | Captures asset posting document line item-level transaction metadata from SAP ANEP (such as depreciation area, transaction type, posted amount, ordinary depreciation, and interest), enriched with calendar date dimensions to support asset valuation and depreciation analysis. | anep, tcurx | ✅ |  |   
Asset Documents | Captures asset posting ledger transactions from the SAP S/4HANA Universal Journal (ACDOCA) joined with BKPF (such as asset number, depreciation area, transaction type, posted amounts in local and transaction currencies, and document metadata), filtered by asset account type ('A') and enriched with calendar date dimensions. | bkpf, acdoca, tcurx |  | ✅ |   
Asset Transaction Types | Details the business transaction types used in asset accounting, including capitalization flags, retirement rules, and group mappings. | tabw, tabwh, tabwt | ✅ | ✅ |   
Planned Depreciation and Revaluations | Captures planned depreciation values and revelations from the SAP S/4HANA FAAT_PLAN_VALUES table, including asset number, depreciation area, posting period, and planned amounts in company code and global currencies. | faat_plan_values, tcurx |  | ✅ |   
Bill of Materials | Bill of Materials Headers | Contains BOM header details including validity dates, base quantities, and BOM status. | stko | ✅ | ✅ |   
Bill of Materials Item Selections | Contains BOM item selection details mapping item nodes to alternative BOMs. | stas | ✅ | ✅ |   
Bill of Materials Items | Contains BOM item/component details, including component quantities, scrap percentages, and item categories. | stpo, stko | ✅ | ✅ |   
Budget Allocations | Budget Balances | Annual and overall budget allocations and balances per budget object. | bpja, bpge, tcurx | ✅ | ✅ |   
Budget Documents | Budget allocation document line items representing budget postings. | bpvg, tcurx | ✅ | ✅ |   
Billing Documents | Billing Document Headers | Billing document header details at the granularity of Client(System) and Billing Document. | vbrk | ✅ | ✅ |   
Billing Document Items | Billing document item details at the granularity of Client(System), Billing Document, and Item Number. | vbrk, vbrp | ✅ | ✅ |   
Billing Blocking Reasons | Billing blocking reasons at the granularity of Client(System), Language Key, and Billing Block. | tvfst | ✅ | ✅ |   
Business Partners | Business Partners | Business partners at the granularity of Client(System) and Business Partner. | but000 | ✅ | ✅ |   
Business Partner Addresses | Business partner addresses at the granularity of Client(System), Business Partner, Address Number, and Valid From. | adrc, adr6, adrct, but020 | ✅ | ✅ |   
Business Partner Bank Details | Business partner bank details at the granularity of Client(System), Business Partner, Bank Details ID, and Valid From. | but0bk | ✅ | ✅ |   
Cash and Liquidity Management | Cash Forecast Summaries | Summary records of cash management and forecast data for G/L accounts from the ECC FDSB table. | fdsb, t001, tcurx | ✅ |  |   
Liquidity Flows | Granular, real-time liquidity flows from the S/4HANA One Exposure from Operations (FQM_FLOW) table. | fqm_flow, tcurx |  | ✅ |   
Condition Contracts | Condition Contracts Header | Condition contracts header details at the granularity of Client(System) and Condition Contract Number. | wcocoh | ✅ | ✅ |   
Condition Contracts Item | Condition contracts item details at the granularity of Client(System), Condition Contract Number, and Item GUID. | wcocoi | ✅ | ✅ |   
Rebates Settlement Calendar | Rebates settlement calendar at the granularity of Client(System), Condition Contract Number, Settlement Date, and Settlement Date Sequential ID. | wb2_d_settl_cal | ✅ | ✅ |   
Condition Contract Settlement Detailed Statement | Condition contract settlement detailed statements at the granularity of Client(System), Condition Contract Number, Document Number, Document Item, and Business Volume Document keys. | wb2_d_bvdetail | ✅ | ✅ |   
Controlling Areas and Cost Elements | Controlling Area Assignment | Controlling area assignments at the granularity of Client(System), Company Code, and Business Area. | tka02 | ✅ | ✅ |   
Controlling Areas | Controlling areas at the granularity of Client(System) and Controlling Area. | tka01 | ✅ | ✅ |   
Cost Elements | Cost elements at the granularity of Client(System), Controlling Area, Cost Element, Valid To Date, and Language Key. | cskb, csku, tka01 | ✅ | ✅ |   
Controlling Documents | Controlling Document Headers | Controlling document headers containing metadata for controlling transactions. | cobk, tcurx | ✅ | ✅ |   
Controlling Document Period Line Items | Controlling document line items representing financial transactions across periods. | coep, tcurx | ✅ | ✅ |   
Controlling External Posting Cost Totals | Controlling external posting cost totals at the cost center/controlling area granularity. | cosp, tcurx | ✅ | ✅ |   
Controlling Internal Posting Cost Totals | Controlling internal posting cost totals representing internal allocation postings. | coss, tcurx | ✅ | ✅ |   
Controlling Commitment Line Items | Controlling commitment line items representing financial commitments and encumbrances. | cooi, tcurx | ✅ | ✅ |   
Cost and Profit Centers | Cost Centers | Cost centers at the granularity of Client(System), Controlling Area, Cost Center, Valid To Date, and Language Key. | csks, cskt | ✅ | ✅ |   
Profit Centers | Profit centers at the granularity of Client(System), Profit Center, Valid To Date, Controlling Area, and Language Key. | cepc, cepct | ✅ | ✅ |   
Currency Conversion | Currency Codes | Currency codes at the granularity of Client(System), Currency Code, and Language Key. | tcurc, tcurt, tcurx | ✅ | ✅ |   
Exchange Rates | Exchange rates at the granularity of Client(System), Exchange Rate Type, From Currency, To Currency, and Conversion Date. | tcurf, tcurr | ✅ | ✅ |   
Customers | Customers | Customer master data, customer number, name of customer, location, address, and similar information at the granularity of Client(System) and Customer number, Version ID for International Addresses and Valid from date.  | kna1, adrc | ✅ | ✅ |   
Delivery Documents | Delivery Document Headers | Delivery documents at the header level at the granularity of Client(System) and Delivery document number.  | tcurx, likp | ✅ | ✅ |   
Delivery Document Items | Delivery document items at the granularity of Client(System), Delivery document number and Item number of delivery document. | tcurx, likp, lips | ✅ | ✅ |   
Delivery Blocking Reasons | Delivery blocking reasons at the granularity of Client(System) and Language Key. | tvlst | ✅ | ✅ |   
Financial Hierarchies | Classic Sets Headers | Headers of classic SAP Sets. | setheader, setheadert, t002 | ✅ | ✅ |   
Classic Sets Leaves | Set leaves of classic SAP Sets. | setleaf | ✅ | ✅ |   
Classic Sets Nodes | Set nodes and hierarchy structure of classic SAP Sets. | setnode | ✅ | ✅ |   
Cost Center Group Hierarchy | Cost center group hierarchical structure with descriptions. | ECC: setheadert  
S/4H: sethanahier0101 | ✅ | ✅ |   
Cost Center Hierarchy Flattened | Flattened cost center hierarchy with names and descriptions up to multi-level nodes. | ECC: t002, setnode, setleaf, csks, setheader, cskt  
S/4H: t002, sethanahier0101, csks, cskt | ✅ | ✅ |   
Financial Hierarchy Directories | Directory and metadata of financial hierarchies from S/4HANA HRRP tables. | hrrp_directory |  | ✅ |   
Financial Hierarchy Nodes | Financial hierarchy nodes and node descriptions from S/4HANA HRRP tables. | hrrp_node, hrrp_nodet |  | ✅ |   
Profit Center Group Hierarchy | Profit center group hierarchical structure with descriptions. | ECC: setheadert  
S/4H: sethanahier0106 | ✅ | ✅ |   
Profit Center Hierarchy Flattened | Flattened profit center hierarchy with names and descriptions up to multi-level nodes. | ECC: t002, setnode, setleaf, cepc, setheader, cepct  
S/4H: t002, sethanahier0106, cepc, cepct | ✅ | ✅ |   
Financial Statement Structure & Versions | Financial Statement Structure Items | Financial statement structure items at the granularity of Client(System), Financial Statement Version, and Node ID. | fagl_011pc | ✅ | ✅ |   
Financial Statement Structure Text | Financial statement structure texts at the granularity of Client(System), Financial Statement Version, Language Key, Financial Statement Item, Text Type, and Line Number. | fagl_011qt | ✅ | ✅ |   
Financial Statement Structure Version Assignments | Financial statement structure version assignments at the granularity of Client(System), Financial Statement Version, Financial Statement Item, Chart of Accounts, and G/L Account From. | fagl_011zc | ✅ | ✅ |   
Fiscal Year Variants | Fiscal Year Variants | Fiscal year variant configurations at the granularity of Client(System) and Fiscal Year Variant. | t009 | ✅ | ✅ |   
Fiscal Year Variant Periods | Fiscal year variant periods at the granularity of Client(System), Fiscal Year Variant, Year, Calendar Month, and Calendar Day. | t009b | ✅ | ✅ |   
Fixed Assets | Fixed Assets Master | Fixed assets master details at the granularity of Client(System), Company Code, Asset Number, Asset Subnumber, and Language Key. | anla, anlh, ankt, t095t, t098t | ✅ | ✅ |   
Depreciation Terms | Depreciation terms at the granularity of Client(System), Company Code, Asset Number, Asset Subnumber, Depreciation Area, Valid To Date, and Language Key. | anlb, t090nat, t093b, t093c, t093t | ✅ | ✅ |   
Time Dependent Asset Allocations | Time-dependent asset allocations at the granularity of Client(System), Company Code, Asset Number, Asset Subnumber, and Valid To Date. | anlz | ✅ | ✅ |   
General Ledger Accounts | General Ledger Accounts | General ledger accounts at the granularity of Client(System), Chart of Accounts, G/L Account Number, and Language Key. | ska1, skat | ✅ | ✅ |   
General Ledger Items | General Ledger Actual Line Items | General ledger actual line items from FAGLFLEXA containing balances and transactional line item amounts. | faglflexa, t001, tcurx | ✅ |  |   
Global Settings | Company Codes | Company codes at the granularity of Client(System) and Company Code. | t001 | ✅ | ✅ |   
Languages | Languages at the granularity of Language Key and Description Language. | t002, t002t | ✅ | ✅ |   
Countries | Countries at the granularity of Country Key and Language Key. | t005, t005t | ✅ | ✅ |   
Country Dialing Codes | Country dialing codes at the granularity of Client(System) and Country Key. | t005k | ✅ | ✅ |   
Country Tax Regions | Country tax regions at the granularity of Client(System), Country Key, Region, and Language Key. | t005s, t005u | ✅ | ✅ |   
System Status Texts | System status texts at the granularity of System Status Key and Language Key. | tj02t | ✅ | ✅ |   
Inventory and Special Stocks | Sales Order Stock | Material stock allocated to specific sales orders. | mska, t148t | ✅ |  |   
Sales Order Stock with Vendor | Sales order stock specifically allocated with vendor information. | msfd, t148t | ✅ |  |   
Special Stocks from Vendor | Special stock owned/consigned by vendors. | mkol, t148t | ✅ |  |   
Special Stocks with Customer | Special stock consigned or placed at customer sites. | mslb, t148t | ✅ |  |   
Special Stocks with Vendor | Vendor special stocks with descriptive indicator labels. | msku, t148t | ✅ |  |   
Ledger Master | Ledger Master | Ledger master details containing ledger characteristics and language-specific descriptions. | t881, t881t | ✅ | ✅ |   
Material Batches | Material Cross Plant Batches | Material cross-plant batches at the granularity of Client(System), Material Number, Batch Number, and Language Key. | makt, mch1 | ✅ | ✅ |   
Material Plant Batches | Material plant batches at the granularity of Client(System), Material Number, Plant, Batch Number, and Language Key. | makt, mcha, t001w | ✅ | ✅ |   
Material Batch Stocks | Material batch stocks at the granularity of Client(System), Material Number, Plant, Storage Location, Batch Number, and Language Key. | makt, mchb, t001w | ✅ | ✅ |   
Material Ledger | Material Ledger Header | Contains master records (from CKMLHD) linking a material, plant, and valuation type to a unique valuation header number (kalnr). | ckmlhd | ✅ | ✅ |   
Material Ledger Period Totals | Exposes stock quantity, value, standard price, periodic unit price, and price/exchange rate differences (from CKMLCR) per header, period, value structure type, and currency type. | ckmlcr, tcurx | ✅ | ✅ |   
Material Valuation Area | Lists valuation area configurations (from T001K, T001W, T001), including the company code name, plant name, and indicating if Material Ledger is active. | t001k, t001w, t001 | ✅ | ✅ |   
Material Valuation | Exposes current standard and moving average valuation details for ECC from MBEW, including rich details like planned/future prices and costing variants. | mbew, tcurx | ✅ |  |   
Material Valuation History | Exposes historical valuation details for ECC. Union of current (MBEW) and historical (MBEWH) valuation tables, limited to core valuation fields. | mbew, mbewh | ✅ |  |   
Materials Movements | Material Documents  | Material documents at the granularity of Client(System), Document Number, Document Year and Document Item.  | ECC: tcurx, mseg  
S/4H: tcurx, matdoc | ✅ | ✅ |   
Material Movement Types | Material movement types at the granularity of Client(System), Language Key, Movement Type, Special Stock Indicator, Movement Indicator, Receipt Indicator and Consumption Related Movement Type. | t156, t156t | ✅ | ✅ |   
Materials | Materials | Materials at the granularity of Client(System) and Material Number. | mara, makt | ✅ | ✅ |   
Material Types | Material types at the granularity of Client(System), Material Type and Language Key. | t134, t134t | ✅ | ✅ |   
Material Groups | Material groups at the granularity of Client(System), Material Group, and Language Key. | t023, t023t | ✅ | ✅ |   
Material Plants | Material plants at the granularity of Client(System), Material Number and Plant. | marc | ✅ | ✅ |   
Materials by Storage Location | Exposes material inventory levels, multilingual material descriptions, plant names, and storage location names at the storage location level | mard, makt, t001w, and t001l | ✅ | ✅ |   
Material to BOM Link | Exposes link between materials and bills of materials, including plant and BOM usage from MAST. | mast | ✅ | ✅ |   
Object Statuses | Individual Object Statuses | Consolidated view of status information for various SAP objects (such as orders, projects, and WBS elements) to track historical and current statuses from JEST. | jest | ✅ | ✅ |   
Order Master Data | Order Master Data | Exposes order master data from AUFK, including order category, order type, order status, order currency, controlling area, and cost center. | aufk, tcurx | ✅ | ✅ |   
Plants and Storage | Plants | Plants at the granularity of Client(System) and Plant. | t001w | ✅ | ✅ |   
Storage Locations | Storage locations at the granularity of Client(System), Plant, and Storage Location. | t001l | ✅ | ✅ |   
Product Hierarchies | Flattened Product Hierarchies | Flattened representation of the product hierarchy up to 6 levels, showing codes and descriptions for each level. | t179, t179t | ✅ | ✅ |   
Product Hierarchies | Master data for product hierarchies, including node codes, levels, and descriptions. | t179, t179t | ✅ | ✅ |   
Production Orders | Production Order Header | Production order header details including quantities, scheduling dates, status, and plant assignments from AUFK and AFKO. | aufk, afko, tcurx | ✅ | ✅ |   
Production Order Item | Production order line item details including material numbers, target and delivered quantities, and settlement rules from AUFK and AFPO. | aufk, afpo, tcurx | ✅ | ✅ |   
Project Structure | Project Structure | Project structure at the granularity of Client(System), Project Internal ID, and WBS Element Internal ID.  | proj, prhi, prps, prte | ✅ | ✅ |   
Project Info Database | Project info database records at the granularity of Client(System), Object Number, Ledger, Value Type, Object Indicator, Fiscal Year, Value Category, Budget Type, Version, Category, Fund, Transaction Currency, and Period Block. | rpsco | ✅ | ✅ |   
Purchasing Documents | Purchasing Document Headers | Provides details about purchase orders at the header level. This view is at the granularity of Client(System) and Purchasing document number. | ekko | ✅ | ✅ |   
Purchasing Document Items | Details about purchase order items. This view is at the granularity of Client(System), Purchasing document number and Item number of purchasing document. | tcurx, ekpo, ekko | ✅ | ✅ |   
Purchasing Document Schedule Lines | Details about purchase documents at schedule line level, including KPIs such as Open Quantity. The granularity of this view is Client(System), Purchasing Document Number, Item Number of Purchasing Document and Delivery Schedule Line Counter. | tcurx, ekpo, ekko, eket | ✅ | ✅ |   
Purchasing Document Account Assignments | Details about purchase document account assignments, distributing values or quantities to cost centers, orders, WBS elements, or assets. This view is at the granularity of Client(System), Purchasing Document Number, Item Number of Purchasing Document, and Sequence Number of Account Assignment. | tcurx, ekkn, ekko | ✅ | ✅ |   
Purchasing Document Types | Configurations and language-specific descriptions for purchasing document categories and types. This view is at the granularity of Client(System), Purchasing Document Category, Purchasing Document Type, and Language Key. | t161, t161t | ✅ | ✅ |   
Purchasing Document Vendor Confirmations | Vendor confirmation details for purchasing document items, such as confirmation categories, quantities, delivery dates, and references. This view is at the granularity of Client(System), Purchasing Document Number, Item Number of Purchasing Document, and Sequential Number. | ekes | ✅ | ✅ |   
Purchasing Documents History | Transactional history of purchasing documents, tracking goods receipts, invoice receipts, and other events. This view is at the granularity of Client(System), Purchasing Document Number, Item Number of Purchasing Document, Sequence Number of Account Assignment, Transaction/Event Type, Material Document Year, Material Document Number, and Material Document Item. | tcurx, ekbe | ✅ | ✅ |   
Purchasing Organizational Structure | Purchasing Groups | Purchasing groups at the granularity of Client(System) and Purchasing Group. | t024 | ✅ | ✅ |   
Purchasing Organizations | Purchasing organization master data at the granularity of Client(System) and purchasing organization. | t024e | ✅ | ✅ |   
Sales Documents | Sales Document Headers | Sales documents at the header level, at the granularity of Client(System), and Sales document number. | tcurx, vbak | ✅ | ✅ |   
Sales Document Items | Sales document items, at the granularity of Client(System), Sales document number and Item number of sales document. | tcurx, vbap | ✅ | ✅ |   
Sales Document Partners | Sales document partner details at the granularity of Client(System), Sales Document, Sales Document Item, and Partner Function. | vbpa | ✅ | ✅ |   
Sales Document Schedule Lines | Sales documents at schedule line level, including KPIs such as Open Quantity and In-Transit Quantity. The granularity of this view is Client(System), Sales Document Number, Item Number of Sales Document and Delivery Schedule Line Counter. | tcurx, vbep | ✅ | ✅ |   
Sales Document Header Statuses | Sales document header statuses at the granularity of Client(System) and Sales Document. | vbak, vbuk | ✅ | ✅ |   
Sales Document Item Statuses | Sales document item statuses at the granularity of Client(System), Sales Document, and Sales Document Item. | vbap, vbup | ✅ | ✅ |   
Sales Document Flow | Sales document flows at the granularity of Client(System), Preceding Document, Preceding Item, Subsequent Document, and Subsequent Item. | vbfa | ✅ | ✅ |   
Sales Organizational Structure | Sales Organizations | Sales organizations at the granularity of Client(System), Sales Organization and Language Key. | tvko, tvkot | ✅ | ✅ |   
Distribution Channel | Distribution channels at the granularity of Client(System), Distribution Channel and Language Key. | tvtw, tvtwt | ✅ | ✅ |   
Divisions | Divisions at the granularity of Client(System), Division and Language Key. | tspa, tspat | ✅ | ✅ |   
Sales Pricing Conditions | Sales Pricing Conditions (ECC) | Sales pricing conditions containing conditions, rates, calculation types, and values for ECC. | konv | ✅ |  |   
Pricing Elements (S/4HANA) | Pricing elements (transactional data) containing conditions, rates, calculation types, and values for S/4HANA. | prcd_elements |  | ✅ |   
Treasury Market Data | Security Classes | Security class master records containing key attributes for securities. | vwpanla | ✅ | ✅ |   
Security Prices | Security daily market prices at the granularity of Security ID, Price Source, and Price Date. | atras | ✅ | ✅ |   
Treasury Positions | Financial Transaction Headers | Treasury financial transaction header records. | vtbfha, t001, tcurx | ✅ | ✅ |   
Financial Transaction Flows | Treasury financial transaction itemized flows. | vtbfhapo, t001, tcurx | ✅ | ✅ |   
Financial Transaction Activities | Treasury financial transaction execution activities. | vtbfhazu, t001, tcurx | ✅ | ✅ |   
Financial Transaction NPVs | Treasury financial transaction Net Present Values (NPV). | vtvbar, t001, tcurx | ✅ | ✅ |   
Units of Measurement | Units of Measurement | Units of measurement at the granularity of Client(System), Unit of Measurement, and Language Key. | t006, t006a, t006t | ✅ | ✅ |   
Universal Journal | Universal Journal Entry Line Items | Universal journal entry line items at the granularity of Client, Ledger, Company Code, Fiscal Year, Accounting Document Number, and Line Item. | acdoca, tcurx |  | ✅ |   
Universal Journal Entry Ledgers | Universal journal entry ledgers at the granularity of Client, Ledger, and Language. | finsc_ledger, finsc_ledger_t |  | ✅ |   
Group Journal Entries | Group journal entries at the granularity of Client, Ledger, Dimension, Fiscal Year, Document Number, Line Item, and Language Key. | acdocu, fincs_ref_vers_r, tcurx, tf200, tf201 |  | ✅ |   
Vendor Invoices | Vendor Invoice Headers | Vendor invoice headers at the granularity of Client(System), Invoice Document Number, and Fiscal Year. | rbkp | ✅ | ✅ |   
Vendor Invoice Items | Vendor invoice items at the granularity of Client(System), Invoice Document Number, Fiscal Year, and Invoice Item Number. | rbkp, rseg | ✅ | ✅ |   
Vendor Invoice Account Assignments | Vendor invoice account assignments at the granularity of Client(System), Invoice Document Number, Fiscal Year, Invoice Item Number, Sequential Number of Account Assignment, and Sequential Number for Coding Block.  | rbco, rbkp | ✅ | ✅ |   
Vendors | Vendors | Vendor master data, vendor number, name of vendor, location, address, and similar at the granularity of Client(System) and Vendor number, Version ID for International Addresses and Valid from date. | lfa1, adrc | ✅ | ✅ |   
  
## Solution samples

Cortex Framework [solution samples](https://docs.cloud.google.com/cortex/docs/solution-samples/overview) provide an opinionated approach and sample code to help you get started quickly to address specific business scenarios. Solution sample business logic is built on Cortex Framework [data foundation](https://docs.cloud.google.com/cortex/docs/data-foundation) or [data products](https://docs.cloud.google.com/cortex/docs/data-product) layer data assets.

Compared to standard data products, solution samples require additional implementation effort to become production-ready.

The following solution samples are available:

Type | Solution sample | Description | Source data assets | Supported sources  
---|---|---|---|---  
SAP ECC | SAP S/4HANA | SAP BDC  
Consumption | [Sales Performance Insights](https://docs.cloud.google.com/cortex/docs/solution-samples/sales-performance-insights) | Reporting view providing insights into sales documents, delivery statuses, customer and product dimensions, and overdue delivery tracking. | **SAP ERP** required Cortex Framework source-aligned data products: Customers, Materials, Delivery Documents, Sales Documents, Sales Organizational Structure.  
**SAP BDC** required data products: Customer, Sales Order | ✅ | ✅ | ✅  
Consumption | [Supplier Spend Analysis](https://docs.cloud.google.com/cortex/docs/solution-samples/supplier-spend-analysis) | Reporting view providing instant visibility into supplier spend position across materials, vendors, and purchasing organizations to maximize procurement value.  
  
| **SAP ERP** required Cortex Framework source-aligned data products: Materials, Purchasing Documents, Purchasing Organizational Structure, Vendors. **SAP BDC** required data products: Supplier, Procurement Configuration Data, Purchasing Organization, Purchase Order. | ✅ | ✅ | ✅  
  
For further information, see [Solution samples](https://docs.cloud.google.com/cortex/docs/solution-samples/overview).

## Google Cloud Cortex Framework v6 compatibility layer

The [Google Cloud Cortex Framework v6 Compatibility Layer](https://docs.cloud.google.com/cortex/docs/v6-compatibility) layer ensures backward compatibility by providing schema-compatible models for the legacy Cortex v6 SAP reporting data products. This allows downstream conusmers, such as Cortex Framework v6 Looker dashboards and custom reporting scripts, to run seamlessly on a Cortex v7 deployment without requiring query modifications.

Cortex v6 compatibility data products are provided for the following business domains:

Type | Compatibility module | Description | Source data assets | Supported sources  
---|---|---|---|---  
SAP ECC | SAP S/4HANA  
Compatibility | **Master Data**  
  
`sap_cortex_v6_compatibility_master_data` | Publishes schema-compatible master data entities including addresses, calendar and fiscal date dimensions, companies, customers, material groups, material plants, material types, storage locations, vendors, plants, profit centers, cost centers, and sales organizations.  
  
**Cortex Namespace:** cortex_v6_compatibility | [See v6 data model](https://docs.cloud.google.com/cortex/docs/v6/operational-sap) | ✅ | ✅  
Compatibility | **Accounts Payable**  
  
`sap_cortex_v6_compatibility_accounts_payable` | Provides reporting views for Accounts Payable, invoice tracking, cash discount utilization, days payable outstanding, and accounts payable turnover.  
  
**Cortex Namespace:** cortex_v6_compatibility | [See v6 data model](https://docs.cloud.google.com/cortex/docs/v6/operational-sap) | ✅ | ✅  
Compatibility | **Finance**  
  
`sap_cortex_v6_compatibility_finance` | Generates core financial reporting views such as General Ledger accounting documents, accounts receivable tracking, Balance Sheet, Profit and Loss statements, and flattened hierarchies for cost centers and profit centers.  
  
**Cortex Namespace:** cortex_v6_compatibility | [See v6 data model](https://docs.cloud.google.com/cortex/docs/v6/operational-sap) | ✅ | ✅  
Compatibility | **Inventory**  
  
`sap_cortex_v6_compatibility_inventory` | Calculates key inventory metrics, stock weekly and monthly snapshots, stock per plant, stock unrestricted versus sales, and slow-moving thresholds.  
  
**Cortex Namespace:** cortex_v6_compatibility | [See v6 data model](https://docs.cloud.google.com/cortex/docs/v6/operational-sap) | ✅ | ✅  
Compatibility | **Purchasing**  
  
`sap_cortex_v6_compatibility_purchasing` | Exposes procurement reporting views, purchase document history and flows, vendor performance metrics, and purchase order fulfillment/lead time statistics.  
  
**Cortex Namespace:** cortex_v6_compatibility | [See v6 data model](https://docs.cloud.google.com/cortex/docs/v6/operational-sap) | ✅ | ✅  
Compatibility | **Sales (Order to Cash)**  
  
`sap_cortex_v6_compatibility_sales` | Generates standard sales performance and Order-to-Cash views, including deliveries, billing documents, sales order pricing and statuses, one touch order metrics, and sales fulfillment facts.  
  
**Cortex Namespace:** cortex_v6_compatibility | [See v6 data model](https://docs.cloud.google.com/cortex/docs/v6/operational-sap) | ✅ | ✅  
  
For more information, see [Cortex v6 Compatibility Layer](https://docs.cloud.google.com/cortex/docs/v6-compatibility) documentation. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

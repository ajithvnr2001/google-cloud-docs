---
url: https://docs.cloud.google.com/carbon-footprint/docs/methodology/
title: Carbon Footprint reporting methodology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:59.336553+00:00
---

# Carbon Footprint reporting methodology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/carbon-footprint/docs/methodology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Carbon Footprint ](https://docs.cloud.google.com/carbon-footprint/docs/view-carbon-data)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Carbon Footprint reporting methodology

This page explains the background, high-level methodology, and technical details behind the customer-specific greenhouse gas emissions reports provided by Carbon Footprint. Any future changes to data sources and methodology are captured in the Release Notes.

## About Carbon Footprint reporting

To help customers run their business with as light a footprint as possible, Google Cloud offers Carbon Footprint. It provides visibility for each customer into the climate impacts of [products purchased from Google Cloud](https://docs.cloud.google.com/carbon-footprint/docs/covered-services) so that customers can report on and take action to reduce those impacts.

Google Cloud customers generally use a diverse portfolio of Google Cloud products in multiple regions, making the tracking of their workloads' carbon footprint complex. To give customers a report tailored to their specific carbon footprint, Google looks at the carbon emissions produced by the computing infrastructure supporting its internal services. Google allocates those emissions to each Google Cloud product, and allocates the emissions to a customer based on the customer's usage of those Google Cloud products.

The Google Cloud customer-specific greenhouse gas emissions data provided by the Carbon Footprint report has not been third-party verified or assured. Any updates to our methodology or the data sources might result in material changes to our calculations and might result in the current and previous Google Cloud customer-specific greenhouse gas emissions data provided by the Carbon Footprint report to be adjusted.

## Behind the methodology

Carbon Footprint reports are prepared according to the widely recognized [Greenhouse Gas Protocol carbon reporting and accounting standards](https://ghgprotocol.org/standards) (GHGP), which provide detailed guidance for emission reports. 

As Google Cloud allocates its emissions (including Google Cloud's Scope 1, 2, and 3) to all customers based on usage, customers can then integrate the allocated Google Cloud emissions data into their own reports as Scope 3 emissions (indirect emissions related to the value chain).

![Apportionment and reporting flow](https://cloud.google.com/carbon-footprint/docs/apportionment_illustration.png)

Carbon Footprint uses the GHGP's _location-based_ and _market-based_ reporting standards in reports and dashboards.

  * _Location-based_ scope 2 emissions data represent emissions arising from all electricity generation sources in use at a given location. Location-based emissions data don't take into account Google's renewable power purchase agreements or other contracts for carbon-free electricity. As such, these metrics help customers understand how their Google Cloud product choices and use patterns affect greenhouse gas emissions without factoring in Google's carbon-free electricity purchases.

  * _Market-based_ scope 2 emissions data includes the impact of Google's carbon-free electricity purchases to the appropriate data centers according to the GHGP's market-based method and standards. Google Cloud customers seeking to compile annual Scope 3 emissions inventories for their own products and services will likely find the market-based footprint most useful.




Carbon Footprint builds its calculations from bottom-to-top, relying heavily on machine-level power and activity monitoring inside Google data centers. This lets us allocate emissions to the internal services that are directly using these machines or driving machine purchasing decisions. This level of granularity ultimately enables us to allocate emissions to customers based on their specific usage.

In addition to the different ways that _location-based_ and _market-based_ emissions data account for Google's carbon-free electricity purchases, Carbon Footprint also uses different granularity levels of the emission factors when estimating _location-based_ and _market-based_ emissions:

  * _Hourly_ greenhouse gas emission factors are used to calculate _location-based_ emissions. That is because the electricity generators supplying electricity to the grid are constantly changing; an hourly greenhouse gas emission factor takes into account the mix of generation sources in use hour-by-hour. When matched with hourly electricity load data, this calculation method produces an emissions figure that is sensitive to the relationship between electricity demand on the grid and the resources called to supply it. The increased granularity of the emissions calculation is more suitable for optimizing workload location and timing to reduce your operational greenhouse gas emissions.
  * _Annual_ greenhouse gas emission factors are used to calculate _market-based_ emissions. That is because these are the emissions factors that are most often used in other Scopes of corporate greenhouse gas accounting. These emissions factors combined with the impact of Google's carbon-free electricity purchases makes it a suitable data source for including in reported Scope 3 emissions inventories. 



Using machine-level data and hourly emission factors is a new approach and therefore _these emissions reports have not yet been third-party verified or assured._ Whereas Google annually obtains [third-party assurance](https://www.gstatic.com/gumdrop/sustainability/alphabet-fy2021-environmental-indicators-assurance-letter.pdf) from an independent, accredited auditor for Google's top down footprint, the data streams and processes required to produce these customer reports have not been similarly verified or assured. However, a third party performed a [detailed review](https://services.google.com/fh/files/misc/3degrees_cloud_services_review_statement_final.pdf) of our methodology for calculating and allocating GHG emissions arising from Google Cloud products to individual customers per GHG Protocol to critique and improve our work, and we look forward to further refinements as this effort matures.

## Boundaries

The Carbon Footprint report encompasses emissions arising from the following activities:

  * Scope 1 
    * Fossil fuels combusted on-site, such as diesel for backup power, natural gas for heating, and fuels used in fleet vehicles.
    * Fugitive emissions from data center HVAC system coolants.
  * Scope 2

    * [Google Cloud product](https://docs.cloud.google.com/carbon-footprint/docs/covered-services) electricity use, including that from Google-owned compute and networking equipment as well as ancillary electricity services such as cooling and lighting, whether inside a Google-owned data center or a facility owned by others (location-based and market-based calculations).
  * Scope 3

    * Upstream lifecycle (embodied) emissions of data center equipment.
    * Upstream lifecycle (embodied) emissions of data center buildings.
    * Business travel and commuting associated with employees who work at Google data centers.
    * Generating electricity that is subsequently lost during transmission and distribution.
    * Extraction, production, and transportation of fuels used to generate grid electricity.



The Carbon Footprint report excludes emissions arising from the following activities:

  * Emissions arising from small equipment deployments at internet service providers' partners.
  * Emissions from Google networking equipment deployed outside data centers.
  * Downstream end-of-life emissions of data center equipment and buildings.
  * Embodied emissions associated with grid electricity generation facilities and equipment. 



## Methodology

The Google Cloud customer-specific carbon footprint report (the "Carbon Footprint report"), is calculated automatically. This section describes how Google Cloud makes those calculations.

### Key concepts

  * **Google Cloud is a shared computing platform.** Its compute resources -- processing power, memory, storage, networking, etc. -- are shared across Google Cloud customers.
  * **Google is organized around units of functionality called internal services.** An internal service is a particular software functionality that's run on Google's data center machines. Google Cloud products use internal services and are consumed as [customer-facing product units (SKUs)](https://docs.cloud.google.com/skus).

  * **Electricity use is one of Google Cloud's largest sources of greenhouse gas emissions.** Data centers consolidate compute resources into shared buildings. These buildings consume electricity to run the computing equipment and additional power for lights, cooling, power systems, and other ancillary needs.

  * **Electricity is provided by a wide variety of generation plants operating on individual grids all over the world.** The greenhouse gases arising from electricity generation vary with the generation fuel (e.g., natural gas, coal, wind, sun, water) among other factors. Each grid's generation sources differ, and within a grid, the sources will differ over the course of a day.

  * **Disaggregating Google Cloud's electricity use and its resulting carbon footprint to specific products and customers presents a technical conundrum.** Determining a customer's footprint is very complex due to the layers of shared resources called upon to serve customer compute needs. Developing new allocation methodologies and assumptions (as discussed in detail below) enables Google Cloud to present customer footprint reports that are appropriate and representative of each customer's cloud computing use and product choices.




### Calculation summary

Carbon Footprint first calculates energy use as a function of compute usage and data center resource requirements. Then, Carbon Footprint calculates location-based and market-based carbon emissions from electricity use, and allocates those emissions across customers and further across each customer's purchased products. The carbon emissions from electricity per customer and product are then augmented with proportional allocations of emissions arising from the non-electricity sources.  
The market-based emissions metrics match Google's clean electricity purchases to relevant data center loads to establish regional market-based electricity emission factors wherever Google purchases clean energy. In the market-based emission reports, the regional market-based emission factors replace the location-based emission factors.

#### Energy use and allocation to internal services

In order to allocate the total machine energy usage to internal services, Google separately evaluates the energy used when running a workload ("dynamic power") against the energy used when machines are idle ("idle power"). Each machine's hourly dynamic power is allocated to the internal services it supported that hour, based on relative internal service CPU usage. Machine idle power is allocated to each internal service based on its _resource allocation_ (CPU, RAM, SDD, HDD) in the data center.

Overhead energy use–power systems, cooling and lights–is allocated hourly to every machine, and its users, based on the machine's total energy use that hour.

Google's shared infrastructure services track the usage of other internal services that call them. This enables the shared infrastructure services' energy usage to be reallocate to those internal services based on their relative usage. For some internal services that don't have sufficient usage data, Google uses internal costs to reallocate the shared infrastructure's energy consumption.

When these calculations and allocations are complete, we have hourly power use allocated to each internal service in each data center.

Energy consumption associated with each customer's usage is available for customers participating in a private preview.

#### Greenhouse gas emissions from electricity: location-based calculations

Google calculates location-based greenhouse gas emissions on an hourly basis by multiplying location-specific energy use by a grid electricity carbon emission intensity factor. This reflects the actual mix of power sources (fossil fuels, renewables, etc.) feeding into the grid in the location of energy consumption. Notably, location-based Scope 2 emissions don't account for energy purchasing choices or contracts – like energy attribute certificates (EACs) or power purchase agreements (PPAs). 

The hourly grid carbon emission intensity data incorporated into Carbon Footprint reports encompasses only the emissions associated with electricity generation; it does not include other lifecycle stages. The hourly emission factor data is provided by [Electricity Maps](https://www.electricitymap.org/map). Where Electricity Maps data is unavailable, Google uses country-specific annual average carbon emission intensity factors published by the [International Energy Agency](https://www.iea.org/data-and-statistics/data-products).

To calculate emissions, Google multiplies the hourly energy use for each internal service at each location by the appropriate carbon emission intensity factor for that hour and location to determine the internal service's location-based electricity carbon footprint per hour and location.

#### Greenhouse gas emissions from electricity: market-based calculations

The market-based electricity footprint is estimated by matching Google's clean electricity purchases to relevant data-center loads according to GHGP standards.

Google calculates its market-based emissions on an annual basis, taking into account the actual generation of our clean electricity contract facilities and the electricity used at each site. This calculation uses publicly-available annual emissions factors from government sources, published by the International Energy Agency. 

In each region where we purchase clean electricity, a market-based annual emissions total is calculated for Google's data centers. The location-based electricity emissions are scaled down using the ratio of the previous year's renewable electricity percentage in the region. This scaling factor is multiplied by the granular location-based emissions calculations in the appropriate region to create monthly market-based emission reports broken down by customer and product.

The market-based scaling factor is updated once per year, as it relies on the market-based emissions calculations for Google as a whole. For this reason, the market-based emission reports don't provide a dynamic view of Google's electricity purchases and renewable generation at any given time; rather, they are representative of our renewable energy activity from the previous year.

The GHGP Scope 2 guidance limits zero-emission claims from purchased clean energy to those instances where the clean energy is generated and then used in the same geographic region and within a reasonable timespan.

Note that the emission factors differ between location-based and market-based emissions data.

  * _Hourly_ greenhouse gas emission factors are used to calculate _location-based_ emissions. That's because the electricity generators supplying electricity to the grid are constantly changing; an hourly greenhouse gas emission factor takes into account the mix of generation sources in use hour-by-hour. When matched with hourly electricity load data, this calculation method produces an emissions figure that is sensitive to the relationship between electricity demand on the grid and the resources called to supply it. The increased granularity of the emissions calculation is more suitable for optimizing workload location and timing to reduce your operational greenhouse gas emissions.
  * _Annual_ greenhouse gas emission factors are used to calculate _market-based_ emissions. That's because these are the emissions factors that are most often used in other Scopes of corporate greenhouse gas accounting. These emissions factors combined with the impact of Google's carbon-free electricity purchases makes it a suitable data source for including in reported Scope 3 emissions inventories.



#### Electricity footprint allocation to SKUs

Every Google Cloud product is consumed as [customer-facing product units](https://docs.cloud.google.com/skus), identified by their unique SKUs. Google links each SKU to the internal service that provides it (which often has a one-to-one mapping to the equivalent Google Cloud product). Not all Google Cloud products are [covered by the Carbon Footprint report](https://docs.cloud.google.com/carbon-footprint/docs/covered-services) because this mapping isn't always possible. SKU usage is the primary means of allocating each Google Cloud product's total electricity carbon footprint amongst its customers.

Google first quantifies each SKU's emissions footprint. An internal service's carbon footprint is divided amongst its SKUs proportional to their usage (quantity purchased) and list prices (all in US dollars), while also accounting for different carbon intensities in each location where the internal service is deployed. This allocation is solved as a series of equations that satisfy the following principles:

  * SKUs for a given internal service deployed in the same location have carbon footprints that are proportional to their list price
  * A specific SKU for a specific internal service, deployed in multiple locations, has different carbon footprints in each location, proportional to the grid carbon intensity in each location
  * The aggregated footprint of all the SKUs within each internal service is equal to the total carbon footprint of the internal service, plus some overhead for certain activities that are not accounted for in the internal service allocations described above. The carbon electricity footprint aggregated across all SKUs is equal to the total Google Cloud location-based electricity carbon footprint.



#### Electricity footprint allocation to customers

Solving these equations results in a total carbon footprint for each SKU in each region where the SKU is deployed. The last step for electricity calculations is to allocate the SKU regional carbon footprints to specific customers, aggregated into meaningful units (products, projects, regions). Here's an overview of this process:

  1. First, each SKU's carbon footprint is divided by the total SKU usage (volume metric) for a given region to establish each SKU's per-usage carbon intensity factor for that region.
  2. Each customer's usage of each SKU in each region is then multiplied by the respective SKU carbon intensity factor. This results in a per-SKU, per-region, per-customer footprint.
  3. The customer SKU footprints are then aggregated into customer-specific Google Cloud product footprints to increase the confidence in the reported carbon emission numbers.
  4. Finally, the data is aggregated to a monthly granularity to minimize daily fluctuations. The resulting report includes a customer specific location-based electricity carbon footprint that is totalized overall per month, with breakdowns per Google Cloud product, per customer-defined project, and per region.



Note that there is validation performed to ensure the aggregation of all the customer electricity carbon footprints is equal to the total Google Cloud location-based electricity carbon footprint.

#### Non-electricity emission sources

While emissions from electricity production represent the majority of Google Cloud's carbon emissions, other emission sources do contribute to the total. 

Carbon Footprint uses data streams for these non-electricity sources that originate with Google company-wide emissions inventory. As such, emissions from non-electricity sources are calculated and added to the Google Cloud footprint on a less dynamic and less granular basis than emissions from electricity. While we measure electricity use and associated location-based emissions on an hourly basis, emissions from other sources are established on either a monthly or annual basis, and are not available with any geographic specificity. Note that the Google company-wide data for embodied emissions of data center equipment and data center facilities has not been assured.

To allocate company-wide emissions from non-electricity sources to the customer-specific breakdowns in Carbon Footprint reports, we establish an allocation factor – a ratio of the customer's Google Cloud electricity use to the total Google Cloud electricity use – and multiply that factor by the worldwide Google Cloud emissions from each source, determined as described here.

  * **Embodied emissions of data center equipment:** This emission source encompasses the activities necessary to extract, refine, and transport materials to equipment manufacturing locations, and the emissions associated with the manufacturing processes. Using lifecycle analysis, Google has established a per-piece embodied emissions footprint for data center equipment. This footprint is then amortized over a 4-year timeframe (chosen to match our financial accounting standards though we see significantly longer lifetimes for our equipment in practice) to create an annual emissions burden for each piece of equipment. 

The total number of machines resident in Google data centers and the summed emissions of all equipment is updated monthly by adding the new machines and dropping those at the 4-year mark.

  * **Embodied emissions of data center facilities:** This emission source encompasses the activities necessary to extract, refine, and transport materials to data center construction locations, and the emissions associated with the construction itself - including site infrastructure such as coolant systems and power systems. Using lifecycle analysis, Google has established a data center construction emissions footprint, which is then scaled up or down based on the size (data capacity) of new data center additions. This scaled footprint is then amortized over a 20-year timeframe (chosen to match our financial accounting standards).

On a monthly basis, Google adds newly available building capacity to its running calculation of embodied facility emissions. 

  * **Fossil fuels combusted onsite:** This emission source encompasses all data center onsite fuels use, for example for backup power, water and space heating, and transportation (fleet vehicles). On an annual basis, Google collects all relevant records and sums its total data center fuels use and calculates the resulting carbon footprint as part of its annual emission reporting process. 

The total data center fuel emissions number is updated annually for Carbon Footprint calculations.

  * **Data center employee commuting and business travel:** This emission source encompasses travel and commuting associated with employees who work at Google data centers. On an annual basis, Google collects travel records and estimates of employee commute modes, in each case creating a worldwide total emissions footprint for the activity. This worldwide Google total is then downscaled to data center employees by multiplying the proportion of data center employees vs. Google's total employee count, to create the data center emissions total.

The total data center commute and travel emissions number is updated annually for Carbon Footprint calculations.




## Technical details

### Electricity use

This section describes Google's method for bottoms-up energy consumption calculations.

First, every machine runs workloads for one or more internal services. Google records the internal services using each machine, on an hourly basis. Similarly, Google also records power use by machine, on an hourly basis.

A machine's power use will be a mix of power used to execute workloads (dynamic power), and power used when the machine is idle (idle power). There are two different methods to allocate these machine-level power uses to the internal service level:

  * Each machine's hourly dynamic power is allocated to the internal services it supported during that hour. When a workload is running, the major resource contributor to energy consumption is CPU usage. Google monitors CPU usage inside its data centers per machine and internal service workload. If one internal service is using the machine, it allocates the machine's dynamic energy consumption to that internal service. If a machine supported more than one internal service, Google allocates the dynamic power proportional to the CPU usage of each internal service running on the machine.
  * Idle energy consumption is allocated to Google internal services based on each internal service's _resource allocation_ in the data center. An important driver of machines at idle is the desire to have compute resources (CPU, RAM, HDD, SDD) "at the ready" to execute uncertain but potentially large workloads without delay or interruption. Idle power is distributed based on the level of compute resources that has been purchased, whether or not the internal service is using those resources. This allocation results in idle power allocations per internal service, for each data center location.



Data center electric overhead load (power systems, cooling, lights) is then allocated to every machine within the data center. Google measures this load at the building level and estimates it more finely at the sub-building level, using validated algorithms as part of Google's Power Usage Effectiveness monitoring system. The sub-building estimates are allocated across the sub-building sector's deployed machines in the same proportions as the completed dynamic and idle power allocations.

Next, the power required by the shared infrastructure services software layer is allocated based on the usage of those infrastructure services by higher-level internal services. Overhead load for shared infrastructure services is included in their allocations. These allocations remain at the internal service (not machine) level.

For the internal services that don't have sufficient usage data, Google uses back-charged costs between the internal services to reallocate the shared infrastructure's energy consumption. For example, Artifact Registry uses Cloud Storage. So, the fraction of Cloud Storage's energy use that is reallocated to Artifact Registry is Artifact Registry's cost for using Cloud Storage's service divided by Cloud Storage's total costs. Some internal services are revenue-neutral. If an internal service is revenue-neutral or revenue-positive, all of its energy use will be reallocated to the other internal services that use it.

### Greenhouse gas emissions

This section describes [Electricity Maps'](https://app.electricitymap.org/map) calculation.

Grid carbon emission factors begin with electricity generation data from balancing authorities. This data provides the intraday energy mix, which is the relative production of electricity by the different electricity plants available on the grid. Electricity Maps then adds the real-time electricity import and export between interconnected grids.

Finally, Electricity Maps uses the Intergovernmental Panel on Climate Change (IPCC) (2014) electricity generation emission factors for each electricity generation source (e.g. coal, natural gas, hydropower, etc.) to create a volume-weighted hourly carbon intensity factor (emissions per megawatt-hour generated) for each electric grid. You can review Electricity Maps' carbon intensity factors [here](https://app.electricitymap.org/map). Electricity Maps' data acquisition pipeline, grid mix calculations, and emission factor methodology have received an independent [Letter of Limited Assurance from SGS](https://www.electricitymaps.com/resources/updates/independent-assurance-verified-electricity-maps-earns-letter-of-assurance-from-sgs), confirming compliance with international standards including ISO 14064 and GHG Protocol Scope 2 Guidance.

Note that Electricity Maps does not provide data for all Google Cloud locations, with particular gaps in Asia. Where such data is unavailable, Google uses country-specific annual average carbon intensity factors published by the International Energy Agency.

Google maps the relevant carbon emission intensity factors to each of its [Cloud locations](https://cloud.google.com/about/locations). We then multiply the hourly energy use for each internal service at each location, by the appropriate carbon emission intensity factor for that location to determine the internal service's location-based carbon footprint per hour and location. Each internal service's footprint is summed every 24 hours to create a daily footprint for that internal service in each location. These location-based footprints are summed daily into a internal service footprint per Google Cloud region, as well as a worldwide total.

### Allocation to SKUs and customers

Each internal service's location-based emissions are allocated to Google Cloud product units available for customer purchase (SKUs), and then the SKU location-based footprints are aggregated to Google Cloud product for the purpose of customer reports.

Every Google Cloud product comprises one or more customer-facing units available for purchase and identified by unique SKUs (see [all Google Cloud SKUs](https://cloud.google.com/skus)). For example, Cloud Storage is a service and Cloud Storage "_Standard Storage Finland_ ", "_Nearline Storage Finland_ ", "_Coldline Storage Finland"_ and "_Archive Storage Finland_ " are SKUs representing different classes of storage of the Cloud Storage service in Finland (see [all the Cloud Storage SKUs](https://cloud.google.com/skus?currency=USD&filter=95FF-2EF5-5EA1)).

Google Cloud uses "SKUs purchased" as the primary means of allocating each Google Cloud product's total location-based carbon footprint amongst Google Cloud customers. It helps to note that most Google Cloud SKUs are volumetric. For example, some storage SKUs are priced and purchased on a per-terabyte basis. The volume quantity of a customer's purchase of any given product (which we call "SKU usage") is an important factor in data center obligations and load.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

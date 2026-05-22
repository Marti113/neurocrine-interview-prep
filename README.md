# neurocrine-interview-prep

Python integration scripts demonstrating REST API integration, JSON transformation, and error handling — built as part of interview preparation for a Sr. API Integration Engineer role.

## Scripts

### ingrezza_fda_adverse_events.py
Pulls adverse event reports for INGREZZA (valbenazine) from the OpenFDA public API. Demonstrates:
- REST API calls using the `requests` library
- JSON response parsing and field extraction
- Data transformation and normalization
- Error handling for failed API responses

**Data source:** [OpenFDA Adverse Event Reporting API](https://api.fda.gov/drug/event.json)

## Skills Demonstrated
- Python scripting for API integration
- REST API consumption and JSON handling
- Data transformation patterns used in enterprise integration platforms (Workato, MuleSoft)
- Error handling for production-grade reliability

## Background
These scripts reflect the same integration patterns used in enterprise data pipelines — connecting systems, transforming data, and handling errors gracefully. The same logic applies whether the source is a REST API, Databricks, or Salesforce.

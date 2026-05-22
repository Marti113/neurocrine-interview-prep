import requests, json

# Step 1 - Call the FDA API
response = requests.get(
    "https://api.fda.gov/drug/event.json",
    params={"search": "patient.drug.medicinalproduct:INGREZZA", "limit": 5}
)

# Step 2 - Handle errors
if response.status_code != 200:
    print(f"API call failed with status: {response.status_code}")
else:
    data = response.json()
    results = data["results"]

    # Step 3 - Write clean records to a JSON file
    clean_records = []
    
    for event in results:
        clean_records.append({
            "report_date": event.get("receiptdate"),
            "serious": event.get("serious"),
            "country": event.get("occurcountry"),
            "reaction": event.get("patient", {}).get("reaction", [{}])[0].get("reactionmeddrapt", "unknown")
        })
    
    with open("ingrezza_adverse_events_output.json", "w") as f:
        json.dump(clean_records, f, indent=2)
    
    print(f"✅ {len(clean_records)} records written to ingrezza_adverse_events_output.json")

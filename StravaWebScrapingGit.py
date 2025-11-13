import requests
import pandas as pd

# API VALUES FROM STRAVA SHOULD BE HERE (got rid of them for privacy purposeS)
CLIENT_ID = ""
CLIENT_SECRET = ""
REFRESH_TOKEN = ""

# Get access token
token_resp = requests.post(
    "https://www.strava.com/api/v3/oauth/token",
    data={
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
    },
)
token_resp.raise_for_status()
access_token = token_resp.json()["access_token"]

#GET ACTIVITIES HERE
activities = []
page = 1

while True:
    resp = requests.get(
        "https://www.strava.com/api/v3/athlete/activities",
        params={"per_page": 200, "page": page},
        headers={"Authorization": f"Bearer {access_token}"},
    )
    resp.raise_for_status()
    data = resp.json()
    if not data:
        break
    activities.extend(data)
    page += 1

# Build DataFrame for ALL activities
rows = []
for a in activities:
    activity_type = a.get("type")

    start_local = a.get("start_date_local", "")
    simple_date = start_local[:10] if start_local else None

    #variables
    distance_m = a.get("distance", 0.0)
    moving_time_s = a.get("moving_time", 0)
    distance_km = distance_m / 1000 if distance_m else 0
    moving_time_min = moving_time_s / 60 if moving_time_s else 0
    pace_min_per_km = (
        moving_time_min / distance_km if distance_km > 0 else None
    )

    rows.append(
        {
            "date": simple_date,
            "name": a.get("name"),
            "activity_type": activity_type,
            "distance_km": distance_km,
            "moving_time_min": moving_time_min,
            "pace_min_per_km": pace_min_per_km,
            "avg_heart_rate": a.get("average_heartrate"),
            "elevation_gain_m": a.get("total_elevation_gain"),
        }
    )

df_acts = pd.DataFrame(rows)
df_acts.to_csv("strava_activities.csv", index=False)
print("Saved", len(df_acts), "activities to strava_activities.csv")

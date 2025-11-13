# Web Scraping to obtain a dataset of all your workouts from Strava

I like to participate in triathlons and train for these competitions. I’m constantly swimming, running, and biking, and I usually keep track of my performance on each workout I complete through the app Strava to get a summary of each workout (how long I workedout for, distance, heart rate, a map of the distance I ran, elevation, etc). When I started this project, I honestly thought I’d have way more workouts recorded, but later i found out I've only have around 200 workouts recorded.

I chose this topic because I wanted to take a deeper look at my training. I’ve never actually sat down and analyzed my performance with real data. This project gave me an excuse to pull everything from Strava and finally see patterns in how I train.

## Motivating Question

The main thing I want to learn from this dataset is to analyze my performance on each kind of workout i do

Questions to consider:

* Has my performance improved consistently?
* Is my strongest sport running, swimming, or biking?
* Are there big jumps where I suddenly got faster?
* Does working out more often actually make me better, or am I just tired all the time?


## Ethical Considerations

All the data I used is my own. Every workout comes from my watch syncing to Strava. I accessed my data through Strava’s official API, which is intended to let users access the information from their own profile

## How I Gathered the Data

1. Open Strava settings and go to the API section
2. Register a small "application" and later obtain the following values that's needed to access the data:

   * Client ID
   * Client Secret
   * Refresh Token
3. Use those values in Python to request an access token
4. Call Strava’s API to access my own profile from strava
5. Collect the JSON response and select the variables you care about
6. Clean and save the results into a CSV

## EDA Highlights

My final dataset includes:

* 200 workouts
* 5 different types of workouts: running, swimming, biking, weight training, walks
* 8 features such as distance, time, pace, heart rate, and elevation

### Interesting Findings

* I swim more than I thought, but most of my hours come from running
* My fastest paces aren’t always on the days I feel the best
* Elevation has a huge effect on pace
* I’m the most consistent during September and October
* My heart rate is much lower during swims compared to runs and rides

## Further Resources

* Strava Developer Docs: [https://developers.strava.com/](https://developers.strava.com/)
* Getting Started Guide: [https://developers.strava.com/docs/getting-started/](https://developers.strava.com/docs/getting-started/)

## Code Repository

* Code Repository: [[StravaWebScrapingGit.py](https://github.com/armandocarreon14/Data-Acquisition.git)]
* File Name: StravaWebScraping.py

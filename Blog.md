### Introduction / Motivation

I’ve always liked keeping track of my workouts. Since I’m training for a triathlon, I’m constantly swimming, running, and biking, and every little stat helps me understand how I’m doing. Strava is basically where I log everything, and I’ve used it for about a year and a half now. When I started this project, I honestly thought I’d have way more workouts recorded, but it turns out I’m only around the 200-workout mark.

I chose this topic because I wanted to take a deeper look at my training. I’ve never actually sat down and analyzed my performance with real data. This project gave me an excuse to pull everything from Strava and finally see patterns in how I train.

# Motivating Question

The main thing I want to learn from this dataset is: **What do I actually do best in?** Is my strongest sport running, swimming, or biking?

Beyond that:

* Has my performance improved consistently?
* Are there big jumps where I suddenly got faster?
* Does working out more often actually make me better, or am I just tired all the time?

These are things I’ve always wondered, and having all my workouts in one dataset makes it possible to explore them.

# Ethical Considerations

All the data I used is **my own**. Every workout comes from my watch syncing to Strava. I accessed my data through Strava’s official API, which is meant for users to download their own information. Nothing was taken from anyone else’s account, and no scraping of private pages was involved. Everything I did is allowed, ethical, and supported by Strava’s documentation.

# How I Gathered the Data

Here’s the quick version if someone wants to do a similar project:

1. Open Strava settings and go to the **API** section.
2. Register a small "application" to receive:

   * Client ID
   * Client Secret
   * Refresh Token
3. Use those values in Python to request an access token.
4. Call Strava’s API endpoint for activities.
5. Collect the JSON response and select the variables you care about.
6. Clean and save the results into a CSV.

You don’t need advanced skills — just basic Python and a Strava account.

# EDA Highlights

My final dataset includes:

* **200+ workouts**
* Activity types: running, swimming, biking, weight training, walks
* **8 features**, including distance, time, pace, heart rate, and elevation

### Interesting Findings

* I swim more than I thought, but most of my hours come from running.
* My fastest paces aren’t always on the days I feel the best.
* Elevation has a huge effect on pace.
* Some months I’m super consistent, others not so much.
* My heart rate is much lower during swims compared to runs and rides.

# Further Resources

* Strava Developer Docs: [https://developers.strava.com/](https://developers.strava.com/)
* Getting Started Guide: [https://developers.strava.com/docs/getting-started/](https://developers.strava.com/docs/getting-started/)

# Code Repository

Insert your GitHub link here.

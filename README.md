# Running the Repo
1. Clone it, cd into the repo
2. Run: ```docker build -t workout-web .```
3. Find the Docker Image Id by running: ```docker images```
4. Run: ```docker run -p 5000:5000 workout-web```
5. Go to localhost:5000 in a browser

# Current Status
Rebuilding as a React-Native app! Check it out [Here](https://github.com/ObiBaratt/rn-workout/tree/main)

# History
Workout Web is an attempt to create the workout tracking / program generating app I always wanted. I realized while doing this project that Full Stack Python was NOT the path forward, and that I needed to learn a full JavaScript stack in order to build the app I actually want. Additionally the ideal was always a mobile app.

Workout Web is, and will remain a fully functional Full Stack Web App with a solid backend, and a frontend severely limited by the tools I had available at the time. It's a legacy project that demonstrates how far I was able to get with pure Python and backend development for a Full Stack App.

## Main Page
![Main Page on Desktop](https://github.com/ObiBaratt/Workout-Web/blob/main/static/img/ww-main.jpg)
## User Homepage
![User Homepage on Desktop](https://github.com/ObiBaratt/Workout-Web/blob/main/static/img/ww-home.jpg)
## One Rep Max Calculator (Genereates 1-20 rep max based on user input)
![One Rep Max Calc on Desktop](https://github.com/ObiBaratt/Workout-Web/blob/main/static/img/ww-1rm.jpg)
## Program Generator (Example for a Bench / Overhead Press workout) on mobile.
![Workout Generation on Mobile](https://github.com/ObiBaratt/Workout-Web/blob/main/static/img/ww-res-prog.jpg)


# Future
I still love this project, and the idea behind it. Now that I've picked up Full Stack JavaScript I have significantly better tools to upgrade and work on this further. Specifically a full rewrite in React Native, with a serverless backend in order to get maximum flexibility between platforms. It will be mobile first design, as that's where I always wanted to take the original, but will have a fully functional webapp as well!

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import time

app = FastAPI(title="CloudPulse API")

START_TIME = time.time()
REQUEST_COUNT = 0


@app.get("/", response_class=HTMLResponse)
def home():

    return """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>ITISHREE ACHARYA | CSE-2</title>

<link rel="preconnect"
      href="https://fonts.googleapis.com">

<link rel="preconnect"
      href="https://fonts.gstatic.com"
      crossorigin>

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
      rel="stylesheet">


<style>

/* =====================================================
   RESET
===================================================== */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {

    font-family:
        Inter,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;

    background: #050505;

    color: #f5f5f7;

    overflow-x: hidden;
}


/* =====================================================
   NAVIGATION
===================================================== */

nav {

    position: fixed;

    top: 0;
    left: 0;

    width: 100%;

    height: 64px;

    display: flex;

    align-items: center;

    justify-content: space-between;

    padding: 0 7%;

    z-index: 100;

    background:
        rgba(5, 5, 5, 0.72);

    backdrop-filter:
        blur(20px);

    -webkit-backdrop-filter:
        blur(20px);

    border-bottom:
        1px solid
        rgba(255,255,255,0.08);
}


.logo {

    font-size: 17px;

    font-weight: 700;

    letter-spacing: -0.4px;
}


.logo span {

    color: #4f8cff;
}


.nav-links {

    display: flex;

    gap: 30px;

    list-style: none;
}


.nav-links a {

    color: #86868b;

    text-decoration: none;

    font-size: 13px;

    transition: 0.25s;
}


.nav-links a:hover {

    color: white;
}


/* =====================================================
   HERO
===================================================== */

.hero {

    min-height: 100vh;

    display: flex;

    align-items: center;

    position: relative;

    overflow: hidden;

    padding:
        120px 8% 80px;
}


/* ambient light */

.hero::before {

    content: "";

    position: absolute;

    width: 650px;
    height: 650px;

    right: -200px;
    top: 100px;

    background:
        radial-gradient(
            circle,
            rgba(55,105,255,0.18),
            transparent 68%
        );

    filter: blur(20px);

    pointer-events: none;
}


/* grid */

.hero::after {

    content: "";

    position: absolute;

    inset: 0;

    background-image:

        linear-gradient(
            rgba(255,255,255,0.025) 1px,
            transparent 1px
        ),

        linear-gradient(
            90deg,
            rgba(255,255,255,0.025) 1px,
            transparent 1px
        );

    background-size:
        60px 60px;

    mask-image:
        linear-gradient(
            to bottom,
            black,
            transparent
        );

    pointer-events: none;
}


.hero-content {

    max-width: 1050px;

    position: relative;

    z-index: 2;
}


.eyebrow {

    color: #4f8cff;

    font-size: 13px;

    font-weight: 600;

    letter-spacing: 2px;

    text-transform: uppercase;

    margin-bottom: 25px;

    animation:
        fadeUp 0.8s ease;
}


.hero h1 {

    font-size:
        clamp(
            60px,
            10vw,
            135px
        );

    line-height: 0.88;

    letter-spacing: -7px;

    font-weight: 700;

    margin-bottom: 35px;

    animation:
        fadeUp 0.9s ease;
}


.hero h1 span {

    color: #6e6e73;
}


.hero-description {

    max-width: 680px;

    color: #86868b;

    font-size: 20px;

    line-height: 1.65;

    margin-bottom: 38px;

    animation:
        fadeUp 1s ease;
}


/* =====================================================
   STUDENT INFO
===================================================== */

.student-info {

    border-left:
        3px solid
        #4f8cff;

    padding-left: 18px;

    margin-bottom: 35px;

    animation:
        fadeUp 1.1s ease;
}


.student-name {

    font-size: 21px;

    font-weight: 700;

    margin-bottom: 5px;
}


.college {

    color: #86868b;

    font-size: 14px;

    margin-bottom: 5px;
}


.course {

    color: #4f8cff;

    font-size: 12px;

    font-weight: 600;

    letter-spacing: 0.5px;
}


/* =====================================================
   BUTTONS
===================================================== */

.buttons {

    display: flex;

    gap: 13px;

    flex-wrap: wrap;

    animation:
        fadeUp 1.2s ease;
}


.btn {

    display: inline-flex;

    align-items: center;

    justify-content: center;

    padding:
        13px 21px;

    border-radius: 30px;

    text-decoration: none;

    font-size: 13px;

    font-weight: 600;

    transition:
        transform 0.25s,
        background 0.25s,
        border 0.25s;
}


.btn-primary {

    background: white;

    color: #000;
}


.btn-primary:hover {

    background: #4f8cff;

    color: white;

    transform:
        translateY(-3px);
}


.btn-secondary {

    border:
        1px solid
        #333;

    color: white;
}


.btn-secondary:hover {

    border-color: #4f8cff;

    color: #4f8cff;

    transform:
        translateY(-3px);
}


/* =====================================================
   SCROLL
===================================================== */

.scroll {

    position: absolute;

    bottom: 28px;

    left: 50%;

    transform:
        translateX(-50%);

    color: #555;

    font-size: 10px;

    letter-spacing: 3px;

    z-index: 5;

    animation:
        floating 2s infinite;
}


@keyframes floating {

    0%, 100% {
        transform:
            translate(-50%, 0);
    }

    50% {
        transform:
            translate(-50%, 6px);
    }
}


/* =====================================================
   ABOUT
===================================================== */

.about {

    background: #f5f5f7;

    color: #1d1d1f;

    padding:
        140px 8%;
}


.container {

    max-width: 1100px;

    margin: auto;
}


.section-label {

    color: #4f8cff;

    font-size: 12px;

    font-weight: 700;

    letter-spacing: 2px;

    text-transform: uppercase;

    margin-bottom: 15px;
}


.section-title {

    font-size:
        clamp(
            45px,
            7vw,
            80px
        );

    line-height: 0.95;

    letter-spacing: -4px;

    margin-bottom: 30px;
}


.about-text {

    max-width: 760px;

    color: #6e6e73;

    font-size: 20px;

    line-height: 1.75;
}


/* =====================================================
   CARDS
===================================================== */

.cards {

    margin-top: 60px;

    display: grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap: 18px;
}


.card {

    padding: 30px;

    background: white;

    border:
        1px solid
        #dedee2;

    border-radius: 18px;

    transition:
        transform 0.3s,
        box-shadow 0.3s;
}


.card:hover {

    transform:
        translateY(-7px);

    box-shadow:
        0 20px 50px
        rgba(0,0,0,0.08);
}


.card-number {

    color: #4f8cff;

    font-size: 12px;

    font-weight: 700;

    margin-bottom: 25px;
}


.card h3 {

    font-size: 20px;

    margin-bottom: 10px;
}


.card p {

    color: #6e6e73;

    font-size: 14px;

    line-height: 1.6;
}


/* =====================================================
   PROJECT
===================================================== */

.projects {

    background: #050505;

    padding:
        140px 8%;
}


.project {

    margin-top: 60px;

    padding: 40px;

    max-width: 900px;

    border:
        1px solid
        #222;

    border-radius: 24px;

    background:
        linear-gradient(
            145deg,
            #111,
            #080808
        );

    transition:
        transform 0.3s,
        border 0.3s;
}


.project:hover {

    transform:
        translateY(-5px);

    border-color:
        #4f8cff;
}


.project h3 {

    font-size: 30px;

    margin-bottom: 15px;
}


.project p {

    color: #86868b;

    line-height: 1.7;

    font-size: 15px;
}


.project-tech {

    margin-top: 25px;

    color: #4f8cff;

    font-size: 12px;

    font-weight: 600;
}


/* =====================================================
   CONTACT
===================================================== */

.contact {

    background: #f5f5f7;

    color: #1d1d1f;

    padding:
        140px 8%;

    text-align: center;
}


.contact p {

    max-width: 600px;

    margin:
        0 auto 30px;

    color: #6e6e73;

    line-height: 1.7;
}


/* =====================================================
   FOOTER
===================================================== */

footer {

    background: #050505;

    color: #555;

    padding: 30px;

    text-align: center;

    font-size: 12px;
}


/* =====================================================
   ANIMATION
===================================================== */

@keyframes fadeUp {

    from {

        opacity: 0;

        transform:
            translateY(25px);
    }

    to {

        opacity: 1;

        transform:
            translateY(0);
    }
}


/* =====================================================
   MOBILE
===================================================== */

@media(max-width: 750px) {

    .nav-links {

        display: none;
    }

    .hero h1 {

        letter-spacing: -4px;
    }

    .cards {

        grid-template-columns:
            1fr;
    }

    .about,
    .projects,
    .contact {

        padding:
            100px 7%;
    }

    .section-title {

        letter-spacing: -3px;
    }
}

</style>

</head>


<body>


<!-- =====================================================
     NAVIGATION
===================================================== -->

<nav>

    <div class="logo">
        ITISHREE<span>.</span>
    </div>


    <ul class="nav-links">

        <li>
            <a href="#home">
                Home
            </a>
        </li>

        <li>
            <a href="#about">
                About
            </a>
        </li>

        <li>
            <a href="#projects">
                Projects
            </a>
        </li>

        <li>
            <a href="#contact">
                Contact
            </a>
        </li>

    </ul>

</nav>



<!-- =====================================================
     HERO
===================================================== -->

<section
    class="hero"
    id="home"
>

    <div class="hero-content">


        <div class="eyebrow">

            Computer Science Student

        </div>


        <h1>

            ITISHREE
            <br>

            <span>ACHARYA</span>

        </h1>


        <p class="hero-description">

            I'm a Computer Science student
            exploring technology, programming,
            and the art of turning ideas into
            practical digital experiences.

        </p>


        <div class="student-info">

            <div class="student-name">

                ITISHREE ACHARYA

            </div>


            <div class="college">

                DRONACHARYA COLLEGE OF ENGINEERING

            </div>


            <div class="course">

                CSE-2 · COMPUTER SCIENCE & ENGINEERING

            </div>

        </div>


        <div class="buttons">

            <a
                href="#projects"
                class="btn btn-primary"
            >

                Explore My Work

            </a>


            <a
                href="#about"
                class="btn btn-secondary"
            >

                About Me

            </a>

        </div>

    </div>


    <div class="scroll">

        SCROLL

    </div>

</section>



<!-- =====================================================
     ABOUT
===================================================== -->

<section
    class="about"
    id="about"
>

<div class="container">


    <div class="section-label">

        About Me

    </div>


    <h2 class="section-title">

        Learning.
        <br>
        Building.
        <br>
        Growing.

    </h2>


    <p class="about-text">

        I'm Itishree Acharya, a CSE-2 student
        at Dronacharya College of Engineering.
        I'm interested in computer science,
        software development and modern
        technology. My goal is to keep learning,
        build meaningful projects and develop
        skills that can solve real-world problems.

    </p>


    <div class="cards">


        <div class="card">

            <div class="card-number">
                01
            </div>

            <h3>
                Technology
            </h3>

            <p>

                Exploring programming,
                software development and
                emerging technologies.

            </p>

        </div>


        <div class="card">

            <div class="card-number">
                02
            </div>

            <h3>
                Problem Solving
            </h3>

            <p>

                Developing logical thinking
                and learning how to approach
                technical challenges.

            </p>

        </div>


        <div class="card">

            <div class="card-number">
                03
            </div>

            <h3>
                Projects
            </h3>

            <p>

                Turning ideas into practical
                projects and continuously
                improving them.

            </p>

        </div>


    </div>

</div>

</section>



<!-- =====================================================
     PROJECTS
===================================================== -->

<section
    class="projects"
    id="projects"
>

<div class="container">


    <div class="section-label">

        Selected Work

    </div>


    <h2 class="section-title">

        Projects.

    </h2>


    <div class="project">

        <h3>
            CloudPulse
        </h3>


        <p>

            A containerized cloud monitoring
            API built with Python, FastAPI
            and Docker. The project demonstrates
            REST API development, containerization
            and preparation for cloud deployment.

        </p>


        <div class="project-tech">

            PYTHON · FASTAPI · DOCKER · REST API

        </div>

    </div>

</div>

</section>



<!-- =====================================================
     CONTACT
===================================================== -->

<section
    class="contact"
    id="contact"
>

<div class="container">


    <div class="section-label">

        Contact

    </div>


    <h2 class="section-title">

        Let's connect.

    </h2>


    <p>

        Interested in technology, projects
        or collaboration? Feel free to
        get in touch.

    </p>


    <a
        href="https://www.linkedin.com/in/itishree985?utm_source=share_via&utm_content=profile&utm_medium=member_android"
        class="btn btn-primary"
    >

        Contact Me

    </a>

</div>

</section>



<!-- =====================================================
     FOOTER
===================================================== -->

<footer>

    ITISHREE ACHARYA
    ·
    CSE-2
    ·
    DRONACHARYA COLLEGE OF ENGINEERING

</footer>


</body>

</html>
"""


# =====================================================
# HEALTH
# =====================================================

@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


# =====================================================
# INFO
# =====================================================

@app.get("/info")
def info():

    return {

        "name": "ITISHREE ACHARYA",

        "college":
            "DRONACHARYA COLLEGE OF ENGINEERING",

        "class": "CSE-2",

        "project": "CloudPulse",

        "technology":
            "Python + FastAPI + Docker"

    }


# =====================================================
# STATS
# =====================================================

@app.get("/stats")
def stats():

    global REQUEST_COUNT

    REQUEST_COUNT += 1

    uptime = round(
        time.time() - START_TIME,
        2
    )

    return {

        "uptime_seconds":
            uptime,

        "requests":
            REQUEST_COUNT

    }
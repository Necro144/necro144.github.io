<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0"><style>
body {
  background-color: black;
  font-family: Times New Roman, Verdana;
  color: white;
  padding: 20px;
}

.container {
  margin-top: 100px;
}

.profile-pic {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  border: 5px solid white;
  box-shadow: 0 0 100px rgba(255, 255, 100, 0.5);
}

.name {
  font-size: 28px;
  margin-top: 20px;
  text-shadow: 2px 2px 4px rgba(255, 255, 100, 0.5);
}

.title {
  font-size: 18px;
  margin-top: 10px;
  text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.5);
}

.email {
  margin-top: 10px;
  text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.5);
}

.glow {
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.7);
}

/* Adjust button styles for mobile */
.glow-button {
  display: block;
  margin: 30px 5;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  color: #fff;
  font-size: 30px;
  text-align: center;
  text-decoration: none;
  background-color: #000;
  box-shadow: 0 0 10px #000;
  transition: box-shadow 0.3s ease-in-out;
  width: 100%;
  max-width: 250px;
}

.glow-button:hover {
  box-shadow: 0 0 20px #ff0, 0 0 40px #ff0, 0 0 80px #ff0;
}

.glow-text {
  animation: glow 1s ease-in-out infinite alternate;
}

@keyframes glow {
  0% {
    text-shadow: 0 0 5px #ff0;
  }
  100% {
    text-shadow: 0 0 20px #ff0, 0 0 30px #ff0, 0 0 40px #ff0;
  }
}

/* Remove underline from links */
a {
  text-decoration: none;
}

/* Apply bold font weight to links */
a.bold {
  font-weight: bold;
}

/* Adjust font sizes for mobile */
@media only screen and (max-width: 600px) {
  .name {
    font-size: 22px;
  }
  .title {
    font-size: 16px;
  }
  .email {
    font-size: 14px;
  }
}
</style>

</head>
<body>
<div class="container">
  <img src="https://i.stack.imgur.com/l60Hf.png" alt="Profile Picture" class="profile-pic">
  <h1 class="name glow">Qusai Ali</h1>
  <h3 class="title glow">Lens Creator - Video Editor
  <h3 class="title glow">Photographer - Videographer - Writer</h3>

  <button class="glow-button">
    <span class="glow-text">Snapchat: </span><a href="https://www.snapchat.com/add/nekro.me" target="_blank" class="bold"> +Add</a>
  </button>

  <button class="glow-button">
    <span class="glow-text">Instagram: </span><a href="https://www.instagram.com/8si.ig" target="_blank" class="bold"> +Follow</a>
  </button>

  <button class="glow-button">
    <span class="glow-text">Mail: </span><a href="mailto:Necro144@yahoo.com" class="bold"> >Send</a>
  </button>

  <button class="glow-button">
    <span class="glow-text">CS1.6: </span><a href="https://necro144.github.io/members.html" class="bold"> View Members</a>
  </button>

  <p class="email glow-text">This website can be accessed via www.8si.me</p>


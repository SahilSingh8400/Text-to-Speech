const textInput = document.getElementById("textInput");
const counter = document.getElementById("counter");

const clearBtn = document.getElementById("clearBtn");

const speed = document.getElementById("speed");
const pitch = document.getElementById("pitch");

const speedValue = document.getElementById("speedValue");
const pitchValue = document.getElementById("pitchValue");

const themeBtn = document.getElementById("themeBtn");

const generateBtn =
  document.getElementById("generateBtn");

const emptyAudio =
  document.getElementById("emptyAudio");

const audioPlayer =
  document.getElementById("audioPlayer");

const status =
  document.getElementById("status");

const playBtn =
  document.getElementById("playBtn");


/* =========================
   CHARACTER COUNTER
========================= */

textInput.addEventListener("input", () => {

  counter.textContent =
    `${textInput.value.length} / 2000`;

});


/* =========================
   CLEAR TEXT
========================= */

clearBtn.addEventListener("click", () => {

  textInput.value = "";

  counter.textContent = "0 / 2000";

  textInput.focus();

});


/* =========================
   EXAMPLE TEXT
========================= */

const examples =
  document.querySelectorAll(
    ".examples button"
  );

examples.forEach(button => {

  button.addEventListener("click", () => {

    textInput.value =
      button.dataset.text;

    counter.textContent =
      `${textInput.value.length} / 2000`;

  });

});


/* =========================
   SPEED
========================= */

speed.addEventListener("input", () => {

  speedValue.textContent =
    `${Number(speed.value).toFixed(1)}×`;

});


/* =========================
   PITCH
========================= */

pitch.addEventListener("input", () => {

  const value =
    Number(pitch.value);

  pitchValue.textContent =
    value > 0 ? `+${value}` : value;

});


/* =========================
   DARK MODE
========================= */

themeBtn.addEventListener("click", () => {

  document.body.classList.toggle("dark");

});


/* =========================
   GENERATE UI
========================= */

generateBtn.addEventListener("click", () => {

  const text =
    textInput.value.trim();

  if (!text) {

    alert(
      "Please enter some text first."
    );

    textInput.focus();

    return;

  }


  /*

    UI DEMO ONLY

    Backend/TTS model will be
    connected later.

  */


  emptyAudio.classList.add("hidden");

  audioPlayer.classList.remove("hidden");

  status.textContent =
    "Audio ready";

});


/* =========================
   PLAY BUTTON DEMO
========================= */

let playing = false;

playBtn.addEventListener("click", () => {

  playing = !playing;

  playBtn.textContent =
    playing ? "Ⅱ" : "▶";

});
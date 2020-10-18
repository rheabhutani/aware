"use strict";
(function() {

  window.addEventListener("load", init);

  function init() {
    id("check-button").addEventListener("click", check);
    console.log("hi");
  }

  function check() {
    id('input-box').innerHTML = "";
    id("result").innerHTML = response;
    console.log("bitch");
  }

  function response() {
    return "real";
  }

  function id(id) {
    return document.getElementById(id);
  }

})();

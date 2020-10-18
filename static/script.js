"use strict";
(function() {

  window.addEventListener("load", init);

  function init() {
    id("check-button").addEventListener("click", check);
    
  }

  function check() {
    let data = id("input-box").value;
    console.log(data);
    id('input-box').innerHTML = "";
    response(data);
  }

  function response(data) {
    // Code to get data from python
    fetch("/")
      .then((res)=>{console.log(res)})
    let response = data;
    id("result").innerHTML = data;
  }

  function id(id) {
    return document.getElementById(id);
  }

})();

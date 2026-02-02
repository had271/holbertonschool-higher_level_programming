#!/usr/bin/node
// Select the element with id "red_header"
const redHeader = document.getElementById('red_header');

// Add click event listener
redHeader.addEventListener('click', () => {
  // Select the <header> element
  const header = document.querySelector('header')
  // Add the class "red"
  header.classList.add('red')
})

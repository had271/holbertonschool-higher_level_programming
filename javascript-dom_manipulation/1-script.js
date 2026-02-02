#!/usr/bin/node
const redHeader = document.getElementById('red_header');

redHeader.addEventListener('click', () => {
  const header = document.querySelector('header')
  header.style.color = '#FF0000'
})
